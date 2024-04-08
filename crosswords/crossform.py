from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired

class PuzzForm(FlaskForm):
    puzz = FileField(validators=[FileRequired()])
    submit = SubmitField("uplaod File")