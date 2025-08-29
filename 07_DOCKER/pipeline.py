import pandas as pd
from pathlib import Path

def extract_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return None

def transform_data(df):
    if df is None:
        return None

    df_transformed = df.copy()
    df_transformed['cantidad'] = df_transformed['cantidad'].fillna(0)
    df_transformed['precio'] = df_transformed['precio'].fillna(0)
    df_transformed['ingreso_total'] = df_transformed['cantidad'] * df_transformed['precio']
    return df_transformed

def load_data(df, output_path):
    if df is not None:
        df.to_csv(output_path, index=False)

if __name__ == "__main__":

    input_path = Path("data/ventas.csv")
    output_path = Path("ventas_procesadas.csv")

    ventas_df = extract_data(input_path)
    ventas_procesadas_df = transform_data(ventas_df)
    load_data(ventas_procesadas_df, output_path)