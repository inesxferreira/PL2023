import csv
import re
import json

dict4 = {}


def read(csv_file):
    with open(csv_file, 'r', encoding="utf-8") as f:
        dataset = f.readlines()
        return dataset  # uma compreensão de lista,cada item será uma linha do arquivo CSV


def main(csv_file, json_file):
    data = []
    dataset = read(csv_file)

    # Abre o ficheiro json em modo escrita
    with open(json_file, "w", encoding="utf-8") as f:

        # Guarda os campos do cabeçalho, garante que não é seguida por um ou mais digitos e uma chave }
        fields = re.split(r',(?!\d+})', dataset[0].strip())

        for line in dataset[1:]:
            info = line.strip().split(',')

            for index, field in enumerate(fields):
                if field != '':

                    # Verifica se no campo tem um intervalo associado
                    intervalo = re.search(r'{(\d+),?(\d+)?}', field)

                    if intervalo:
                        if intervalo.group(2):
                            group1 = int(intervalo.group(1))
                            group2 = int(intervalo.group(2))
                        else:
                            group1 = int(intervalo.group(1))

                    # procurar media, sum etc
                    m = re.search(r'(?<=(::))\w+', field)

                    if m:
                        # Atualiza o campo com nome da soma, media etc
                        field = m.group(0)

                    # Guarda os números numa lista,
                    if intervalo:
                        lista = [int(num)
                                 for num in info[index:index + group2] if num != '']
                        if len(lista) < group1:
                            print("error in dataset")
                            break

                        # Verifica se o campo é uma das funções disponíveis; se não for associa ao campo a lista
                        elif field == "sum":
                            dict4[field] = sum(lista)
                        elif field == "media":
                            dict4[field] = sum(lista) / len(lista)
                        else:
                            dict4[field.split('{')[0]] = lista
                    # Se não existir guarda apenas a única informação presente
                    else:
                        dict4[field] = info[index]

            # Armazena o dicionário registo numa lista
            data.append(dict4)

        # Escreve no ficheiro .json
        json_str = json.dumps(data, ensure_ascii=False,indent=4)
        f.write(json_str)


#main("3ano2sem/PL/TPC4/alunos.csv", "3ano2sem/PL/TPC4/alunos.json")
#main("3ano2sem/PL/TPC4/alunos2.csv", "3ano2sem/PL/TPC4/alunos2.json")
#main("3ano2sem/PL/TPC4/alunos3.csv", "3ano2sem/PL/TPC4/alunos3.json")
#main("3ano2sem/PL/TPC4/alunos4.csv", "3ano2sem/PL/TPC4/alunos4.json")
main("3ano2sem/PL/TPC4/alunos5.csv", "3ano2sem/PL/TPC4/alunos5.json")
