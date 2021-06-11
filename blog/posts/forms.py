from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class PostForm(FlaskForm):
    title         = StringField('Title', validators = [DataRequired()])
    post_picture  = FileField('Update Profile Picture', validators = [FileAllowed(['jpg', 'png'])])
    content       = TextAreaField('Content', validators = [DataRequired()])
    submit        = SubmitField('Post')
    
    
