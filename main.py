import os
import time
import operator


def calculadora(num1: float, num2: float, operador: str) -> float:
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        if num2 == 0:
            return float("nan")
        result = num1 / num2
    elif operador == '%':
        if num2 == 0:
            return float("nan")
        result = num1 % num2
    elif operador == '^':
        result = num1 ** num2
    return result

aux = {"Nome": "João", "Idade": 25, "Profissão": "Programador"}

def calculadora_v2(num1, num2, operador):
    operacoes = {
        "+": lambda: num1 + num2,
        "-": lambda: num1 - num2,
        "*": lambda: num1 * num2,
        "/": lambda: float('nan') if num2 == 0 else num1 / num2,
        "%": lambda: float('nan') if num2 == 0 else num1 % num2,
        "^": lambda: num1 ** num2,
    }

    # A chave `operador` pode não existir no dicionário, então garantimos um default.
    funcao = operacoes.get(operador, lambda: float('nan'))
    return funcao()  # Avaliamos o lambda aqui, após a verificação.





def calculadora_v3(num1, num2, operador):
    operadores = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: float('nan') if y == 0 else x / y,
        "%": lambda x, y: float('nan') if y == 0 else x % y,
        "^": lambda x, y: x ** y,
    }

    # Verifica se o operador é válido.
    if operador in operadores:
        return operadores[operador](num1, num2)
    else:
        return float('nan')



# esta versão quando tentamos o expoente de 0, ele retornava um erro, foi retificado
def calculadora_v4(num1: float, num2: float, operador: str) -> float:
    if num2 == 0 and operador in ['/', '%']:
        return float("nan")

    operacoes = {
        "+": num1 + num2,
        "-": num1 - num2,
        "/": num1 / num2,
        "*": num1 * num2,
        "%": num1 % num2,
        "^": num1 ** num2,
    }

    return operacoes.get(operador, float("nan"))


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            numero1: float = float(input('Introduza o primeiro número: '))
            numero2: float = float(input('Introduza o segundo número: '))
            operacao: str = input('Introduza a operação a realizar (+ - / * %) ou (^): ')
            print(f'O resultado: {calculadora(numero1, numero2, operacao)}')  # Usa versão 1 por padrão
            print()
            cont: str = input('Deseja continuar? (s/n): ').lower()
            if cont == 'n':
                break

        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')
