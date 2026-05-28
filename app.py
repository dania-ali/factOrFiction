from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    claim = request.form.get("claim", "").strip()
    return render_template("index.html", claim=claim)


if __name__ == "__main__":
    app.run(debug=True)
