from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, validators, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=64)])


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        validators.DataRequired(message='Username is required.'),
        validators.Length(min=3, max=20, message='Username must be between 3 and 20 characters.'),
        validators.Regexp(r'^[\w.]+$', message='Username can only contain letters, numbers, and underscores.')
    ])
    email = EmailField('Email', validators=[DataRequired(), Length(min=3, max=255)])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 Length(min=8, max=64),
                                 EqualTo('confirm_password', message='Passwords must match')
                             ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8)])


class AddNoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=255)])
    content = TextAreaField('Content', validators=[DataRequired(), Length(min=1, max=10000)])


class EditNoteForm(FlaskForm):
    edit_title = StringField('Title', validators=[DataRequired(), Length(min=1, max=255)])
    edit_content = TextAreaField('Content', validators=[DataRequired(), Length(min=1, max=10000)])
