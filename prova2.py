# Mesmo exemplo simples utilizando o While com uma resolução diferente
email_cadastrado = 'mirandaabc@gmail.com'
senha_cadastrada = '12345'

while True:
    email_usuario = input('Digite seu e-mail: ')
    senha_usuario = input('Digite sua senha: ')
    
    if email_usuario == email_cadastrado or senha_usuario == senha_cadastrada:
        print('E-mail ou senha já cadastrada')
        break
   