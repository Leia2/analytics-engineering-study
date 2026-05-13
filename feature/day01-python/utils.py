#Storage reusible functions here
import pandas as pd

def load_csv(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    #Make a copy of the original dataframe
    df = df.copy()
    df.columns = ( 
        df.columns.str.lower()
        .str.strip()
        .str.replace(" ", "_"))

    df = df.drop_duplicates()
    df = df.dropna() 
    return df

def save_csv(df: pd.DataFrame, file_path):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    return df.to_csv(file_path, index=False)


