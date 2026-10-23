from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = "chave_secreta_projeto"

user = {
    "nome": "lttl",
    "cpf": "11122233344",
    "senha": "123456"
}

def login_required(func):
    @wraps(func)
    def verificar_login(*args, **kwargs):
        if "logado" not in session:
            return redirect(url_for("login"))

        return func(*args, **kwargs)

    return verificar_login


@app.route('/api', methods=['GET'])
def teste_api():
    return jsonify({"message": "Projeto revisão SAEP"}), 200


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cpf = request.form['cpf']
        senha = request.form['senha']
        nome = request.form['nome']

        if cpf == user['cpf'] and senha == user['senha'] and nome == user['nome']:
            session['logado'] = True
            return render_template('index.html')

        else:
            return render_template(
                'login.html',
                erro="Nome, CPF ou senha incorretos!"
            )

    return render_template("login.html")


@app.route('/index', methods=['GET'])
@login_required
def index():
    return jsonify({
        "message": "Futura tela principal do projeto"
    }), 200


if __name__ == '__main__':
    app.run(debug=True)