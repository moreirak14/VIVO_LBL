import csv
from pathlib import Path


BASE_DIR = Path("CSV/")
csv_path = BASE_DIR / "lbl_scgn000026_20210716164414.csv"
json_path = 'JSON/pythonJSON.json'


def lineCSV():
    input_names = [ 'INPUT'';''REGIONAL'';''CEP'';''BAIRRO'';''MUNICIPIO'';''ENDERECO' ]

    with open(csv_path, 'r+') as file_csv:
        writer = csv.DictWriter(file_csv, fieldnames=input_names)
        writer.writeheader()

if __name__ == "__main__":
    lineCSV()
