from flask import Flask

app = Flask(__name__) # __name__ ist eine spezielle Variable in Python: der Name vom Modul. Wenn man es in Python direkt ablaufen lässt, dann gilt: __name__ = __main__

@app.route("/") # mit dem Slash ist die Stammwebseite gemeint aka Homepage
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
