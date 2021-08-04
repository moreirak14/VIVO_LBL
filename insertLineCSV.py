import csv
from pathlib import Path
from turtle import pd

BASE_DIR = Path("CSV/")
csv_path = BASE_DIR / "lbl_scgn000026_20210716164414.csv"

def lineCSV():

    input_names_str = ['INPUT;''REGIONAL;''CEP;''BAIRRO;''MUNICIPIO;''ENDERECO']

    with open(csv_path, 'w') as file_csv:
        writer = csv.DictWriter(file_csv, fieldnames=input_names_str)
        writer.writeheader()

def lineCSV2():

    input_names_str = ['INPUT;''REGIONAL;''CEP;''BAIRRO;''MUNICIPIO;''ENDERECO']

    df = pd.read_csv(csv_path, header=None)
    df.to_csv("example.csv", header=["Letter", "Number", "Symbol"], index=False)

if __name__ == "__main__":
    lineCSV2()
