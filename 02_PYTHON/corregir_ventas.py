import pandas as pd
from pathlib import Path

def analyze_sales(csv_file_path):
    df = pd.read_csv(csv_file_path)

    df['cantidad'] = df['cantidad'].fillna(0)

    result = df.groupby('cliente_id')['cantidad'].sum()

    result_sorted = result.sort_values(ascending=False)

    return result_sorted

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    input_path = base_dir / "data" / "ventas.csv"

    analysis_result = analyze_sales(input_path)