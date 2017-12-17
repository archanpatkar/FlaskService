from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/Hello")
@app.route("/Hello/<name>")
def f1(name="World"):
    return "<h1>Hello {}! Welcome to Flask microserivce</h1>".format(name)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)