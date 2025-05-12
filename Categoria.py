class Categoria:
    def __init__(self, id = None, nome = None):
        self.nome = nome   
        self.id = id   
    def __str__(self):
        return f"ID: {self.id} Nome:  {self.nome}"