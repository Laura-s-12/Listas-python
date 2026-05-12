'''

SISTEMA: CALCULADORA

'''

while True:
print(30*"-","calculadora",30*"-")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
print('1, soma')
print('2, subtração')
print('3, multiplicação')
print('4, divisão')
opcao = input('Digite a operação: (+,-,*,/): ')


match opcao:
    case '1':
     resultado = num1 + num2
     print(f'{num1} + {num2} = {resultado}')
     
    case '2':
     resultado = num1 - num2
     print(f'{num1} - {num2} = {resultado}')
     
    case '3':
     if num1 != 0 and num2 != 0:
     resultado = num1 * num2
     print(f'{num1} * {num2} = {resultado}')
     
    case '4':
     resultado = num1 / num2
     print(f'{num1} / {num2} = {resultado}')
     
    case _:
     print("Digite um numero valido:")
     
