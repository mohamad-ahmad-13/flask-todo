from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self) :
        return f"task: {self.title}"

db.create_all()

@app.route('/')
def index():
    
    todo_list = Todo.query.all()
    return render_template('base.html', items=todo_list)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    new_todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/update/<int:item_id>')
def update(item_id):
    item = Todo.query.filter_by(id=item_id).first()
    item.completed = not item.completed
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<int:item>')
def delete(item):
    todo = Todo.query.filter_by(id=item).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))