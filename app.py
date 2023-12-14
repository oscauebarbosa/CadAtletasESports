from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'Senai'

class cadESports:
    def __init__(self, nome, jogo, funcao, ranking):
        self.nome = nome
        self.jogo = jogo
        self.funcao = funcao
        self.ranking = ranking

lista = []


@app.route('/atletas')
def atletaseSports():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('ESports.html', Titulo ="Atletas eSports: ", ListaAtletas = lista)


@app.route('/cadastro')
def cadastro():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('Cadastro.html', Titulo = "Cadastro de Atletas")


@app.route('/criar', methods= ['POST'])
def criar():
    if 'salvar' in request.form:
        nome = request.form['nome']
        jogo = request.form['jogo']
        funcao = request.form['funcao']
        ranking = request.form['ranking']
        obj = cadESports(nome, jogo, funcao, ranking)
        lista.append(obj)
        return redirect('/atletas')
    elif 'deslogar' in request.form:
        return redirect('/')



@app.route('/excluir/<nomeatletas>', methods=['GET','DELETE'])
def excluir(nomeatletas) :
    for i, atletas in enumerate(lista):
        if atletas.nome == nomeatletas:
            lista.pop(i)
            break
    return redirect('/atletas')

@app.route('/editar/<nomeatletas>', methods=['GET'])
def editar(nomeatletas):
    for i, atletas in enumerate(lista):
        if atletas.nome == nomeatletas:
            return render_template("Editar.html", atletas=atletas, Titulo="Alterar Atletas")

@app.route('/alterar', methods = ['POST','PUT'])
def alterar():
    nome = request.form['nome']
    for i, atletas in enumerate(lista):
        if atletas.nome == nome:
            atletas.nome = request.form['nome']
            atletas.jogo = request.form['jogo']
            atletas.funcao = request.form['funcao']
            atletas.ranking = request.form['ranking']
    return redirect('/atletas')


@app.route('/')
def login():
    session.clear()
    return render_template('Login.html', Titulo = "Faça seu login")


@app.route('/autenticar', methods = ['POST'])
def autenticar():
    if request.form['usuario'] == 'Caue' and request.form['senha']=='123':
        session['Usuario_Logado'] = request.form['usuario']
        flash('Usuario Logado com Sucesso')
        return redirect('/cadastro')
    else:
        flash('Usuario não encontrado')
        return redirect('/login')




if __name__ == '__main__':
    app.run()
