from flask import Flask, render_template, request, redirect
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
    articles = Article.query.order_by(-Article.id).all()
    return render_template('blog.html', articles=articles)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/success')
        except:
            return 'При добавлении статьи произошла ошибка...'
    else:
        return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
