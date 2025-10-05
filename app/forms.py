from flask import Flask
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_babel import lazy_gettext as _l
from config import *
from forms import *

app = Flask(__name__)
app.config.from_object(Config)
models = app.config['MODELS']

class UploadFileForm(FlaskForm):
    select = SelectField(_l('Select a model'), choices=models, default=1)
    file = FileField(_l('Select a CSV file with the data'))
    submit = SubmitField(_l('Upload'))