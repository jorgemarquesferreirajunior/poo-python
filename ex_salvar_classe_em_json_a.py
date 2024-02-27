import json

DESTINO = "classe-aula127.json"


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("Joao", 23)
p2 = Pessoa("Ana", 27)
p3 = Pessoa("Helena", 13)


bd = [vars(p1), vars(p2), vars(p3)]

# Desse modo quando importarmos esse script para outro, a etapa FAZENDO DUMP sera realizada automaticamente
with open(DESTINO, "w") as arquivo:
    print("FAZENDO DUMP")
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
