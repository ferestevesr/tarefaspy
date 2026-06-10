from projetoti102 import app
from flask import render_template, url_for
from flask_login import login_required
from projetoti102.forms import FormLogin, FormCriarConta


@app.route('/', methods=['GET', 'POST'])
def home():
    formlogin=FormLogin()
    return render_template('homepage.html', form=formlogin)

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    formCriarConta = FormCriarConta()
    return render_template('criarConta.html', form=formCriarConta)

@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    formCriarConta = FormCriarConta()
    return render_template('perfil.html', usuario=usuario)


