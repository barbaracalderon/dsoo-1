from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException

class Elevador:
    def __init__(self, capacidade: int, totalPessoas: int, totalAndaresPredio: int, andarAtual: int):
        if isinstance(capacidade, int):
            self.__capacidade = capacidade
        if isinstance(totalPessoas, int):
            self.__totalPessoas = totalPessoas
        if isinstance(totalAndaresPredio, int):
            self.__totalAndaresPredio = totalAndaresPredio
        if isinstance(andarAtual, int):
            self.__andarAtual = andarAtual
    
    def subir(self):
        if self.__andarAtual >= self.__totalAndaresPredio - 1:
            raise ElevadorJahNoUltimoAndarException
        else:
            self.__andarAtual += 1
        return self.__andarAtual
        
    def descer(self):
        if self.__andarAtual <= 0:
            raise ElevadorJahNoTerreoException
        else:
            self.__andarAtual -= 1
        return self.__andarAtual
        
    def entraPessoa(self):
        if self.__capacidade == self.__totalPessoas:
            raise ElevadorCheioException
        else:
            self.__totalPessoas += 1
        return self.__totalPessoas
    
    def saiPessoa(self):
        if self.__totalPessoas <= 0:
            raise ElevadorJahVazioException
        else:
            self.__totalPessoas -= 1
        return self.__totalPessoas
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @property
    def totalPessoas(self):
        return self.__totalPessoas
    
    @property
    def totalAndaresPredio(self):
        return self.__totalAndaresPredio
    
    @property
    def andarAtual(self):
        return self.__andarAtual
    
    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int):
        self.__totalAndaresPredio = totalAndaresPredio