from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.fields.core import BooleanField, IntegerField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.fields.html5 import EmailField

#register and login form for individuals
class Register_Indi(FlaskForm):
    fname=StringField('First Name:',validators=[DataRequired()])
    lname=StringField('Last Name:',validators=[DataRequired()])
    email=EmailField('Email:',validators=[DataRequired()])
    aadhar=StringField('Aadhar Number:',validators=[DataRequired()])
    password=PasswordField('Password:',validators=[DataRequired(),Length(min=8)])
    confirm_pass=PasswordField('Confirm Password:',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

class Login_Indi(FlaskForm):
    email=EmailField('Email:',validators=[DataRequired()])
    password=PasswordField('Password:',validators=[DataRequired(),Length(min=8)])
    aadhar=StringField('Aadhar Number:',validators=[DataRequired()])
    rememberme=BooleanField('Remember Me:')
    submit=SubmitField('Log In')

#register and login form for organisation
class Register_org(FlaskForm):
    orgname=StringField('Organisation Name:',validators=[DataRequired()])
    hod=StringField('Head of Organisation:',validators=[DataRequired()])
    address=TextAreaField('Address of the Organisation:',validators=[DataRequired()])
    branch=StringField('Branch Location Area:',validators=[DataRequired()])
    contact=StringField('Contact number:',validators=[DataRequired()])
    official_email=EmailField('Official Email:',validators=[DataRequired()])
    passw=PasswordField('Password:',validators=[DataRequired(),Length(min=8)])
    cpassw=PasswordField('Confirm Password:',validators=[DataRequired(),EqualTo('passw')])
    submit=SubmitField('Signup')

class Login_org(FlaskForm):
    email=EmailField('Official Email:',validators=[DataRequired()])
    contact=StringField('Contact:',validators=[DataRequired()])
    passw=PasswordField('Password:',validators=[DataRequired()])
    submit=SubmitField('Log In')

class Message_Send(FlaskForm):
    no_of_bodies = IntegerField('Approximate number of bodies:',validators=[DataRequired()])
    street_name = StringField('Street Name:',validators=[DataRequired()])
    area = StringField('Area:',validators=[DataRequired()])
    landmark = StringField('Landmark:',validators=[DataRequired()])
    city = StringField('City:',validators=[DataRequired()])
    pincode = StringField('Pincode:',validators=[DataRequired()])
    submit=SubmitField('SUBMIT')

class File_upload(FlaskForm):
    Name=StringField('User Name:',validators=[DataRequired()])
    email=EmailField('Email:',validators=[DataRequired()])
    filetoupload = FileField('Upload a file of your choice:',validators=[DataRequired()])
    submit = SubmitField('UPLOAD')
