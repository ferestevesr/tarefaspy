from gunicorn.systemd import sd_notify

from projetoti102 import app, bcrypt, database
from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from projetoti102.forms import FormLogin, FormCriarConta
from projetoti102.models import Usuario





@app.route('/', methods=['GET', 'POST'])
def home():
    formlogin = FormLogin()

    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()


        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario, remember=True)
            return redirect(url_for('perfil', usuario=usuario.username))

    return render_template('homepage.html', form=formlogin)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    formcriarconta = FormCriarConta()


    if formcriarconta.validate_on_submit():
        password = bcrypt.generate_password_hash(formcriarconta.senha.data).decode('utf-8')
        usuario = Usuario(username=formcriarconta.username.data,
                          email=formcriarconta.email.data,
                          password=password)

        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', usuario=usuario.username))



    return render_template('criarConta.html', form=formcriarconta)

@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    formCriarConta = FormCriarConta()
    return render_template('perfil.html', usuario=usuario)


