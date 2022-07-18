from .config import celery
from bambu.predict.run import model_predict_wrapper
from rdkit import Chem
from typing import List, Dict
import pandas as pd
import pickle
import os

@celery.task()
def run_bambu_models(molecules_smiles, config) -> Dict:

    molecules_smiles = [m for m in molecules_smiles.split('\n') if m]

    loaded_models = []
    model_names = []

    for model_data in config['models']:
        preprocessor = pickle.loads(open(model_data['preprocessor'], 'rb').read())
        model = pickle.loads(open(model_data['model'], 'rb').read())
        loaded_models.append((model_data['name'], preprocessor, model))
        model_names.append(model_data['name'])

    results = {'model_names': model_names, 'results': []}

    for molecule_smile in molecules_smiles:
        molecule_smile = molecule_smile.strip("\n").strip('\r')
        mol = Chem.MolFromSmiles(molecule_smile)
        results['results'].append({"molecule": molecule_smile, 'predictions': {}})
        for model_name, preprocessor, model in loaded_models:
            _, predicted_activity_proba = model_predict_wrapper(mol, model, preprocessor)
            results['results'][-1]['predictions'][model_name] = predicted_activity_proba
    
    return results



    