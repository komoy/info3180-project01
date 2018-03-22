"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os

from app import app,db
from flask import render_template, request, redirect, url_for, flash,session, abort
from forms import CreateProfile
from model import UserProfile
from werkzeug.utils import secure_filename
import datetime

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile' , methods=["GET", "POST"])
def profile():
    form = CreateProfile()
    if request.method == "POST" and form.validate_on_submit():
        try:
        
            created_on=str(datetime.datetime.now()).split()[0]

            photo=form.Profile_picture.data
           
            photo_filename = secure_filename(photo.filename)
            
        
            user=UserProfile(form.Firstname.data,form.Lastname.data,form.Gender.data,form.Location.data,form.Biography.data,created_on,photo_filename)
      
        
            db.session.add(user)
            db.session.commit()
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        
            flash("Profile Added", "success")
            return redirect(url_for("profiles"))
        except Exception as e:
            db.session.rollback()
            flash("Internal Error", "danger")
            return render_template("profile.html", form =form)
        
@app.route("/profiles")
def profiles():
    users = UserProfile.query.all()
    profiles = []
    
    for user in users:
        profiles.append({"profile_pic": user.photo, "firstname":user.first_name, "lastname": user.last_name, "gender": user.gender, "location":user.location, "id":user.userid})
    
    return render_template("profiles.html", profiles = profiles)

@app.route('/profile/<userid>')
def profile_i(userid):
    user = UserProfile.query.filter_by(id=userid).first()
    
    if user is None:
        return redirect(url_for('home'))
        
    yr = int(user.created_on.split("-")[0])
    mth= int(user.created_on.split("-")[1])
    dy = int(user.created_on.split("-")[2])
    
    user.created_on = format_date_joined(yr, mth, dy)
    
    return render_template("profile.html", user=user)

def format_date_joined(yy,mm,dd):
    return datetime.date(yy,mm,dd).strftime("%B, %d,%Y")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
