from flask import Flask, render_template, request, redirect
app = Flask(__name__)

class cadESports:
    def __init__(self, nome, jogo, funcao, ranking):
        self.nome = nome
        self.jogo = jogo
        self.funcao = funcao
        self.ranking = ranking

lista = []


@app.route('/atletas')
def atletaseSports():
    return render_template('ESports.html', Titulo ="Atletas eSports: ", ListaAtletas = lista)


@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = "Cadastro de Atletas")


@app.route('/criar', methods= ['POST'])
def criar():
    nome = request.form['nome']
    jogo = request.form['jogo']
    funcao = request.form['funcao']
    ranking = request.form['ranking']
    obj = cadESports(nome, jogo, funcao, ranking)
    lista.append(obj)
    return redirect('/atletas')

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



if __name__ == '__main__':
    app.run()
