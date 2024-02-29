class Pen:
    def __init__(self, cor):
        self.cor = cor
        self._cor_tampa = None
        
    # retornando o valor de um atributo
    def get_cor(self):
        print("ESTOU NO GETTER")
        return self._cor
    
    # usando getter, um metodo se comportando como um atributo
    @property
    def cor(self):
        print("ESTOU NO GETTER")
        return self._cor
    
    
    @cor.setter
    def cor(self, valor):
        print("ESTOU NO SETTER")
        self._cor = valor
    
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor
    
caneta = Pen('Azul')

caneta.cor = "Rosa"
print(caneta.cor)

caneta.cor_tampa = "Azul"
print(caneta.cor_tampa)