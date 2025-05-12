import tkinter as tk
from TelaNotebook import TelaNotebook
from TelaDesktop import TelaDesktop

def main():
    janela = tk.Tk()
    janela.title("Sistema de Cadastro de Produtos")

    tk.Button(janela, text="Cadastrar Notebook", command=TelaNotebook).pack(pady=10)
    tk.Button(janela, text="Cadastrar Desktop", command=TelaDesktop).pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    main()



































# from Categoria import Categoria
# from Desktop import Desktop
# from Notebook import Notebook

# def main():
    
#     print("\n==============================")

#     # Criando um Desktop
#     desktop = Desktop(
#         marca="Dell",
#         modelo="Dell Inspiron",
#         cor="Preto",
#         preco=3500.00,
#         categoria= "Desktop",
#         potencia_da_fonte=500
#     )
#     desktop.cadastrar()
#     print("Informações do Desktop:")
#     print(desktop.getInformacoes())


#     print("\n==============================")

#     # Criando um Notebook
#     notebook = Notebook(
#         marca="Acer",
#         modelo="Acer Aspire",
#         cor="Prata",
#         preco=4500.00,
#         categoria= "Notebook",
#         tempo_de_bateria=8
#     )
#     notebook.cadastrar()
#     print("\nInformações do Notebook:")
#     print(notebook.getInformacoes())

# if __name__ == "__main__":
#     main()
