from flask import Flask, render_template


app = Flask(__name__) #static_folder=",", static_url=path="")


@app.route("/")
def index():
    return "Hello World"

if __name__ == "main":
    app.run("0.0.0.0",port=8000, debug=True)


