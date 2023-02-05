from flask import Blueprint, flash, render_template
from flask_login import current_user, login_required
from .models import User

views= Blueprint('views', __name__)

@views.route('/', methods =['GET', 'POST'])
@login_required
def home():
    
    user = User.query.all()
    return render_template('home.html',user=user)

