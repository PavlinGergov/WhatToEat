1. Set up your virtual env.
2. Before each commit do not commit the virtualenv folder that you have made.
3. Do not forget to install Flask/SQLAlchemy modules .
pip3 install Flask
pip3 install flask-sqlalchemy
4. Do not commit __pycache__ folders  

5. At this point you schould have a working db.

If you do not, first run the python script for db_activation. You might receive an error, open up the main_logic file and 
comment out #import models, then run db_activation again. Do not forget to uncomment the #import models,
you should have a .db file in the folder, or somewhere
on the desktop.

You could download a SQLite Database Browser GUI that could help you visualize the tables better.

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

