import json
from pathlib import Path


BASE_DIR = Path("LBL/.")
JSON_FILE_PATH = "JSON/pythonJSON.json"
LBL_FILE_NAME = "VIVO0212248.lbl"
LBL_FILE_PATH = BASE_DIR / LBL_FILE_NAME


def main():
    if LBL_FILE_PATH.exists():

        with open(JSON_FILE_PATH, "r") as json_file:
            json_data = json.load(json_file)

        # Pega os dados do INPUT referente ao arquivo LBL
        input_data = None
        for input_ in json_data["INPUTs"]:
            if input_["INPUT"] == LBL_FILE_NAME.replace(".lbl", ""):
                input_data = input_

        assert input_data, "Não possui dados no arquivo JSON referente o arquivo lbl"

        with open(LBL_FILE_PATH, "r") as lbl_file:
            lbl_file_lines = lbl_file.readlines()

        separator = ":"
        for i, file_line in enumerate(lbl_file_lines):
            try:
                # Pega a posição do ":"
                separator_position = file_line.index(separator)

                # Pega a string que está antes dos ":"
                column = file_line[:separator_position]
                # Insere o dado do json referente a coluna do arquivo
                for key, value in input_data.items():
                    if column == key:
                        lbl_file_lines[i] = f"{column}{separator}  {value}\n"

            except ValueError:
                continue

        with open(LBL_FILE_PATH, "w") as result_file:
            result_file.writelines(lbl_file_lines)


if __name__ == "__main__":
    main()
