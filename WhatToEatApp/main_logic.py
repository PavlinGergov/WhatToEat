import os
import models
from flask import Flask, render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from validation import Validation

#determine the absolute path to the current python file
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#congifuration of the path to the database = 'sqlite:///path/to/database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tables.db')
# We need a secret to use flash, but I am not sure how to make it to work
app.config['SECRET_KEY'] = "neshto si"
db = SQLAlchemy(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    error = None
    if request.method == "POST":
        un = request.form["username"]
        password = request.form["password"]
        
        #if the user is in the db and the passwords match you could make a render_template()

        #else show him appropriate message

    # get request for signin
    return render_template("signin.html")

@app.route("/about")
def about():
    flash('pesho')
    return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        un = request.form['username']
        email = request.form['email']
        password = request.form['password']

        v = Validation()
        if v.check_validation(un, email, password):
            #put the user in the db
             u = models.User(username = un, email = email, password = password)
             db.session.add(u)
             db.session.commit()
             # render the template where the user is logged in 
             return render_template("user_logged.html")
        else:
            #validation did not succeed, showing the user a flash message
            flash("Sorry, but some of your input is not enough secured")
            return render_template("signup.html")

    #get request for signup
    return render_template("signup.html")

    #import os
#import sys
#
#path = '/home/bgvladedivac/path/to/flask_app_directory'
#if path not in sys.path:
#    sys.path.append(path)
#
#from main_flask_app_file import app as application
#
# NB -- many Flask guides suggest you use a file called run.py; that's
# not necessary on PythonAnywhere.  And you should make sure your code
# does *not* invoke the flask development server with app.run(), as it
# will prevent your wsgi file from working.subl

