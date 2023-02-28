
from sys import stdin


def main():
    ativado = False  # variavel de controlo
    soma = 0

    for texto in stdin:
        texto = texto.lower()
        i = 0

        while i < len(texto):
            if texto[i] == "=":
                print(f"A soma dos números é: {soma}")
                i += 1
            else:
                if ativado:
                    if texto[i].isdigit():
                        j = i
                        while j < len(texto) and texto[j].isdigit():
                            j += 1
                        soma += int(texto[i:j])
                        i = j-1

                if texto[i:i+2] == "on":
                    ativado = True
                    i += 2
                elif texto[i:i+3] == "off":
                    ativado = False
                    i += 3
                else:
                    i += 1


main()
