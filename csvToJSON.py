import csv
import json
from pathlib import Path


BASE_DIR = Path("CSV/")
csv_path = BASE_DIR / "lbl_scgn000026_20210716164414.csv"
json_path = 'JSON/pythonJSON.json'


def toJson():
    if csv_path.exists():
        with open(csv_path, 'r') as arquivo_csv:
            reader = csv.reader(arquivo_csv, delimiter=';')
            next(reader)
            data = {'INPUTs': []}
            for line in reader:
                data['INPUTs'].append({
                    'INPUT': line[0],
                    'REGIONAL': line[1],
                    'CEP': line[2],
                    'BAIRRO': line[3],
                    'MUNICIPIO': line[4],
                    'ENDERECO': line[5],
                })

        with open(json_path, 'w') as arquivo_json:
            json.dump(data, arquivo_json, indent=6)

if __name__ == "__main__":
    toJson()
