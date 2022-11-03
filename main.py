#main.py
from tkinter import *
from tkinter import Tk,ttk, messagebox
from calcular import Calculadora

#CORES UTILIZADAS ---------------------------
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra

#criando janela --------------------
janela = Tk ()
janela.title ("Calculadora")
janela.geometry('360x360')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# Frames - Dividindo a janela ---------------------------
frame_cima = Frame(janela,width=360, height=50,bg=co1, relief="flat")
frame_cima.grid(row=0, column=0,pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela,width=360, height=310,bg=co2, relief="flat")
frame_baixo.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

# configurando frame_cima ---------------------------
l_nome = Label(frame_cima, text="Insira dois valores:", height=1,anchor=NE, font=('Ivy 15 '), bg=co1, fg=co4)
l_nome.place(x=5, y=5)


#Configurando uma linha para estilização ---------------------------
l_linha = Label(frame_cima,width=275, text="", height=1,anchor=NW, font=('Ivy 1 '), bg=co2)
l_linha.place(x=10, y=45)


#Definindo metodo para criar a calculadora e realizar as operações
def calcular(num1, num2, op):   
    try:
        n1 = int(num1)
        n2 = int(num2)
        c = Calculadora(n1, n2, op)
        messagebox.showinfo('O valor é', c.calculo())  

    except:
        messagebox.showwarning('Erro', 'Algo de errado não está certo')

# configurando frame_baixo ---------------------------
l_nome = Label(frame_baixo, text="Valor 1", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_valor_um = Entry(frame_baixo, width=25, justify='left',font=("",15),highlightthickness=1, relief="solid")
e_valor_um.place(x=14, y=50)

l_pass = Label(frame_baixo, text="Valor 2", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_valor_dois = Entry(frame_baixo, width=25, justify='left',font=("",15),highlightthickness=1,relief="solid")
e_valor_dois.place(x=15, y=130)

# configurando os botões ---------------------------

botao_soma = Button(frame_baixo, text="+", command=lambda: calcular(e_valor_um.get(), e_valor_um.get(), "+"),  width=4, height=4, bg=co1, fg=co2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_soma.place(x=20, y=180)

botao_soma = Button(frame_baixo, text="-", command=lambda:calcular(e_valor_um.get(), e_valor_um.get(), "-"),  width=4, height=4, bg=co1, fg=co2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_soma.place(x=70, y=180)


botao_soma = Button(frame_baixo, text="*", command=lambda:calcular(e_valor_um.get(), e_valor_um.get(), "*"),  width=4, height=4, bg=co1, fg=co2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_soma.place(x=120, y=180)


botao_soma = Button(frame_baixo, text="/", command=lambda:calcular(e_valor_um.get(), e_valor_um.get(), "/"),  width=4, height=4, bg=co1, fg=co2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_soma.place(x=170, y=180)

janela.mainloop()
