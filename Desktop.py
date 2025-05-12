from Produto import Produto

class Desktop(Produto):
    def __init__(self,marca = None, modelo=None, cor=None, preco=0.0, categoria=None, potenciadafonte=0):
        super().__init__(marca, modelo, cor, preco, categoria)
        self._potenciadafonte = potenciadafonte  # Atributo fracamente privado

    @property
    def potencia_da_fonte(self):
        return self._potenciadafonte

    @potencia_da_fonte.setter
    def potencia_da_fonte(self, potenciadafonte):
        self._potenciadafonte = potenciadafonte

    def getInformacoes(self):
        return (
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Cor: {self.cor}\n"
            f"Preço: {self.preco}\n"
            f"Categoria: {self.categoria}\n"
            f"Potência da Fonte: {self._potenciadafonte}W"
        )

    def cadastrar(self):
        print("Cadastro de Desktop feito com sucesso!")
    