from flask import Flask
from flask import render_template
import sqlite3



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/rohan")
def rohan():
    return "Hello, Rohan"

@app.route("/recommendation2000s")
def recommend2000s():

    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM movies2000s ORDER BY RANDOM() LIMIT 1")
    movie = cursor.fetchone()

    movieData = [dict(name = movie[0], year = movie[1], poster = movie[2], prime = movie[3], yt = movie[4],
                google = movie[5], vudu = movie[6], itunes = movie[7], netflix = movie[8])]

    return render_template("recommendation.html", movieData=movieData)

@app.route("/recommendation1990s")
def recommend1990s():

    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM movies1990s ORDER BY RANDOM() LIMIT 1")
    movie = cursor.fetchone()

    movieData = [dict(name = movie[0], year = movie[1], poster = movie[2], prime = movie[3], yt = movie[4],
                google = movie[5], vudu = movie[6], itunes = movie[7], netflix = movie[8])]

    return render_template("recommendation.html", movieData=movieData)

@app.route("/recommendation1980s")
def recommend1980s():

    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM movies1980s ORDER BY RANDOM() LIMIT 1")
    movie = cursor.fetchone()

    movieData = [dict(name = movie[0], year = movie[1], poster = movie[2], prime = movie[3], yt = movie[4],
                google = movie[5], vudu = movie[6], itunes = movie[7], netflix = movie[8])]

    return render_template("recommendation.html", movieData=movieData)

@app.route("/recommendation1970s")
def recommend1970s():

    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM movies1970s ORDER BY RANDOM() LIMIT 1")
    movie = cursor.fetchone()

    movieData = [dict(name = movie[0], year = movie[1], poster = movie[2], prime = movie[3], yt = movie[4],
                google = movie[5], vudu = movie[6], itunes = movie[7], netflix = movie[8])]

    return render_template("recommendation.html", movieData=movieData)
    
if __name__ == "__main__":
    app.run(debug=True)