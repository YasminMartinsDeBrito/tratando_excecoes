from flask import Flask, request

app = Flask(__name__)

@app.post('/')
def soma():
    try:
        valores = request.get_json()
        v1 = valores.get("valor1")
        v2 = valores.get("valor2")
        soma = v1 + v2

        return {'valor1':v1, 'valor2':v2, 'resultado':soma}, 201
    except TypeError:
        return {'msg': f'Algum dado não está de acordo'}, 400

@app.get('/names')
def names(meu_dict):
    try:
        if "nome" in meu_dict:
            print(meu_dict['chave'])
    except KeyError as _:
        ...


        # Erros e exceções: https://docs.python.org/pt-br/3/tutorial/errors.html#syntax-errors

        # lista de exceções ambutidas: https://docs.python.org/pt-br/3/library/exceptions.html#bltin-exceptions