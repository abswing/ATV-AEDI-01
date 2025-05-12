from Produto import Produto

class Notebook(Produto):
    def __init__(self, marca = None, modelo=None, cor=None, preco=0.0, categoria=None, tempodebateria=0):
        super().__init__(marca, modelo, cor, preco, categoria,)
        self.__tempodebateria = tempodebateria  # Atributo fortemente privado

    @property
    def tempo_de_bateria(self):
        return self.__tempodebateria

    @tempo_de_bateria.setter
    def tempo_de_bateria(self, tempodebateria):
        self.__tempodebateria = tempodebateria

    def getInformacoes(self):
        return (
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Cor: {self.cor}\n"
            f"Preço: {self.preco}\n"
            f"Categoria: {self.categoria}\n"
            f"Tempo de Bateria: {self.__tempodebateria} horas"
        )

    def cadastrar(self):
        print("Cadastro de Notebook feito com sucesso!")