from app import app
from flask import render_template,redirect,url_for,flash,request
from app.forms import RegistrationForm,LoginForm
from app.model import User,Post
from app import app,db,bcrypt
from . import db
from flask_login import login_required,login_user,current_user,logout_user
from flask import session
import secrets
from flask_bcrypt import Bcrypt

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

@app.route('/')
@app.route('/home')
def main():


    return render_template('index.html')

@app.route('/register',methods =["POST","GET"])
def register():
    if current_user.is_authenticated:
        flash(f'Already registered','danger')
        return redirect(url_for('main'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username = username,email=email,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.username.data} your Acoount has been created','success')
        return redirect(url_for('login'))
    return render_template('register.html',title = 'Register',form=form)

@app.route('/login',methods =["POST","GET"])
def login():
    if current_user.is_authenticated:
        flash(f'Already logged in','danger')
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        
        if user  and  bcrypt.check_password_hash(user.password,form.password.data):
             login_user(user,remember =form.remember.data)
             flash(f'Welcome  you  have succesfully logged into your account','success')
             return redirect(request.args.get('next') or url_for('main'))
             return redirect(url_for('main'))
        else:
             flash(f'Login unsucessful verify the email and password entered are correct','danger')

    return render_template('login.html',title = 'Login',form=form)


@app.route('/logout')

def logout():
    logout_user()
    return redirect(url_for('main'))

@login_required
@app.route('/profile')


def profile():

     image_file = url_for('static',filename = 'img/'+ current_user.image_file)
     return render_template('profile.html',image_file=image_file)