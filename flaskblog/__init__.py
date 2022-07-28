from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # __name__ ist eine spezielle Variable in Python: der Name vom Modul. Wenn man es in Python direkt ablaufen lässt, dann gilt: __name__ = __main__
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # The database URI that should be used for the connection. /// for relative path, creates site.db in project folder
db = SQLAlchemy(app) # Erzeuge Instanz von SQLAlchemy

from flaskblog import routes # watch circular imports, routes werden erst nach dem Erzeugen der App importiert, weil routes.py auch app.py importiert