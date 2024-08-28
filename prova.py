# Exemplo simples utilizando o While

email_cadastrado = 'mirandaabc@gmail.com'
senha_cadastrada = '12345'

while True:
    email_usuario = input('Digite seu e-mail: ')
    senha_usuario = input('Digite sua senha: ')
    
    if email_usuario == email_cadastrado:
        print('E-mail já cadastrado')
        break
    if senha_usuario == senha_cadastrada:
        print('Senha já cadastrada')
        break

