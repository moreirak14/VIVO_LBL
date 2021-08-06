import os
import tkinter.messagebox
import json
import csv
from pathlib import Path


JSON_FILE_PATH = "JSON/pythonJSON.json"
path_lbl = "LBL/"
filename_filter = "VIVO*.LBL"
path_filename_filter = "LBL/VIVO0212248.LBL"


def insertlineCSV():

    csv_path = "CSV/"
    extension = "*.csv"
    input_names_str = ['INPUT;''REGIONAL;''CEP;''BAIRRO;''MUNICIPIO;''ENDERECO']

    for filename in Path(csv_path).rglob(extension):
        inputsfile = [filename]

    # Verifica se existe algum arquivo .csv para ser ajustado
    if (inputsfile == 0):
        tkinter.messagebox.showwarning(
            title="AVISO",
            message="Não têm nenhum arquivo CSV para ser ajustado")

    elif (inputsfile != 0):
        with open(inputsfile[0], 'r') as read_file_csv:
            readFile = csv.reader(read_file_csv)
            lines = list(readFile)
            lines.insert(0, input_names_str)

        with open(inputsfile[0], 'w', newline='') as write_file_csv:
            writeFile = csv.writer(write_file_csv)
            writeFile.writerows(lines)
        return toJson()


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
            return list_inputs_lbl()


def list_inputs_lbl():
    list = os.listdir(path_lbl)
    number_files = len(list)

    # Verifica se existe algum arquivo .lbl para ser ajustado
    if (number_files == 0):
        tkinter.messagebox.showwarning(
            title="AVISO",
            message="Não têm nenhum arquivo LBL para ser ajustado")

    elif (number_files != 0):
        return readerJSON()


def readerJSON():
    # Lista todos inputs do diretorio LBL/
    for filename in Path(path_lbl).rglob(filename_filter):
        inputsfile = [filename.name]
        print(inputsfile)

    with open(JSON_FILE_PATH, "r") as json_file:
        json_data = json.load(json_file)
        print(json_data)

    # Pega os dados do INPUT referente ao arquivo LBL
    input_data = None
    for input_ in json_data["INPUTs"]:
        if input_["INPUT"] == inputsfile:
            input_data = input_

    with open(path_filename_filter, "r") as lbl_file:
        lbl_file_lines = lbl_file.readlines()


if __name__ == '__main__':
    insertlineCSV()
