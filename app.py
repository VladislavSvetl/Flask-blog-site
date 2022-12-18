from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r' %self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/works')
def works():
    return render_template('works.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/create')
def create():
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
