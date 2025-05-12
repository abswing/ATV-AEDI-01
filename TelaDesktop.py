import tkinter as tk
from tkinter import messagebox
from Categoria import Categoria
from Desktop import Desktop


def TelaDesktop():
    def cadastrar():
        try:
            categoria = Categoria(1, "Desktop")
            d = Desktop(
               marca.get(), modelo.get(), cor.get(), float(preco.get()), categoria, potenciadafonte.get()
            )
            d.cadastrar()
            messagebox.showinfo("Cadastro", d.getInformacoes())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    janela = tk.Toplevel()
    janela.title("Cadastrar Desktop")

    tk.Label(janela, text= "Marca").pack()
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

    tk.Label(janela, text="Potência da Fonte").pack()
    potenciadafonte = tk.Entry(janela)
    potenciadafonte.pack()

    tk.Button(janela, text="Cadastrar", command=cadastrar).pack()