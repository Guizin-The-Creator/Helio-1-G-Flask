class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3

    @property
    def lado1(self):
        return self._lado1

    @lado1.setter
    def lado1(self, value):
        if value <= 0:
            raise ValueError("O lado deve ser maior que zero.")
        self._lado1 = value

    @property
    def lado2(self):
        return self._lado2

    @lado2.setter
    def lado2(self, value):
        if value <= 0:
            raise ValueError("O lado deve ser maior que zero.")
        self._lado2 = value

    @property
    def lado3(self):
        return self._lado3

    @lado3.setter
    def lado3(self, value):
        if value <= 0:
            raise ValueError("O lado deve ser maior que zero.")
        self._lado3 = value

    # Método para verificar o tipo de triângulo
    def verificar_tipo(self):
        if self._lado1 == self._lado2 == self._lado3:
            return "Equilátero"
        elif self._lado1 == self._lado2 or self._lado2 == self._lado3 or self._lado1 == self._lado3:
            return "Isósceles"
        else:
            return "Escaleno"
