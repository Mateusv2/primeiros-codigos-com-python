
#Considere uma lista de números inteiros 
#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:

#Função map() para obter uma nova lista com o quadrado de cada número da lista numeros

#Função filter() para obter uma nova lista com números pares da lista numeros

#Função reduce()  para obter a soma de todos os números da lista numeros



pares = []
quadrado = []
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def map():
    for i in numeros:
       valor = i**2
       quadrado.append(valor)
    print(f'Os numeros ao quadrado dessa lista são: {quadrado}')

map()

def filter():
    for par in numeros:
        if par%2 == 0:
            pares.append(par)
    print(f'Os numeros pares dessa lista são: {pares}')

filter()

def reduce():
    print(f'A soma de todos os numeros da lista é: {sum(numeros)}')

reduce()