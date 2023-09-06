print("\n**********Calculadora Simples**********")
def soma (n1, n2):
    resultado = n1 + n2
    print("O resultado da soma é: ", resultado)

def subtracao (n1, n2):
    resultado = n1 - n2
    print("O resultado da soma é: ", resultado)

def multiplicacao (n1, n2):
    resultado = n1 * n2
    print("O resultado é: ", resultado)

def divisao (n1, n2):
    resultado = n1 / n2
    print("O resultados é: ", resultado)

print ("\nDigite a operação desejada: ")
operacao = input("1-soma\ 2-subtração\ 3-multiplicação\ 4-divisão :")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if "1" in operacao:
    print(soma(n1, n2))
elif "2" in operacao:
    print(subtracao(n1,n2))
elif "3" in operacao:
    print(multiplicacao(n1,n2))
elif "4" in operacao:
    print(divisao(n1,n2))
else:
    print("Fim da operação")
