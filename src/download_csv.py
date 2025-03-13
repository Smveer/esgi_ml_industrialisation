import pandas as pd

# Replace 'FILE_ID' with the actual file ID from your Google Drive shareable link
file_id = '1WJPZQEijYsfTga6il8Ls3pgjdsGhCrq0'
url = f'https://drive.google.com/uc?export=download&id={file_id}'

# Read the CSV file directly into a pandas DataFrame
df = pd.read_csv(url).to_csv('esgi_ml_industrialisation/data/raw/db.csv', index=False)
