# O uso de @staticmethod apenas garante que a funcao pertece a classe, mas nao serve para mais nada
class Pessoa:
    @staticmethod
    def print_oi():
        print("Oi")


p1 = Pessoa()
p1.print_oi()

Pessoa.print_oi()
