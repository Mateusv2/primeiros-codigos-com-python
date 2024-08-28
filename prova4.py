# Mesmo exemplo do codigo anterior mais começando com a lista vazia

alunos = []

def AdicionarAluno():
    nome = input("Digite o nome do aluno(a): ")
    matricula = input("Digite o número de matrícula do aluno(a): ")
    alunos.append({"nome": nome, "matricula": matricula})
    print("Aluno(a) adicionado com sucesso!")

def RemoverAluno():
    matricula = input("Digite o número de matrícula do aluno(a) que deseja remover: ")
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            print("Aluno(a) removido com sucesso!")
            return
    print("Aluno(a) não encontrado.")

def ListaAlunos():
    if alunos:
        print("Lista de alunos:")
        for aluno in alunos:
            print("Nome:", aluno["nome"], "- Matrícula:", aluno["matricula"])
    else:
        print("Nenhum aluno(a) cadastrado.")

while True:
    
    print("\nEscolha uma opção:")
    print("1. Adicionar aluno(a)")
    print("2. Remover aluno(a)")
    print("3. Ver alunos")
    print("5. Sair")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        AdicionarAluno()
    elif opcao == "2":
        RemoverAluno()
    elif opcao == "3":
        ListaAlunos()
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")