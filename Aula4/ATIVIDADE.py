'''

 atividade aula 4 

'''
# atividade 1 
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
div = n1/n2
print("O resultado da divisão é: ", div)

# atividade 2

temp1 = float(input("Digite a temperatura em fahrenheit: "))
temp2 = (temp1 - 32) * 5/9
print("A temperatura em Celsius é: ", temp2)

# atividade 3

dólares = float(input('Digite o valor de dólares: '))
reais = dólares * 5.25 
print(f'O valor de {dólares} dólares é igual a {reais} reais')
 
# atividade 4

print("Digite 3 numeros e vou calcular a média aritimedica entre eles: ")
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))
media = (n1 + n2 + n3) / 3
print("A média aritmética é: ", media)

# atividade 5

nome = input('Digite seu nome: ')
print(f"O nome digitado foi: {nome}")
print("O tipo de dado armazenado é: ", type(nome))

# atividade 6 

numeros = [1,2,3,4,5,6,7,8,9,10]
dobro = [x * 2 for x in numeros]

print("Números originais: '", numeros)
print("Número ao dobro: '", dobro)

# atividade 7 

num1 = int(input("Digite o primeiro numero:  "))
num2 = int(input("Digite o segundo numero:  "))
if num1 > num2: 
    print("O maior numero é: ", num1)

else:
    print("O maior numero é: ", num2)

# atividade 8 

nome1 = input("Digite o primeiro nome:") 
sobrenome1 = input('Digite o primeiro sobrenome do primeiro nome:')

nome2 = input("Digite o segundo nome: ")
sobrenome2 = input("Digite o segundo sobrenome do segundo nome:")
print("Combinação 1 : ", nome1, sobrenome1 )
print("Combinação 2 : ", nome2, sobrenome2)

# atividade 9 

numero = float(input("Digite um numero: "))
metade = numero/2
print("A metade do numero é: ", metade) 

# atividade 10 

altura = float(input("Digite o valor da altura: "))
base = float(input("Digite o valor da base:"))
resultado = base * altura
print("A área do retangulo é: ", resultado )

# atividade  11

num1 = int(input("Fale um numero que falarei o antecessor e o sucessor dela: "))
ant=num1-1
suc=num1+1
print(f"O numero escolhido foi {num1}\n Seu sucessor é: {suc}")

# atividade 12

from math import sqrt
num1=int(input("Fale um número"))
print(f"O dobro desse número é: {num1*2}\n O triplo é:{num1*3}\n e a raiz quadrada dele é {sqrt(num1)}")

# atividade 13

from math import sqrt
n1=int(input("Fale um número para calcular a raiz quadrada: "))
print(f"A raiz quadrada do número {n1} é {sqrt(n1)}")

# atividade 14

num1=int(input("Fale um número: "))
num2=int(input("Fale outro número: "))
num3=int(input("Fale outro número: "))
mult=num1*num2*num3
print(f"O produto de todos eles juntos é {mult}")

# atividade 15

p1=float(input("Fale um número e eu vou aplicar o desconto de 10% nela: "))
print(f"O valor que você colocou foi {p1} e com o desconto ficou {p1*0.90}")

# atividade 16

v1=int(input("Fale um valor:"))
t=int(input("Fale a taxa de juros: "))
i=int(input("Fale o tempo: "))
js=v1*t*i
print(f"O valor foi {v1}\nA taxa de juros foi de {t}\nE o juros simples foi {js} ")

# atividade 17

horas = float(input("Digite a quantidade de horas:"))
minutos = horas * 60
print ("Minutos:", minutos)

# atividade 18 

m=float(input("Digite o valor em metros:"))
cm=m*100
mm=m*1000
km=m*1000
print("Centímetros:", cm)
print("milimetros:", mm)
print("quilometros:",km)

# atividade 19 

distancia = float(input("Digite a distancia percorrida:"))
c = int(input("Digite a quantidade do combustivel gasto:"))
m = (distancia+c)/2
print(f"O consumo medio do veiculo foi dito {m} ")

# atividade 20 

numero = int(input("Digite um numero: "))
print("O numero diigitado foi: ", numero)
if numero < 0:
   numero = -numero
   print( "O valor absoluto do numero é: ", numero)
