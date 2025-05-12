import tkinter as tk
from tkinter import messagebox
from Categoria import Categoria
from Notebook import Notebook

def TelaNotebook():
    def cadastrar():
        try:
            categoria = Categoria(2, "Notebook")
            n = Notebook(
              marca.get(), modelo.get(), cor.get(), float(preco.get()), categoria, int(tempodebateria.get())
            )
            n.cadastrar()
            messagebox.showinfo("Cadastro", n.getInformacoes())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    janela = tk.Toplevel()
    janela.title("Cadastrar Notebook")

    tk.Label(janela, text="Marca").pack()
    marca = tk.Entry(janela)
    marca.pack()

    tk.Label(janela, text="Modelo").pack()
    modelo = tk.Entry(janela)
    modelo.pack()

    tk.Label(janela, text="Cor").pack()
    cor = tk.Entry(janela)
    cor.pack()

    tk.Label(janela, text="Preço").pack()
    preco = tk.Entry(janela)
    preco.pack()

    tk.Label(janela, text="Tempo de Bateria").pack()
    tempodebateria = tk.Entry(janela)
    tempodebateria.pack()

    tk.Button(janela, text="Cadastrar", command=cadastrar).pack()