from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, IntegerField, SubmitField, TextAreaField, RadioField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
#what kimd of files do we want to allow to be opened
from flask_wtf.file import FileField, FileAllowed
from flaskdraft.models import UserInfo
from flask_login import current_user


class SelectMockYear(FlaskForm):
    mock = SelectField(u'Mock Drafts Years:', choices=[])
    submit = SubmitField('Submit')
