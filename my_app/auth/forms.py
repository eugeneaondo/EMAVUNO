from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import Length,DataRequired,Email,EqualTo
from .models import User
from wtforms import ValidationError


class RegisterForm(FlaskForm):
    first_name = StringField('FirstName',validators=[DataRequired(), Length(1,30) ] )
    last_name = StringField('Last Name',validators=[DataRequired(), Length(1,30) ] )
    username = StringField('UserName',validators=[DataRequired(), Length(1,30) ] )
    email = StringField('Email', validators=[DataRequired(),Email() ])
    phone_number = StringField('Phone Number', validators =[DataRequired(),Length(10,14) ])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='password MUST be the same') ] )
    password2 = PasswordField('Confirm Password' , validators=[DataRequired() ])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email has already been registered')
        
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already taken')
