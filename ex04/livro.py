from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int,
                 titulo_capitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__numero_capitulo = numero_capitulo
        self.__titulo_capitulo = titulo_capitulo
        self.__autores = [autor]
        self.__capitulos = []

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

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

    @property
    def autores(self):
        return self.__autores

    @autores.setter
    def autores(self, autores):
        self.__autores = autores

    @property
    def capitulos(self):
        return self.__capitulos

    @capitulos.setter
    def capitulos(self, capitulos):
        self.__capitulos = capitulos

    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and (autor not in self.__autores) and (autor is not None):
            self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if autor in self.__autores:
            self.__autores.remove(autor)

    def incluir_capitulo(self, numero_capitulo: int, titulo_capitulo: str):
        if isinstance(numero_capitulo, int) and (titulo_capitulo, str):
            for objeto in self.__capitulos:
                if (titulo_capitulo not in self.__capitulos) and (numero_capitulo not in self.__capitulos) and (
                        capitulo is not None):
                    capitulo = Capitulo(titulo_capitulo, numero_capitulo)
                    self.__capitulos.append(capitulo)

    def excluir_capitulo(self, titulo_capitulo: str):
        for objeto in self.__capitulos:
            if titulo_capitulo in self.__capitulos:
                self.__capitulos.remove(objeto)

    def find_capitulo_by_titulo(self, titulo_capitulo: str):
        for objeto in self.__capitulos:
            if titulo_capitulo in objeto:
                return objeto