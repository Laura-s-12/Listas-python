#for 

# laco de for, é finito: quando eu sei o numero de repeticoes
# lista_foutas = ['melancia','abacaxi','melão','pera']
# fruta = 'melancia'
#for f in fruta:
   # print(f)

# for range ( inicio,fim,salto ) 
# for i in range(1,20,2):
   # print("Repeti")

# num = input("Digite um numero para saber a sua tabuada: ")

#for i in range (1,11):
 #   print(f"{i} x {num} = {i*num}")'''


lista_nomes = ['Laura Sousa','Bianca Rodrigues','Jhonnhy Rodrigues','Davi Cavalcanti','Pedro Inácio',
               'Pedro Barbosa','Matheus Nonato','Victor Melo','Gustavo Melo',"Victor Fernando'"]

for i, nome in enumerate(lista_nomes):
    print(f'{i+1}º {nome}')

nome_buscar = input("Digite um nome para buscar: ").title()

if 'Bianca Rodrigues' in lista_nomes:
    print('Usuario encontrado!')

