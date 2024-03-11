class A:
    atributo_a = "valor a"

    def __init__(self, valor):
        self.valor = valor

    def metodo(self):
        print("A")


class B(A):
    atributo_b = "valor b"

    def __init__(self, valor, outra_coisa):
        super().__init__(valor)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print("B")


class C(B):
    atributo_c = "valor c"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def metodo(self):
        super().metodo()
        print("C")


c = C("valor", "outra coisa")
print("")

print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
print(c.valor)
print(c.outra_coisa)

c.metodo()
