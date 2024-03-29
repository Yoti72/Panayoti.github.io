from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from views import views
import os
from flask_assets import Environment, Bundle
import requests
import configparser

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

assets = Environment(app)

#js = Bundle('jquery.js', 'base.js', 'widgets.js',
#            filters='jsmin', output='gen/packed.js')
#assets.register('js_all', js)

# Configure Flask-SQLAlchemy
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db = SQLAlchemy(app)

#class Contact(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(100), nullable=False)
#    email = db.Column(db.String(100), nullable=False)
#    message = db.Column(db.Text, nullable=False)

# to run the website
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


#@app.route('/contact', methods=['POST'])
#def contact():
#    name = request.form['name']
#    email = request.form['email']
#    message = request.form['message']

#    contact = Contact(name=name, email=email, message=message)
#    db.session.add(contact)
#    db.session.commit()

 #   return 'Thank you for your submission!'









#from flask import Flask
#from views import views
#import os

#app = Flask(__name__)
#app.register_blueprint(views, url_prefix="/")
#import sqlite3



# to run the website
#if __name__ == '__main__':
#    app.run(debug=True)


#