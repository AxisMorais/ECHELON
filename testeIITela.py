from tkinter import *

def mostrar():
    texto_resposta = Label(janela, text="Ola mundo" ,font=("GeosansLight", 14))
    texto_resposta.grid(column=0, row=2, padx=20, pady=20) 


Tk()

janela = Tk()
janela.title('Echelon System')
janela.geometry("800x500")

bg = PhotoImage(master= janela, file = "imgFundo.png")
LogoImagem = Label(janela, image=bg)
LogoImagem.place(x = 0, y = 0, relwidth=1, relheight= 1)

rotuloUm = Label(janela, text='Sistema Teste Interface', font=("GeosansLight", 12))
rotuloUm.grid(column = 0, row = 0)

botao = Button(janela, text="Clique para executar", font=("GeosansLight", 14), command = mostrar) 
botao.grid(column = 0 , row = 3 )


janela.mainloop()