from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/<int:movie_id>')
def page_one(movie_id):
    movies = []
    return render_template("homepage.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
