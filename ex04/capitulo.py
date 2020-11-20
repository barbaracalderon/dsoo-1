class Capitulo:
    def __init__(self, numero_capitulo: int, titulo_capitulo: str):
        self.__numero_capitulo = numero_capitulo
        self.__titulo_capitulo = titulo_capitulo

    @property
    def numero_capitulo(self):
        return self.__numero_capitulo

    @numero_capitulo.setter
    def numero_capitulo(self, numero_capitulo):
        self.__numero_capitulo = numero_capitulo

    @property
    def titulo_capitulo(self):
        return self.__titulo_capitulo

    @titulo_capitulo.setter
    def titulo_capitulo(self, titulo_capitulo):
        self.__titulo_capitulo = titulo_capitulo