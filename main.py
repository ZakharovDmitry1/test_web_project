import datetime
import time

import sqlalchemy
from flask import Flask, request, render_template, make_response, redirect
from flask_login import LoginManager, login_user
from werkzeug.security import generate_password_hash

from data import db_session
from data.jobs import Jobs
from data.news import News
from data.users import User
from forms.user import RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
# login_manager = LoginManager()
# login_manager.init_app(app)
# db_sess.commit()
#
# @login_manager.user_loader
# def load_user(user_id):
#     db_sess = db_session.create_session()
#     return db_sess.query(User).get(user_id)


# @app.route("/")
# def index():
#     news = db_sess.query(News).all()
#     return render_template("index.html", news=news)

# @app.route('/jobs')
# def myjobs():
#     jobs = db_sess.query(Jobs).all()
#     for i in jobs:
#         print(i)
#     return render_template("jobs.html", jobs=jobs)
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def reqister():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         if form.password.data != form.password_again.data:
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Пароли не совпадают")
#         db_sess = db_session.create_session()
#         if db_sess.query(User).filter(User.email == form.email.data).first():
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Такой пользователь уже есть")
#         user = User()
#         user.surname = form.surname.data
#         user.name = form.surname.name
#         user.email = form.surname.email
#         user.position = form.surname.position
#         user.age = form.surname.age
#         user.address = form.surname.address
#         user.speciality = form.surname.speciality
#         user.set_password(form.password.data)
#
#         db_sess.add(user)
#         db_sess.commit()
#         return redirect('/login')
#     return render_template('register.html', title='Регистрация', form=form)


def main():
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
