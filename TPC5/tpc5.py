import re

estado = "inicial"
saldo = 0
moedasValidas = ["1c", "2c", "5c", "10c", "20c", "50c", "1e", "2e"]
while True:
    comando = input(">")
    if estado == "inicial":
        if (comando == "LEVANTAR"):
            estado = "espera"
            print("Aguardando inserção de moedas")
        else:
            print(
                "ERRO: O telefone está desligado. Levante o auscultador para iniciar uma chamada.")

    elif estado == "espera":

        if re.match("(?i:moeda)", comando):
            moedas = re.findall(r"\d+[ce]", comando)
            for moeda in moedas:
                if moeda in moedasValidas:
                    # acede ao ultimo caracter da string e adiciona ao saldo
                    if (moeda[-1] == "c"):
                        saldo += int(moeda[:-1])
                    if (moeda[-1] == "e"):
                        saldo += int(moeda[:-1])*100
                else:
                    print(f"{moeda} - moeda inválida; ")
            print(f"saldo = {int(saldo/100)}e{saldo%100}c")

        elif re.match("(?i:t=)", comando):
            if re.search(r't=(601|641)\d+', comando):
                print("chamada bloqueada")
            elif re.search(r't=(00)\d+', comando):
                if saldo <= 150:
                    print("saldo invalido")
                else:
                    saldo -= 150
            elif re.search(r't=(2)\d+', comando):
                if saldo <= 25:
                    print("Saldo invalido")
                else:
                    saldo -= 25
            elif re.search(r't=(808)\d+', comando):
                if saldo <= 10:
                    print("Saldo invalido")
                else:
                    saldo -= 10
            print(f"saldo = {int(saldo/100)}e{saldo%100}c")

        if re.match("(?i:POUSAR)", comando):
            print(f"troco = {int(saldo/100)}e{saldo%100}c; Volte sempre!")
            estado = "estado inicial"
            saldo = 0
        elif re.match("(?i:Abortar)", comando):
            estado = "estado inicial"
            saldo = 0
    else:
        if re.match("(?i:levantar)", comando):
            estado = "espera"
            print("Introduza moedas.")
