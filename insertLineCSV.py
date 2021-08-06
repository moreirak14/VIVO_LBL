import csv
import tkinter.messagebox
from pathlib import Path


def insertlineCSV():

    csv_path = "CSV/"
    extension = "*.csv"
    input_names_str = ['INPUT;''REGIONAL;''CEP;''BAIRRO;''MUNICIPIO;''ENDERECO']

    for filename in Path(csv_path).rglob(extension):
        inputsfile = [filename]

    # Verifica se existe algum arquivo .csv para ser ajustado
    if (inputsfile != 0):
        with open(inputsfile[0], 'r') as read_file_csv:
            readFile = csv.reader(read_file_csv)
            lines = list(readFile)
            lines.insert(0, input_names_str)

        with open(inputsfile[0], 'w', newline='') as write_file_csv:
            writeFile = csv.writer(write_file_csv)
            writeFile.writerows(lines)

        write_file_csv.close()
        read_file_csv.close()

    elif (inputsfile == 0):
        tkinter.messagebox.showwarning(
            title="AVISO",
            message="Não têm nenhum arquivo CSV para ser ajustado")


if __name__ == "__main__":
    insertlineCSV()
