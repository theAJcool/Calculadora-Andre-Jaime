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
        result = num1 % num2
    elif operador == '^':
        result = num1 ** num2
    return result



def calculadora_v2(num1: float, num2: float, operador: str) -> float:
    operacoes = {
        "+": lambda: num1 + num2,
        "-": lambda: num1 - num2,
        "/": lambda: num1 / num2,
        "*": lambda: num1 * num2,
        "%": lambda: num1 % num2,
        "^": lambda: num1 ** num2,
    }
    funcao = operacoes.get(operador)
    if funcao:
        return funcao()

    return float("nan")



def calculadora_v3(num1: float, num2: float, operador: str) -> float:
    operadores = {
        "+": operator.add,
        "-": operator.sub,
        "/": operator.truediv,
        "*": operator.mul,
        "%": operator.mod,
        "^": operator.pow,
    }

    if operador in operadores:
        return operadores[operador](num1, num2)

    return float("nan")



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
            print(f'O resultado: {calculadora(numero1, numero2, operacao)}')  
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
