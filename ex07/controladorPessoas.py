from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico

class ControladorPessoas(AbstractControladorPessoas):
  def __init__(self):
    super().__init__()
    self.__clientes = []
    self.__tecnicos = []

  @property
  def clientes(self) -> list:
    return self.__clientes

  @property
  def tecnicos(self) -> list:
    return self.__tecnicos

  def inclui_cliente(self, codigo :int, nome :str) -> Cliente:
    cliente = Cliente(nome, codigo)
    contador = 0
    for i in range(len(self.__clientes)):
      if self.__clientes[i].codigo == codigo:
          contador = contador + 1
    if contador == 0:
        self.__clientes.append(cliente)
    return cliente
    
  def inclui_tecnico(self, codigo :int, nome :str) -> Tecnico:
    tecnico = Tecnico(nome, codigo)
    contador = 0
    for i in range(len(self.__tecnicos)):
      if self.__tecnicos[i].codigo == codigo:
          contador = contador + 1
    if contador == 0:
        self.__tecnicos.append(tecnico)
    return tecnico