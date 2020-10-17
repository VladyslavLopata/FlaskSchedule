from flaskschedule import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    group = db.Column(db.String(20))


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
