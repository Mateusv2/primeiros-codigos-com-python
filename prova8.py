# Criando um loop com While para adicionamos a quantidade de valores que desejamos, a soma desses valores 
# e a média deles utilizando também a biblioteca random.

import random
valor = []
novo_valor = "Nada"
while novo_valor != 0:
    novo_valor = int(input('Digite um valor, (Caso queira encerrar digite 0):'))
    if novo_valor == '0':
        break
    valor.append(novo_valor)
print(f'Quantidade de valores, {len(valor)}')
print(f'Soma dos valores, {sum(valor)}')
print(f'Média dos valores, {sum(valor) / len(valor)}')
