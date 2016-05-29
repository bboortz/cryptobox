from flask_wtf import Form
from wtforms.fields import TextAreaField, TextField, SubmitField, HiddenField
from wtforms.validators import Required

class UploadForm(Form):
    content = TextAreaField(u'Your content', validators=[Required()])
    accesskey = TextField(u'The key to access your data', validators=[Required()])
    cryptpass = TextField(u'The key to encrypt your data', validators=[Required()])
    submit = SubmitField(u'submit')
    
    
class AccessForm(Form):
    id = TextField(u'The id', validators=[Required()])
    accesskey = TextField(u'The key to access your data', validators=[Required()])
    cryptkey = TextField(u'The key to decrypt your data', validators=[Required()])
    submit = SubmitField(u'submit')
    
    
class ResultForm(Form):
    
    def __init__(self, fid, furl, fcryptkey):
        self.fid = HiddenField(fid)
        self.furl = HiddenField(furl)
        self.fcryptkey = HiddenField(fcryptkey)
        
    submit = SubmitField(u'access content')