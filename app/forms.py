from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, Length
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from app.models import User
from flask_login import current_user

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()] )
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Please choose another username!')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Please choose another email!')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About Me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=self.username.data).first()
            if user:
                raise ValidationError('Please use a different username!')

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit Request')