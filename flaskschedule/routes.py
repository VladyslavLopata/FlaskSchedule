import datetime

from flask import render_template, url_for, flash, redirect

from flaskschedule import app, db
from flaskschedule.forms import RegistrationForm, LoginForm
from flaskschedule.models import Lesson, Data


def current_week():
    return (datetime.datetime.now()).isocalendar()[1] % 2 + 1


@app.route('/')
def week_selector():
    return week(current_week())


@app.route('/next_week/')
def next_week():
    return week(3 - current_week())


def week(week_number):
    return render_template('schedule.html',
                           days=db.session
                           .query(Lesson.day)
                           .distinct()
                           .filter_by(week=week_number),

                           lessons=db.session.query(Lesson)
                           .filter_by(week=week_number)
                           .join(Data, Data.id == Lesson.data_id))


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Зареєстровано користувача {form.username.data}.', 'success')
        return redirect(url_for('week_selector'))
    return render_template('register.html', form=form)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Авторизовано користувача {form.email.data}.', 'success')
        return redirect(url_for('week_selector'))
    return render_template('login.html', form=form)
