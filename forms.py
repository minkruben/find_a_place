from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(Form):

    first_name = StringField('First name', validators=[DataRequired("Please enter your first name")])
    last_name = StringField('Last name',  validators=[DataRequired("Please enter your last name")])
    email = StringField('Email',  validators=[DataRequired("Please enter your Email"), Email("Please enter a valid email")])
    password = PasswordField('Password',  validators=[DataRequired("Please enter your password"), Length(min=6, message="Passwords must be 6 character")])
    submit = SubmitField('sign up')


class SigninForm(Form):

    email = StringField('Email', validators=[DataRequired('Please Enter your Email address'), Email("Please enter a valid email")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password")])
    submit = SubmitField("Sign in")