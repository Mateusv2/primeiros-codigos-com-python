# Criando um sistema simples para calcular a tabuado de qualquer numero inteiro
valor = int(input('Tabuada de: '))

for tabuada in range(1,11):
    valor1 = valor * tabuada

    print(f'{valor} X {tabuada} = {valor1}')

