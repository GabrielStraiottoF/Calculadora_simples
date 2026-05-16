import unicodedata
import time
from colorama import Fore, Style
import math

def remover_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sem_acentos = ''.join(
        char for char in texto_normalizado
        if unicodedata.category(char) != 'Mn'
    )
    return texto_sem_acentos

while True:
    print(Fore.GREEN +"Bem vindo a calculadora Básica o que você deseja fazer? \n Opeçaões básicas (0) \n Operações especiais (1)")
    p = int(input(Style.RESET_ALL))

    if p == 0:
        op = remover_acentos(str(input("Digite sua operação básica que você quer utilizar: \n"))).lower().replace(" ","")

        n = int(input("Digite um número: \n"))
        n2 = int(input("Digite um número: \n"))

        if op == "adicao":
            print(f"A soma de {n} + {n2} é igual a: \n{n + n2}")
            time.sleep(1)

        elif op == "subtracao":
            print(f"A subtração de {n} - {n2} é igual a: \n{n - n2}")
            time.sleep(1)

        elif op == "divisao":
            print(f"A divisão de {n} / {n2} é igual a: \n{n / n2}")
            time.sleep(1)

        elif op == "multiplicacao":
            print(f"A multiplicação de {n} . {n2} é igual a: \n{n * n2}")
            time.sleep(1)

        elif op == 'operacoesespeciais':
            print("Bem vindo as operações especia")

        else:
            print(Fore.RED + f"Por favor, coloque uma operação válida")
            time.sleep(1)
    elif p == 1:
        print("Tabela de Operações especiais: \n fatorial \n raiz quadrada \n raiz cubica \n")
        op = remover_acentos(str(input("Digite sua operação especial: \n"))).lower().replace(" ","")

        numero = int(input("Digite um número: \n"))

        if op == "fatorial":
            print(f"O fatorial do número {numero} é: \n{math.factorial(numero)}")

        elif op == "raizquadrada":
            print(f"A raiz quadrada do {numero} é: \n{math.sqrt(numero)}")

        elif op == "raizcubica":
            print(f"A raiz cubica de {numero} é \n{math.cbrt(numero)}")

        else:
            print(Fore.RED + "Digite um valor válido")
            print(Style.RESET_ALL)

    else:
        print(Fore.RED + "Digite um valor válido")  