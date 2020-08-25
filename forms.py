
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class CommandForm(FlaskForm):
    command = StringField('command')


class LoginForm(FlaskForm):
    nickname = StringField('nickname', [validators.DataRequired()])


class NewCharacter(FlaskForm):
    pdf = FileField('pdf', validators=[
                    FileRequired(), FileAllowed(['pdf'], 'this is not a pdf')])


class newBattle(FlaskForm):
    battle = StringField('battle', [validators.DataRequired("needs name")])
    password = PasswordField(
        'pass', [validators.data_required("needs password")])
