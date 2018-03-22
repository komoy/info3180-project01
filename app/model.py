from . import db
from datetime import datetime

class UserProfile(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    
    first_name = db.Column(db.String(80), nullable=False)
    
    last_name = db.Column(db.String(80), nullable=False)
    
    gender= db.Column(db.String(80), nullable=False)
    
    email=db.Column(db.String(120), nullable=False)
    
    location=db.Column(db.String(255), nullable=False)
    
    biography=db.Column(db.Text(300), nullable=False)
    
    photo=db.Column(db.String(80))
    
    created_on=db.Column(db.String(20), nullable=False)
    
    __tablename__ = "users"

    def __init__(self,first_name,last_name,gender,email,location,biography,created_on,photo):
        
        self.first_name = first_name
        
        self.last_name = last_name
        
        self.gender = gender
        
        self.email = email
        
        self.location = location
        
        self.biography = biography
        
        self.created_on = created_on
        
        self.photo = photo
   
    def __repr__(self):
         
        return "UserProfile: {0} {1}".format(self.first_name, self.last_name)
