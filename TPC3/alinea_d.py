import json

with open('processos.txt', 'r') as f, open('processos.json', 'w') as output:
    data = []
    for i in range(20):
        line = f.readline().strip()
        campos = line.split('::')
        registos = {
            "id": campos[0],
            "data_nascimento": campos[1],
            "nome": campos[2],
            "nome_pai": campos[3],
            "nome_mae": campos[4],
            "outros_parentes": campos[5]
        }
        data.append(registos)

    # dump usada para escrever um objeto em python em formato JSON num arquivo
    json.dump(data, output, indent=4)
