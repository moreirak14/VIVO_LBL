import os
import tkinter.messagebox
import json
from pathlib import Path


JSON_FILE_PATH = "JSON/pythonJSON.json"
path_lbl = "LBL/"
filename_filter = "VIVO*.LBL"


def list_inputs():
    list = os.listdir(path_lbl)
    number_files = len(list)
    #print(number_files)

    # Verifica se existe algum arquivo .lbl para ser ajustado
    if (number_files == 0):
        tkinter.messagebox.showwarning(title="AVISO", message="Não têm nenhum arquivo LBL para ser ajustado")


def readerJSON():
    # Lista todos inputs de determinado diretorio
    for filename in Path(path_lbl).rglob(filename_filter):
        print(filename)

    with open(JSON_FILE_PATH, "r") as json_file:
        json_data = json.load(json_file)
        print(json_data)


if __name__ == '__main__':
    list_inputs()
    readerJSON()