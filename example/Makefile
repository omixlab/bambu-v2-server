export MAKEFLAGS="-j 2"

dirs:
	mkdir -p data/raw
	mkdir -p data/preprocess
	mkdir -p data/train

download:
	bambu-download \
	--pubchem-assay-id 39 \
	--pubchem-InchI-chunksize 100 \
	--output data/raw/data.csv

preprocess:
	bambu-preprocess \
	--input data/raw/data.csv \
	--output data/preprocess/data.csv \
	--output-preprocessor data/preprocess/preprocessor.pickle \
	--feature-type morgan-2048 \
	--train-test-split 0.75 \
	--undersample

train:
	bambu-train \
		--input-train data/preprocess/data_train.csv \
		--output data/train/model.pickle \
		--time-budget 60 \
		--estimators extra_tree

server:
	bambu-server \
		--host 0.0.0.0 \
		--port 8081 \
		--config configuration.json

worker:
	cd ../ && celery -A bambu_server.worker.celery worker

lifecycle: download preprocess train

deploy: worker server

