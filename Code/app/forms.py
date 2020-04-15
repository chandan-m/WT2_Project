from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from app.models import Users
from app import db

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	fname = StringField('First Name', validators=[DataRequired()])
	lname = StringField('Last Name', validators=[DataRequired()])
	phonenumber = StringField('Phone Number', validators=[DataRequired(), Regexp("[0-9]{10}", message="Enter valid Phone Number")])
	address = StringField('Address', validators=[DataRequired()])
	pin = StringField('Pincode', validators=[DataRequired(), Regexp("[0-9]+", message="Enter valid PIN")])
	submit = SubmitField('Register')

	def validate_username(self, username):
		cur = db.connection.cursor()
		query = "SELECT Usersname FROM Users WHERE Usersname = '{}'".format(username.data)
		cur.execute(query)
		user = cur.fetchone()
		if user:
			raise ValidationError('Username already taken.')

	def validate_email(self, email):
		cur = db.connection.cursor()
		query = "SELECT Usersname FROM Customer WHERE E_mail = '{}'".format(email.data)
		cur.execute(query)
		user = cur.fetchone()
		if user:
			raise ValidationError('Account with this email already exists.')

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')
