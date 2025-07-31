from tkinter import *
from threading import Thread
from Main import vinibubumguloso


c0 = '#FF5733'
c1 = '#33FF57'
c2 = '#3357FF'
c3 = '#F1C40F'
c4 = '#9B59B6'
c5 = '#FF5733'

def testar_internet():
    label_resultado.config(text="⏳ Testando, aguarde...")
    botao.config(state=DISABLED)
    Thread(target=rodar_teste).start()

def rodar_teste():
    resultado = vinibubumguloso()

    if "erro" in resultado:
        texto = f"✖️ ERRO: {resultado['erro']}"
    else:
        texto = (
            f"📶 Ping: {resultado['ping']:.2f} ms\n"
            f"⬇️ Download: {resultado['download']:.2f} Mbps\n"
            f"⬆️ Upload: {resultado['upload']:.2f} Mbps"
        )
    label_resultado.config(text=texto)
    botao.config(state=NORMAL)


janela = Tk()
janela.title("Teste de Internet")
janela.geometry('350x200')
janela.configure(background=c2)
janela.resizable(width=False, height=False)


janela.iconbitmap('180163.ico')

frame_logo = Frame(janela, width=350, height=60, background=c1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corp = Frame(janela, width=350, height=140, background=c2)
frame_corp.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

botao = Button(frame_corp, text="Testar Velocidade", command=testar_internet, bg=c4, fg="white")
botao.pack(pady=10)

label_resultado = Label(frame_corp, text="", bg=c2, fg="white", justify=LEFT, font=("Arial", 10))
label_resultado.pack()

janela.mainloop()