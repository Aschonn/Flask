from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, IntegerField, SubmitField, TextAreaField, RadioField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
#what kimd of files do we want to allow to be opened
from flask_wtf.file import FileField, FileAllowed
from flaskdraft.models import UserInfo
from flask_login import current_user

class PlayerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    position = IntegerField('Position')
    college = StringField('college', validators=[Length(min=0, max=50)])
    year_id = SelectField(u'Year', choices=['2020', '2021', '2022', '2023'])
    img = StringField('Img', validators=[Length(min=0, max=200)])
    biography = StringField('Biography', validators=[Length(min=0, max=200)])
    submit = SubmitField('Submit')

class SearchPlayer(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    position = SelectField('Positions:', choices=['SG', 'PG', 'SM', 'C', 'PF'])
    mock = SelectField('Mock Drafts Years:', choices=[])
    submit = SubmitField('Submit')