'''
  programa 01 - Aula 04 - 28/04
  prof: Karython Gomes
  turma: 2 DS
  
  Sistema de sorteio 1.0
  
'''
import os 
import random 

lista_nomes = ['Laura Sousa','Bianca Rodrigues','Jhonnhy Rodrigues','Davi Cavalcanti','Pedro Inácio',
               'Pedro Barbosa','Matheus Nonato','Victor Melo','Gustavo Melo',"Victor Fernando'"]

sorteados = 0 
while sorteados < 5:
    nome_sorteado = random.choice(lista_nomes)
    print(f'sorteado: {nome_sorteado}')
    lista_sorteados.append(nome_sorteado)

    sorteados +=1

print(f'Lista antes de remover: {len(lista_nomes)}')
lista_nomes.remove(nome_sorteado)
print(f'Lista atualizada: {len(lista_nomes)}')


for i in lista_sorteados:
    print(f'Lista de sorteados: {i}')

sorteados +=1

print('fim do programa')

