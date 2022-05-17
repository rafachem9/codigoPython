import tkinter as tk
from tkinter import messagebox, ttk
from tratarimagenes.experimentos.rrc2_116_jurkat import *
from tratarimagenes.experimentos.rrc2_102_lavados import *
from tratarimagenes.experimentos.figura_croacia import *
from tratarimagenes.experimentos.capitulo_gsh import *
texto = "voy a crear Figura "
def figura_102():
    etiqueta.config(text="Voy a crear figura RRC2-102 lavados")
    Experimento102()
    etiqueta.config(text="")

def figura_116_jurkat():
    etiqueta.config(text="Voy a crear figura RRC2-116 jurkat")
    experimento116Jurkat()
    etiqueta.config(text="")

def figura_116_el4():
    etiqueta.config(text=texto + "RRC2-116 el4")
    experimento116EL4()
    etiqueta.config(text="")


def figura_croacia():
    etiqueta.config(text="Voy a crear figura croacia")
    experimento_croacia()
    etiqueta.config(text="")

def figura_105():
    etiqueta.config(text="Voy a crear figura RRC2-105")
    experimento105()
    etiqueta.config(text="")
def no_funciona():
    etiqueta.config(text="")
    etiqueta.config(text="No funciona")

n = 0
lista_y = []
y = 50
while n < 8:
    lista_y.append(y)
    y = y + 30
    n = n + 1
button_h = 1
button_w = 17


root = tk.Tk()
root.config(width=300, height=300)
root.title("Creador de figuras")
#columna 1
texto_boton = ["RRC2-116-Jurkat", "RRC2-124-Jurkat", "RRC2-102-Lavados", "RRC2-105", "Croacia",
               "", "RRC2-116-DF", ""]

lista_comandos = [no_funciona] * len(texto_boton)
lista_comandos[0] = figura_116_jurkat
lista_comandos[2] = figura_102
lista_comandos[3] = figura_105
lista_comandos[4] = figura_croacia

n = 0
for texto in texto_boton:
    boton = tk.Button(text=texto, height=button_h, width=button_w, command=lista_comandos[n])
    boton.place(x=20, y=lista_y[n])
    n = n + 1
#columna 2
texto_boton = ["RRC2-116-EL4", "RRC2-124-EL4", "RRC2-42-sin Expander", "RRC2-60", "RRC2-97-MCF-7",
               "", "DF Erica", ""]

lista_comandos = [no_funciona] * len(texto_boton)
lista_comandos[0] = figura_116_el4
n = 0
for texto in texto_boton:
    boton = tk.Button(text=texto, height=button_h, width=button_w, command=lista_comandos[n])
    boton.place(x=170, y=lista_y[n])
    n = n + 1

etiqueta= ttk.Label(text="")
etiqueta.place(x=10, y=0, width=250, height=50)

root.mainloop()