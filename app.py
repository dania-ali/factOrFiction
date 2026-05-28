from flask import Flask, render_template, request

from analysis import analyze_claim

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    claim = request.form.get("claim", "").strip()
    result = analyze_claim(claim) if claim else None
    return render_template("index.html", claim=claim, result=result)


if __name__ == "__main__":
    app.run(debug=True)
