class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print("APAGANDO", self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print("APAGANDO", self.rua, self.numero)


c1 = Cliente("Maria")
c1.inserir_endereco("Av. Brasil", 54)
c1.inserir_endereco("Rua B.", 6745)
endereco_externo = Endereco("Av. Felicidade", 578)
c1.inserir_endereco_externo(endereco_externo)

c1.listar_endereco()

del c1

print("FIM")
