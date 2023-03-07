# -------- IMPORTS ---------
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField,StringField
from wtforms.validators import DataRequired, EqualTo
from app.models import User

# ------ Pokedex Form ------
class PokemonForm(FlaskForm):
    pokemon_name = StringField('Pokemon Name', validators=[DataRequired()])
    submit_btn = SubmitField('Submit')


# ------ Registration Form ------
class RegistrationForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name: ', validators=[DataRequired()])
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password:', validators=[DataRequired(), EqualTo('password')])
    submit_btn = SubmitField('Sign Up')


# ------ Login Form -----
class LoginForm(FlaskForm):
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit_btn = SubmitField('Login')


# --------- Edit Profile --------
class EditProfileForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name: ', validators=[DataRequired()])
    email = EmailField('Email: ', validators=[DataRequired()])
    submit_btn = SubmitField('Update')


# ------ Pokemon Team From -------
# class PokemonRegionForm(FlaskForm):


# ------ Pokemon Team From -------
class PokemonTeamForm(FlaskForm):
    team = StringField('')