from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Логін',
                           validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Підтвердіть пароль',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зареєструватись')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль',
                             validators=[DataRequired()])
    remember = BooleanField("Запам'ятати")
    submit = SubmitField('Увійти')
