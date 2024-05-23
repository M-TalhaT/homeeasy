# app/services/data_ingestion.py

import pandas as pd

def load_sales_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, parse_dates=['dated'])
    return df
