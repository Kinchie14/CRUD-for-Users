from flask import Blueprint, flash, render_template, redirect, request, url_for, abort
from flask_login import current_user, login_required
from .models import User
from website import db
from website.forms import UpdateUserInfo

views= Blueprint('views', __name__)

@views.route('/', methods =['GET', 'POST'])
@login_required
def home():
    
    #Querying all the users.
    user = User.query.all()
    cur_user = current_user
    return render_template('home.html',user=user, cur_user= cur_user)

@views.route('/<int:user_id>', methods = ['GET', 'POST'])
@login_required
def view_information(user_id):
    user_info = User.query.get_or_404(user_id)
    cur_user= current_user


    return render_template('view_information.html', id =user_info.id, 
                                                    name = user_info.name,
                                                    email = user_info.email,
                                                    info = user_info, cur_user= cur_user)



@views.route('/<int:user_id>/update', methods = ['GET', 'POST'])
@login_required
def update_information(user_id):
    
    user_info = User.query.get_or_404(user_id)
    if user_info.id != current_user.id:
        abort(403)

    form = UpdateUserInfo()

    if form.validate_on_submit():
        user_info.name = form.name.data
        user_info.email = form.email.data
        db.session.commit()
        flash('User information has been updated')
        return redirect(url_for('views.view_information', user_id = user_info.id))
    elif request.method == 'GET':

        form.name.data = user_info.name
        form.email.data = user_info.email
        cur_user= current_user
    
    return render_template('update_info.html', form=form, cur_user= cur_user)


@views.route('/<int:user_id>/delete', methods = ['POST'])
@login_required
def delete_information(user_id):
    user_info = User.query.get_or_404(user_id)
    if user_info.id != current_user.id:
        abort(403)
    else:
        db.session.delete(user_info)
        db.session.commit()
        flash('User Information has been deleted')
        return redirect(url_for('views.home'))
