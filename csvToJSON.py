import csv
import json
from pathlib import Path


def toJson():

    csv_path = "CSV/"
    extension = "*.csv"
    json_path = 'JSON/VIVO_LBL.json'

    for filename in Path(csv_path).rglob(extension):
        inputsfile = [filename]

    if (inputsfile != 0):
        with open(inputsfile[0], 'r') as arquivo_csv:
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
