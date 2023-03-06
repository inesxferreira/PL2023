from collections import defaultdict
import json
import re

from anyio import sleep

open = open('processos.txt', 'r')
f = open.readlines()
texto = ''.join(f)  # não pode ter espaços
texto_min = texto.lower()


# a)


def year():
    f_year = {}
    for ano in range(1500, 2100):
        freq = len(re.findall(rf'::{ano}', texto))
        if freq > 0:
            print("ANO", ano, "FREQUÊNCIA", freq)


#print("1 - Frequência de processos por ano")
# year()

# b))
def nome():
    # Dicionário para armazenar a frequência de nomes e apelidos por seculo
    nomes_por_seculo = defaultdict(lambda: defaultdict(int))
    for linha in f:
        try:
            # Extrai o século da data
            seculo = int(re.findall(r'\d{4}', linha)[0]) // 100 + 1

            # Extrai o nome e apelido da linha
            nome, apelido = re.findall(
                r'^\d+::.+? (.+?) (.+?)::', linha)[0]

            # Adiciona 1 à frequência do nome e apelido no século correspondente
            nomes_por_seculo[seculo][nome] += 1
            nomes_por_seculo[seculo][apelido] += 1
        except:
            # Ignora linhas mal-formatadas no processo
            pass

    # Imprime os 5 nomes e apelidos mais frequentes por século
    for seculo in sorted(nomes_por_seculo.keys()):
        print(f'Século {seculo}:')
        nomes_seculo = nomes_por_seculo[seculo]
        f_nomes = sorted(nomes_seculo.items(),
                         key=lambda x: x[1], reverse=True)[:5]
        for nome, frequencia in f_nomes:
            print(f'{nome}: {frequencia} ocorrências no ficheiro')
        print('\n')


# c)


def relacoes():
    f_relacoes = {}

    relacoes_validas = ["avo", "avos", "mae", "pai", "pais", "irmao", "irmaos", "tio", "tios", "neto",
                        "netos", "filho", "filhos", "bisavo", "bisavos", "primo", "primos", "sobrinho", "sobrinhos"]

    for relacao in relacoes_validas:
        occorencia = re.findall(rf'{relacao}', texto_min)

        # adiciona a relação ao dicionário e incrementa sua frequência
        f_relacoes[relacao] = len(occorencia)
        # imprime as frequências das relações
    for relacao, frequencia in f_relacoes.items():
        print(f'{relacao}: {frequencia} ocorrências')

# d)


def convert_to_json():
    data = []

    with open("TPC3/processos.json", "w", encoding="utf-8") as file:
        for line in range(20):
            registo = {}
            dados = line.strip().split("\n")
            for i, campo in enumerate(dados):
                key = 'processo.txt'.format(i+1)
                registo[key] = campo
            data.append(registo)

        json_str = json.dumps(data)
        file.write(json_str)


def menu():
    print("1-frequencia por ano")
    print("2-frequencia por seculo")
    print("3-frequencia por relação")
    print("4-Json")

    print("0-sair")

    print("\n")
    opcao = int(input("Qual a sua opção? "))
    print("\n")

    if opcao == 1:
        year()
    if opcao == 2:
        nome()
    if opcao == 3:
        relacoes()
    if opcao == 4:
        convert_to_json()
    if opcao == 0:
        print("Saindo...")


menu()
