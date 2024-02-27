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


def fazer_dump():
    with open(DESTINO, "w") as arquivo:
        print("FAZENDO DUMP")
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


# Fazer isso garante que a funcao fazer_dump sera chamada apenas quando o script da funcao for executado
# Caso esse script seja importado para outro, a funcao fazer_dump nao sera chamada automaticamente
if __name__ == "__main__":
    print("Executando o script ex_salvar_classe_em_json_a.py")
    fazer_dump()
