from flask import Flask, jsonify, request
from control.TrianguloController import TrianguloController

app = Flask("API Triangulo")

# Função auxiliar para lidar com validações
def handle_validation_error(e):
    return jsonify({"erro": str(e)}), 400

# Endpoint POST: /triangulo/tipo
@app.route('/triangulo/tipo', methods=['POST'])
def verificar_tipo_triangulo():
    try:
        # Recebe os dados dos lados via JSON
        data = request.get_json()
        lado1 = data.get('lado1')
        lado2 = data.get('lado2')
        lado3 = data.get('lado3')

        # Validação de entrada
        if None in [lado1, lado2, lado3]:
            raise ValueError("Todos os lados (lado1, lado2, lado3) são obrigatórios.")

        # Cria o controlador e verifica o tipo do triângulo
        trianguloController = TrianguloController()
        trianguloController.criar_triangulo(lado1, lado2, lado3)

        tipo_triangulo = trianguloController.verificar_tipo_triangulo()

        # Retorna o tipo de triângulo
        jsonResposta = {
            "lado1": lado1,
            "lado2": lado2,
            "lado3": lado3,
            "tipo": tipo_triangulo
        }
        return jsonify(jsonResposta), 200

    except ValueError as e:
        return handle_validation_error(e)

# Inicia o servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
