from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "Simple Flask App"
    }


@app.route("/about")
def about():
    return {
        "developer": "Harsh Bhagat",
        "project": "DevSecOps Demo Pipeline"
    }


if __name__ == "__main__":
    app.run(port=80)
