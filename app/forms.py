from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField,TextAreaField,SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
ALLOWED_EXTENSIONS =['png', 'jpg', 'jpeg']

class CreateProfile(FlaskForm):
    Firstname=TextField('Firstname',validators=[InputRequired()])
    
    Lastname=TextField('Lastname',validators=[InputRequired()])
    
    Gender=SelectField(u'Gender', choices=[('Female', 'Male')])
    
    Email=TextField('Email',validators=[InputRequired()])
    
    Location=TextField('Location',validators=[InputRequired()])
    
    Biography=TextAreaField('Biography',validators=[InputRequired()])
    
    Profile_picture = FileField('Profile Picture', validators=[FileRequired(),FileAllowed(ALLOWED_EXTENSIONS, 'Images only!')])
    
    