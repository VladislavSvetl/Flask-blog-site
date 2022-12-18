from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


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


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User information: ' + name + ' ' + str(id)


if __name__ == '__main__':
    app.run(debug=True)
