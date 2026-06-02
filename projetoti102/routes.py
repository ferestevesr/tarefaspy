from projetoti102 import app
from flask import render_template, url_for
@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')
