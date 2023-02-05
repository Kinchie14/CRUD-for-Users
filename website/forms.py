from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, ValidationError
from wtforms.validators import DataRequired, Email



class SignupForm(FlaskForm):
    email = StringField("Input your Email", validators=[DataRequired(), Email()])
    name = StringField("Input your Full Name", validators=[DataRequired()])
    password = PasswordField("Input your Password", validators=[DataRequired()])
    password2 = PasswordField("Confirm your Password", validators = [DataRequired()])
    submit = SubmitField("Sign-Up")



        
class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators= [DataRequired()])
    submit = SubmitField('Login')