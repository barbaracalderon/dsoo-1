from mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self):
        super().__init__(tamanho_passo = 2, volume_som = 2)

    def miar(self):
        return super().produzir_som()+" SOM: MIAU"