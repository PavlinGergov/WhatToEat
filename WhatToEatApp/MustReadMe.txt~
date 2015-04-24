1. Set up your virtual env.
2. Before each commit do not commit the virtualenv folder that you have made.
3. Do not forget to install Flask/SQLAlchemy modules .
pip3 install Flask
pip3 install flask-sqlalchemy
4. Do not commit __pycache__ folders  

5. The script that you need to run in Python3.4 shell to create the db models:

from main_logic import db
from models import User
db.create_all()

After that you will see a file that ends in .db extension, you could download
a SQLite Database Browser GUI that could help you visualize the tables better.

I am not sure if the file will be in the same folder, or on the Destkop.

This is the DB model at that point, so most likely its going to change.

6. Creating an object that will be stored in our DB is just like creating a 
normal python object. Example:

	u = User(name="RadoRado")
	
In order to store it, we have to use the session object and commit it, using
the db object that we have in our main_logic.py file. 
	
	db.session.add(u)
	db.session.commit()

7. Getting an object from our Database:
	- get it by primary key - User.query.get(1)
	- get all objects - User.query.all()
	- select something specific - User.query.filter_by(username="radorado").first

8. Everybody is free to add anything valuable in this document, that way its going to 
be easier for us to see the important new things that we need to be familiar with.

