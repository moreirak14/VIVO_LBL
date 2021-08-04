import os
import tkinter.messagebox
import json
from pathlib import Path


JSON_FILE_PATH = "JSON/pythonJSON.json"
path_lbl = "LBL/"
filename_filter = "VIVO*.LBL"
path_filename_filter = "LBL/VIVO0212248.LBL"


def list_inputs():
    list = os.listdir(path_lbl)
    number_files = len(list)

    # Verifica se existe algum arquivo .lbl para ser ajustado
    if (number_files == 0):
        tkinter.messagebox.showwarning(title="AVISO", message="Não têm nenhum arquivo LBL para ser ajustado")

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
    list_inputs()
