from app import app
from flask import render_template,redirect,url_for,flash
from app.forms import RegistrationForm,LoginForm



@app.route('/')
@app.route('/home')
def main():


    return render_template('index.html',posts = posts)

@app.route('/register',methods =["POST","GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Welcome {form.username.data} your Acoount has been created','success')
        return redirect(url_for('main'))
    return render_template('register.html',title = 'Register',form=form)

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Welcome {form.username.data} you  have succesfully logged into your account','success')
        return redirect(url_for('main'))
    return render_template('login.html',title = 'Login',form=form)