from flask_wtf import Form
from wtforms.fields import TextAreaField, TextField, SubmitField
from wtforms.validators import Required

class UploadForm(Form):
    content = TextAreaField(u'Your content', validators=[Required()])
    accesskey = TextField(u'The key to access your data', validators=[Required()])
    submit = SubmitField(u'submit')