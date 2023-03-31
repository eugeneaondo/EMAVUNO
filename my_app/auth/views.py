
from flask import Blueprint,redirect,url_for,render_template
from .forms import RegisterForm
from .models import User
from my_app import db

auth = Blueprint('auth', __name__)


@auth.route('/auth/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user=User(first_name=form.first_name.data, last_name=form.last_name.data,
                  username=form.username.data,phone_number=form.phone_number.data,
                  password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/auth/login')
def login():
    # if form :
    #     return redirect(url_for('index'))
    return render_template('auth/login.html')

        
