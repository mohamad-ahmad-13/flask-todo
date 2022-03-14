from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

db.create_all()

class Todo(db.Model):
    id = db.Column(db.Integer)
    title = db.Column(db.String(100))
    completed = db.Column(db.Boolean, defaul=False)

    def __repr__(self) :
        return f"task: {self.title}"

@app.route('/')
def index():
    todo_list = Todo.query.all()
    return render_template('base.html', items=todo_list)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

