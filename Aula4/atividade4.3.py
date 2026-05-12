'''
Programa 02 
Prof: Karython 
turma: 2 DS

Sorteio 2.0

'''
import random
import os
import time

lista_nomes = []
lista_sorteados = []


print(30*("-", "Bem vindo ao sistema de sorteios"))

while True :
    nome= input("Digite um nome para ser sorteado: ")
    lista_nomes.append(nome)

    opcao = input ("Deseja adicionar mais ? (S- sim ) ou enter para parar!")
    if opcao != "s":
        break
    if not lista_nomes:
        print("A lista de nomes está vazia!")

    else:
        nome_sorteado = random.choiche(lista_nomes)
        lista_nomes.remove(nome_sorteado)
        lista_sorteados.append(nome_sorteado)
        os.system("cls")


nome_sorteado = random.choice(lista_nomes)
os.system("cls")

for i in range(5):
    time.sleep(1)
    os.system("cls")
    print(f'Contagem regressiva...{i}')
    i-=1

    print(f"O numero sorteado foi {nome_sorteado}")
    