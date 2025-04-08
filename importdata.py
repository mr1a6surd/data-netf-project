import os
import kaggle
import pandas as pd


#creer le dossier de dataset
os.makedirs("dataset",exist_ok=True)



# Télécharger et décompresser le dataset
kaggle.api.dataset_download_files('shivamb/netflix-shows', path='datasets', unzip=False)

import zipfile

with zipfile.ZipFile('datasets/netflix-shows.zip', 'r') as zip_ref:
    zip_ref.extractall('datasets')

print(" Dataset téléchargé et extrait dans le dossier 'datasets'")
