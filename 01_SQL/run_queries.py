import duckdb
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
CSV_FILE_PATH = BASE_DIR / "data" / "ventas.csv"

QUERIES = {
    'consultas_top5.sql': 'resultados_top5.csv',
    'consultas_ingreso_total_cliente_mes.sql': 'resultados_ingreso_total_cliente_mes.csv'
}

def main():
    if not CSV_FILE_PATH.is_file():
        return

    con = duckdb.connect(database=':memory:')
    con.execute(f"CREATE VIEW ventas AS SELECT * FROM read_csv_auto('{str(CSV_FILE_PATH)}')")

    for sql_file, output_csv in QUERIES.items():
        query_file_path = SCRIPT_DIR / sql_file
        output_file_path = SCRIPT_DIR / output_csv
        
        try:
            if not query_file_path.is_file():
                continue
            
            with open(query_file_path, 'r') as f:
                sql_query = f.read()
            
            result_df = con.execute(sql_query).fetchdf()
            result_df.to_csv(output_file_path, index=False)
        except Exception:
            pass
    
    con.close()

if __name__ == "__main__":
    main()