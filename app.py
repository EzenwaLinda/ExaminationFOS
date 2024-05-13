from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    actors = db.Column(db.String(255), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)

def _repr_(self):
        return f'<Movie {self.title}>'


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/movies')
def movies():
    movies = Movie.query.all()
    return render_template('movies.html', movies=movies)


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        actors = request.form['actors']
        publication_year = request.form['publication_year']
        new_movie = Movie(title=title, genre=genre, actors=actors, publication_year=int(publication_year))
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('movies'))
    return render_template('add_movie.html')

if _name_ == '_main_':
    app.run(debug=True)


