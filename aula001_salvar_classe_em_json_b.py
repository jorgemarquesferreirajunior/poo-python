import json
from aula001_salvar_classe_em_json_a import Pessoa, DESTINO, fazer_dump


# Assim a etapa FAZENDO DUMP sera realizada apenas quando a funcao fazer_dump for chamada:
fazer_dump()

with open(DESTINO, "r") as arquivo:
    pessoas = json.load(arquivo)

    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)
