# Calculadora V2 - Refatorada com funções, if/elif, while

# Funções de operações matemáticas
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

# Função principal da calculadora
def calculadora(num1, num2, operacao):
    if operacao in ["+", "adicao", "soma"]:
        return adicao(num1, num2)
    elif operacao in ["-", "subtracao"]:
        return subtracao(num1, num2)
    elif operacao in ["*", "multiplicacao"]:
        return multiplicacao(num1, num2)
    elif operacao in ["/", "divisao"]:
        return divisao(num1, num2)
    else:
        return "Operação inválida!"

# Loop principal
saida = ""

while saida.lower() != "n":
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    op = input("Digite a operação (+, -, *, / ou nome): ")

    resultado = calculadora(n1, n2, op)
    print("Resultado da operação:", resultado)

    saida = input("Deseja continuar? (S/N): ")
