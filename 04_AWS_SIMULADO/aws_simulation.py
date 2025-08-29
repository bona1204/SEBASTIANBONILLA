import os
import time
import pandas as pd
from pathlib import Path

def process_file(filepath, output_dir, processed_dir):
    try:
        df = pd.read_csv(filepath)
        sales_by_product = df.groupby('producto_id')['cantidad'].sum().reset_index()

        output_filename = f"summary_{filepath.name}"
        output_path = output_dir / output_filename
        sales_by_product.to_csv(output_path, index=False)

        processed_path = processed_dir / filepath.name
        filepath.rename(processed_path)

    except Exception:
        pass

def main():
    script_dir = Path(__file__).resolve().parent
    input_dir = script_dir / 'input'
    output_dir = script_dir / 'output'
    processed_dir = script_dir / 'processed'

    processed_files = set()
    while True:
        for filename in os.listdir(input_dir):
            if filename.endswith('.csv') and filename not in processed_files:
                filepath = input_dir / filename
                process_file(filepath, output_dir, processed_dir)
                processed_files.add(filename)
        time.sleep(5)

if __name__ == "__main__":
    main()