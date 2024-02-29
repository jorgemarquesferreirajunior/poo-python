#  por convencao, atributos e metodos do tipo protect (com underline no inicio do nome) nao devem ser acessados fora da classe e sub classes

# por convencao tambem, atributos e metodos do tipo private (com dois underlines no inicio do nome) devem ser usados apenas na classe pai

class Foo:
    def __init__(self) -> None:
        self.atributo_publico = 'atributo publico'
        self._atributo_protegido = 'atributo protegido'
        self.__atributo_privado = 'atributo privado'
        
    def metodo_publico(self):
        print('metodo publico')
        
    def _metodo_protegido(self):
        print('metodo protegido')
        
    def __metodo_privado(self):
        print('metodo privado')
        
f = Foo()
print(f.atributo_publico)
f.metodo_publico()

print(f._metodo_protegido())
