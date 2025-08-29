import pandas as pd
from pathlib import Path

def get_top_clients(json_file_path, output_csv_path):
    df = pd.read_json(json_file_path)
    top_clients = df.groupby('cliente')['monto'].sum().nlargest(3)
    top_clients.to_csv(output_csv_path)

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    input_path = base_dir / "data" / "compras.json"
    output_path = Path(__file__).resolve().parent / "top_clientes.csv"

    get_top_clients(input_path, output_path)