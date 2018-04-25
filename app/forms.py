from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField,TextAreaField,SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
ALLOWED_EXTENSIONS =['png', 'jpg', 'jpeg']

class CreateProfile(FlaskForm):
    
    Firstname=TextField('First Name',validators=[InputRequired()])
    
    Lastname=TextField('Last Name',validators=[InputRequired()])
    
    Gender=SelectField(u'Gender', choices=[('Male', 'Male'),('Female','Female'),('None','Prefer not to disclose'),('None',' None')])
    
    Email=TextField('Email',validators=[InputRequired()])
    
    Location=TextField('Location',validators=[InputRequired()])
    
    Biography=TextAreaField('Biography',validators=[InputRequired()])
    
    Profile_picture = FileField('Profile Picture', validators=[FileRequired(),FileAllowed(ALLOWED_EXTENSIONS, 'Images only!')])
    
    