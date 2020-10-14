import datetime

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedule.db'

db = SQLAlchemy(app)


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer, nullable=False)
    day = db.Column(db.String, nullable=False)
    time = db.Column(db.Time, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    data_id = db.Column(db.Integer, db.ForeignKey('data.id'), nullable=False)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lessons = db.relationship('Lesson', backref='data', lazy=True)
    name = db.Column(db.String(120), nullable=False)
    link = db.Column(db.String(150))
    classroom = db.Column(db.String(40))
    teacher = db.Column(db.String(150), nullable=False)


def current_week():
    return (datetime.datetime.now()).isocalendar()[1] % 2 + 1


@app.route('/')
def week1():
    week_number = current_week()
    return render_template('index.html',
                           days=db.session
                           .query(Lesson.day)
                           .distinct()
                           .filter_by(week=week_number),

                           lessons=db.session.query(Lesson)
                           .filter_by(week=week_number)
                           .join(Data, Data.id == Lesson.data_id))


if __name__ == '__main__':
    app.run()
