from elevador import Elevador
from comandoInvalidoException import ComandoInvalidoException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException

class ControladorElevador:
    def __init__(self):
        self.__elevador = None

    def subir(self):
        return Elevador.subir(self.__elevador)

    def descer(self):
        return Elevador.descer(self.__elevador)

    def entraPessoa(self):
        return Elevador.entraPessoa(self.__elevador)

    def saiPessoa(self):
        return Elevador.saiPessoa(self.__elevador)

    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        if type(andarAtual) is not int or type(totalAndaresPredio) is not int or type(capacidade) is not int or type(totalPessoas) is not int:
            raise ComandoInvalidoException
        if andarAtual < 0 or totalAndaresPredio < 0 or capacidade < 0 or totalPessoas < 0:
            raise ComandoInvalidoException
        elif andarAtual < 0 or totalAndaresPredio - 1 < 0 or totalPessoas > capacidade or andarAtual > totalAndaresPredio - 1:
            raise ComandoInvalidoException
        else:
            self.__elevador = Elevador(capacidade, totalPessoas, totalAndaresPredio, andarAtual)

    @property
    def elevador(self):
        return self.__elevador