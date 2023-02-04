from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from .models import User


class SignupForm(FlaskForm):
    email = StringField("Input your Email", validators=[DataRequired()])
    name = StringField("Input your Full Name", validators=[DataRequired()])
    age = IntegerField("Input your Age", validators=[DataRequired(), Email()])
    password = PasswordField("Input your Password", validators=[DataRequired(), EqualTo('password2', message = 'Passwords must match')])
    password2 = PasswordField("Confirm your Password", validators = [DataRequired()])
    submit = SubmitField("Sign-Up")


    def check_email(self,field):
        if User.query.filter_by(enmail = field.data).first():
            raise ValidationError('Already has an account')
    
    def check_username(self,field):
        if User.query.filter_by(username = field.data).first():
            raise (ValidationError('Choose another Username'))
        
        
class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired()])
    password = StringField('Password:', validators= [DataRequired()])
    submit = SubmitField('Login')