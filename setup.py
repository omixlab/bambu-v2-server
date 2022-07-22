from setuptools import setup, find_packages

setup(
    name="bambu-server",
    version='0.0.1',
    packages=find_packages(),
    author="Frederico Schmitt Kremer",
    author_email="leitzke.gi@gmail.com, fred.s.kremer@gmail.com",
    description="bambu-server: model provisiong tool for Bambu",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    keywords="bioinformatics machine-learning data science drug discovery QSAR",
    entry_points = {'console_scripts':[
        'bambu-server   = bambu_server.server:main',
        'bambu-worker   = bambu_server.worker:main'
        ]},
    install_requires = [
        requirement.strip('\n') for requirement in open("requirements.txt")
    ]
)
