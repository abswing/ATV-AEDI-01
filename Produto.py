from abc import ABC, abstractmethod


class Produto(ABC):
    def __init__(self, marca=None, modelo=None, cor = None, preco=0.0, categoria=None): 
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "cor": self.cor,
            "preco": self.preco,
            "categoria": self.categoria
        }

    @abstractmethod
    def cadastrar(self):
        pass
# esse abstractmethod é uma função que não tem implementação na classe pai, 
# mas deve ser implementada nas classes filhas.
