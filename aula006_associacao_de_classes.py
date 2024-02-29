class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None
        
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
    
    
class Ferramenta:
    def __init__(self, nome) -> None:
        self.nome = nome
        
    def escrever(self):
        return f'{self.nome} está escrevendo'
    
escritor = Escritor('Carlos')

caneta = Ferramenta('Caneta Bic')
lapis = Ferramenta('Lapis 2B')

escritor.ferramenta = caneta

print(escritor.ferramenta.escrever())
print(lapis.escrever())
