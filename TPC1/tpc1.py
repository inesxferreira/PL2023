import matplotlib.pyplot as plt
import csv
from collections import defaultdict

# Definir a estrutura do modelo {key:[]}
modelo = defaultdict(list)

# Lendo o arquivo CSV e populando o modelo
with open('myheart.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:  # itera sobre as linhas
        #    print(row[0]) acede à primeira coluna
        for key, value in row.items():  # itera sobre as colunas  do dicionário da linha
            # adiciona o valor à lista correspondente do modelo
            modelo[key].append(value)


def distr_sexo():
    distribuicao = defaultdict(int)
    for i in range(len(modelo['sexo'])):
        if modelo['temDoença'][i] == '1':
            distribuicao[modelo['sexo'][i]] += 1
    return distribuicao


def distr_idade():
    distribuicao = defaultdict(int)
    for idade in range(30, 71, 5):
        key = f'{idade}--{idade+4}'
        distribuicao[key] = sum([1 for i in range(len(modelo['idade'])) if int(
            modelo['idade'][i]) >= idade and int(modelo['idade'][i]) < idade+5 and modelo['temDoença'][i] == '1'])
    return distribuicao


def distr_colesterol():
    distribuição = defaultdict(int)
    for colesterol in range(0, 500, 10):
        key = f'{colesterol}-{colesterol+10}'
        distribuição[key] = sum([1 for i in range(
            len(modelo['colesterol'])) if int(modelo['colesterol'][i]) >= colesterol and int(modelo['colesterol'][i]) <= colesterol+10 and int(modelo['temDoença'][i] == '1')])
    return distribuição

# Função que imprime a distribuição em forma de tabela


def imprime_distribuicao(distribuicao):
    print('Chave\t\tFrequência')
    for chave, quantidade in distribuicao.items():
        print(f'{chave}\t{quantidade}')


# Executando as funções e imprimindo as tabelas correspondentes
print('Distribuição por Sexo:')
imprime_distribuicao(distr_sexo())
print('\nDistribuição por idades:')
imprime_distribuicao(distr_idade())
print('\nDistribuição por Colesterol:')
imprime_distribuicao(distr_colesterol())


sexo = distr_sexo()
plt.pie(sexo.values(), labels=sexo.keys(), autopct='%1.1f%%')
plt.title('Distribuição da doença por sexo')
plt.show()

# Gráfico da distribuição por escalões etários
idade = distr_idade()
plt.bar(idade.keys(), idade.values())
plt.title('Distribuição de doença por idade')
plt.xlabel('Distribuição  por idade')
plt.ylabel('Frequência')
plt.show()

# Gráfico da distribuição de colesterol
colesterol = distr_colesterol()
plt.bar(colesterol.keys(), colesterol.values())
