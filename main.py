import datetime
import time

import sqlalchemy
from flask import Flask, request, render_template, make_response, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash

from data import db_session
from data.jobs import Jobs
from data.news import News
from data.users import User
from forms.job import AddJob
from forms.user import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
db_session.global_init("db/blogs.db")
db_sess = db_session.create_session()

db_sess.commit()

@login_manager.user_loader
def load_user(user_id):
    return db_sess.query(User).get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/")
def index():
    news = db_sess.query(News).all()
    return render_template("index.html", news=news)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/jobs')
def myjobs():
    jobs = db_sess.query(Jobs).all()
    return render_template("jobs.html", jobs=jobs)

@app.route('/addjob',  methods=['GET', 'POST'])
def addjob():
    form = AddJob()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()
        job.title = form.title.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.is_finished.data
        job.team_leader = form.team_leader.data
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('addjob.html', form=form)



@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User()
        user.surname = form.surname.data
        user.name = form.name.data
        user.email = form.email.data
        user.position = form.position.data
        user.age = form.age.data
        user.address = form.address.data
        user.speciality = form.speciality.data
        user.set_password(form.password.data)
        print(user)

        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
