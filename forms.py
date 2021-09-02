from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = TextField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль (от 8 до 12 символов)', validators=[DataRequired(), Length(min=8, max=12)])
    remember = BooleanField('Запомнить меня', default=False)
    submit_btn = SubmitField('Войти')
