# 1 - Crie uma classe Carro
# 2 - Crie uma classe Motor
# 3 - Crie uma classe Fabricante
# 4 - Faca uma ligacao entre Carro e Motor
# Obs: Um Motor pode ser de varios Carros
# 5 -Faca uma ligacao entre Carro e Fabricante
# Obs: Um Fabricante pode fazer varios Carros
# 6 - Exiba o nome do Carro, Motor e Fabricante na tela...


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


# fabricantes
volkswagem = Fabricante("VolksWagem")
chevrolet = Fabricante("Chevrolet")
ford = Fabricante("Ford")
fiat = Fabricante("Fiat")

# motores
motor_refrigerado_1600 = Motor("Refrigerado a Ar 1600")
motor_1_0 = Motor("1.0")
motor_2_0 = Motor("2.0")

# carros    
fusca = Carro("Fusca")
fusca.fabricante = volkswagem
fusca.motor = motor_refrigerado_1600
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

uno = Carro("Uno")
uno.fabricante = fiat
uno.motor = motor_1_0
print(uno.nome, uno.fabricante.nome, uno.motor.nome)

focus = Carro("Focus Titanium ")
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)
