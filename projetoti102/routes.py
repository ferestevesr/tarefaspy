from flask_login import login_required

from projetoti102 import app
from flask import render_template, url_for


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)


