from flask import Flask, render_template, url_for

app = Flask(__name__) # __name__ ist eine spezielle Variable in Python: der Name vom Modul. Wenn man es in Python direkt ablaufen lässt, dann gilt: __name__ = __main__

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/") # mit dem Slash ist die Stammwebseite gemeint aka Homepage
@app.route("/home") # zweite Route für den gleichen Inhalt
def home():
    return render_template('home.html', posts=posts)

@app.route("/about") # mit dem Slash ist die Stammwebseite gemeint aka Homepage
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
