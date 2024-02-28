class Pessoa:
    ano = 2024  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def metodo(self):
        print("Hey")

    @classmethod
    def metodo_de_classe(cls):
        print("Hey")

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)


print(Pessoa.ano)

p1 = Pessoa("Joao", 22)
p1.metodo_de_classe()
Pessoa.metodo(p1)
Pessoa.metodo_de_classe()

p2 = Pessoa.criar_com_50_anos("Helena")

print(p2.nome, p2.idade)
