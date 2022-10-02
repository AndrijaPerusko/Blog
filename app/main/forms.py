from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_login import current_user
from app.models import User
from wtforms.validators import DataRequired, Length, ValidationError

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

class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=1, max=120)])
    submit = SubmitField('Submit')
