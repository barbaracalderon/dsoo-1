from mamifero import Mamifero

class Cachorro(Mamifero):
    def __init__(self):
        super().__init__(tamanho_passo=3, volume_som=3)

    def latir(self):
        return super().produzir_som() + " SOM: AU"