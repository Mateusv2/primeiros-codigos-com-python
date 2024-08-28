# Sistema simples para calcular a media e verificar a situação dos alunos


# Funções para calcular a media e avaliar a situação do aluno caso esteja aprovado ou não

def calcula_media(notas):
    media = sum(notas) / len(notas)
    return media

def verificar_situacao(media):
    if media == 10:
        print('Parabéns, sua média é 10')
    elif media >= 7:
        print('Aprovado')
    else:
        print('Reprovado')

# Uma lista vazia, onde será adicionados as medias dos alunos e poder verificar a situação deles 
notas_aluno = []


# Criando um loop no While para dar mais dinamica e flexibilidade no processo de tarefas no sistema 

while True:
    print('''
            ==============
                Menu
            ==============
          Opções:
          a - Média do Aluno
          b - Situação do Aluno
          x - Sair 
          
          ''')
    
    # Finalizando com um processo de condições com as chamadas das funções
    
    opcao = input('Escolha uma opção: ')

    if opcao == 'a':
        qtd_notas = int(input('Quantas notas você deseja inserir? ')) # Aqui o usuário poderá escolher a quantidade de notas que ela deseja trabalhar para calcular a média
        notas_aluno = []
        for i in range(qtd_notas): #Aqui temos um FOR com o range para criar um loop que se repete o numero de vezes que o usuário colocou na quantidade de nota acima 
            nota = float(input(f'Digite a nota {i+1}: ')) #Aqui é que o usuário colocar quais as notas do aluno. Lembrando que o usuário colocou anteriomente a quantidade de notas que ele quer para calcular a média e aqui é onde ele vai colocar valores dessas notas
            notas_aluno.append(nota) # Aqui colocamos os valores das notas na nossa lista
        media = calcula_media(notas_aluno) # E realizamos o calculo da média chamado a funçõa que contém a formula para o calculo
        print(f'A média do aluno é: {media}') #Imprimindo o resultado na tela
    elif opcao == 'b':
        if notas_aluno:
            media = calcula_media(notas_aluno)
            verificar_situacao(media) # Aqui chando a função para verificar a situação (Aprovado ou Reprovado) do aluno que adicionamos na lista
        else:
            print('É necessário calcular a média primeiro.')
    elif opcao == 'x':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Por favor, escolha novamente.')