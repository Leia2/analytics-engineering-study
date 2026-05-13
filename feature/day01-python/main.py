from config import RAW_DATA_PATH, PROCESSED_DATA_PATH
from utils import load_csv, clean_data, save_csv

def run_pipeline():
    """Run the CSV data pipeline"""
    print("Starting pipeline")
    
    df = load_csv(RAW_DATA_PATH)
    print(f"Rows loaded: {len(df)}")

    df_clean = clean_data(df)
    print(f"Rows after cleaning: {len(df_clean)}")

    save_csv(df_clean, PROCESSED_DATA_PATH)
    print("Pipeline completed")


if __name__ == "__main__":
    run_pipeline()



