from flask import render_template, flash, redirect
from flask.helpers import url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author':{'username':'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author':{'username':'Susan'},
            'body': 'The avenger movie was no so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'.format( form.username.data, form.remember_me.data ))
        return redirect(url_for('/index'))
    return render_template('login.html', title='Sign In', form=form)
