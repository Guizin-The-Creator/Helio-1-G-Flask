from model.Triangulo import Triangulo

class TrianguloController:
    def __init__(self):
        self._triangulo = None

    def criar_triangulo(self, lado1, lado2, lado3):
        self._triangulo = Triangulo(lado1, lado2, lado3)

    def verificar_tipo_triangulo(self):
        if self._triangulo is None:
            raise ValueError("O triângulo não foi criado ainda.")
        return self._triangulo.verificar_tipo()

    # Getters e Setters
    @property
    def triangulo(self):
        return self._triangulo

    @triangulo.setter
    def triangulo(self, valor):
        self._triangulo = valor
