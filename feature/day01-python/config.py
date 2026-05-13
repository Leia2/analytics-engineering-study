from pathlib import Path
#Diretório atual do projeto
BASE_DIR = Path(__file__).parent

RAW_DATA_PATH = BASE_DIR /"data"/"raw"/"sales.csv"
PROCESSED_DATA_PATH = BASE_DIR /"data"/"processed"/"sales_clean.csv"

