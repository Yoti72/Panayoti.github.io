from flask import Flask
from views import views
import os

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
#import sqlite3



# to run the website
if __name__ == '__main__':
    app.run(debug=True)

