#Importando a biblioteca do tkinter para utilizamos no codígo
from tkinter import * 
import tkinter

# Criando a jenela onde aparecera todo o precesso que sera realizado
janela = Tk()

# Criando uma função que ao ser chamada tomará a ação que desejamos, que no caso será mostra uma mensagem
def mostrar_mensagem():
    email = email_do_usuario.get()
    senha = senha_do_usuario.get()

    if len(senha) > 6 and '@' in email:
        mensagem.config(text='Seja bem-vindo(a)', font=("Times New Roman",15), foreground="blue")
    else:
        mensagem.config(text='Por favor, verifique o e-mail e a senha.', font=("Times New Roman",15), foreground="red")


# Vinculando as variaveis criadas na interface do tkinter

email_do_usuario = tkinter.StringVar()
senha_do_usuario= tkinter.StringVar()

# Criando a interface do tkinter
    
rotulo = Label(janela,text="E-mail: ",font=("Times New Roman",15),foreground="blACK")
input_do_nome= Entry(janela,textvariable=email_do_usuario,width=50)
label_senha= Label(janela,text="Senha",fg="blACK", font=('Times New Roman',15))
label_aviso= Label(janela,text="(senha no minimo 7 dígitos)",fg="black", font=('Times New Roman',10))
campo_da_senha= Entry(janela,textvariable=senha_do_usuario,show="*",width=50)
button = Button(janela,text="Clique aqui",command=mostrar_mensagem,width=30) # Chamando a função quando o usuário clicar no botão
mensagem= Label(janela,font=("Times New Roman",15))




rotulo.pack()
input_do_nome.pack()
label_senha.pack()
campo_da_senha.pack()
label_aviso.pack()
button.pack()
mensagem.pack()


janela.mainloop()