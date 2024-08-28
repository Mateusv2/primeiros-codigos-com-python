# Codigo para adicionamos 10 Inteiro e depois separamos os valores pares e impares em duas listas diferente
# Informando também a quantidade desses numeros e a soma deles
pares = []
impares = []

for num in range(1, 11):
    valor = int(input(f'Digite um número: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

resultado_pares = (pares, len(pares), sum(pares))
print("Números pares:", resultado_pares)

resultado_impares = (impares, len(impares), sum(impares))
print("Números ímpares:", resultado_impares)



