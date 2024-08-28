# Conversor simples de centimetro para metro, pelo tkinter
from tkinter import *

janela = Tk()

# Criando uma função que ao ser chamada tomará a ação que desejamos,
#  que no caso será realizar a conversão e mostra o resultado
def conversor():
    valor = float(valor_para_converter.get()) / 100
    mostra_resultado.config(text=str(valor), foreground="black", background='white')

# Vinculando as variaveis criadas na interface do tkinter
valor_para_converter = StringVar()

# Criando a interface do tkinter
mostra_resultado = Label(janela, font=('Arial', 15))
rotulo = Label(janela, text="Conversor: ", font=("Times New Roman", 15), foreground="blue")
input_do_valor = Entry(janela, textvariable=valor_para_converter)
button = Button(janela, text="Clique aqui", command=conversor)

rotulo.pack()
input_do_valor.pack()
button.pack()
mostra_resultado.pack()
janela.mainloop()









