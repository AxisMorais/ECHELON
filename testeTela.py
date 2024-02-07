from tkinter import *

def mostrar():
    texto_resposta = Label(janela, text="Ola mundo")
    texto_resposta.grid(column=0, row=2, padx=20, pady=20) 

def exibir():
    texto_respostaII = Label(janela, text="Ola mundo")
    texto_respostaII.grid(column=1, row=5, padx=20, pady=20) 


Tk()

janela = Tk()
janela.title('Programa Teste - Interface')
janela.geometry("800x500")

rotuloUm = Label(janela, text='Sistema Teste Interface')
rotuloUm.grid(column = 0, row = 0)

botao = Button(janela, text="Clique para executar", command = mostrar) 
botao.grid(column = 0 , row = 3 )

botaoII = Button(janela, text = "Clique aqui para abrir o segundo ola mundo", command = exibir)
botaoII.grid(column = 1 , row = 4 )

janela.mainloop()