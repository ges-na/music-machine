from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/gesina/projects/musicmachine/musicmachine/dev.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
from models import *
migrate = Migrate(app, db)

if __name__ == "__main__":
    from views import *
    app.run(debug=True)
