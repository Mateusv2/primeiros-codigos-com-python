
# Exemplo simples de um sistema para cadastro de aluno utilizando Funções, While e condicionais

# Lista de dicionarios com nome e matricula de alunos
alunos = [
    {"nome": "Mateus", "matricula": "123"},
    {"nome": "Ana", "matricula": "456"},
    {"nome": "Alex", "matricula": "789"},
    {"nome": "Carla", "matricula": "987"}
]

# Funções para Adicionar, Remover e Verificar a lista de alunos no sistema
def adicionar_aluno():
    nome = input('Digite o nome do aluno: ')
    matricula = input('Digite o número da matrícula: ')
    alunos.append({"nome": nome, "matricula": matricula})
    print('Aluno adicionado com sucesso!')

def remover_aluno():
    matricula = input('Digite o número da matrícula do aluno que deseja remover: ')
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            alunos.remove(aluno)
            print('Aluno removido com sucesso!')
            return
    print('Aluno não encontrado.')

def listar_alunos():
    print('Lista de Alunos:')
    for aluno in alunos:
        print('Nome:', aluno['nome'], '- Matrícula:', aluno['matricula'])


# Criando um loop no While para dar mais dinamica e flexibilidade no processo de tarefas no sistema 

while True:
    print('''
      
      =================
            Menu
      =================
    
      Opções:
      
      1 - Adicionar Aluno
      2 - Remover Aluno
      3 - Lista de Alunos
      x - Sair

      ''')
    
    # Finalizando com um processo de condições com as chamadas das funções
    
    op = input('Digite a opção desejada: ')

    if op == 'x':
        print('Saindo...')
        break
    elif op == '1':
        adicionar_aluno()
    elif op == '2':
        remover_aluno()
    elif op == '3':
        listar_alunos()
    else:
        print('Opção inválida. Tente novamente.')