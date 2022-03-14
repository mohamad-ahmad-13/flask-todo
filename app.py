from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['TRACK_DATABASE_MODIFICATION'] = False

db = SQLAlchemy(app)
@app.route('/')
def index():
    return render_template('base.html')

