
try:
    from flask import Flask, url_for, render_template, redirect
except ModuleNotFoundError as exc:
    if exc.name == "flask":
        raise ModuleNotFoundError(
            "Flask is required. Install it in the active Python environment with "
            "`python -m pip install Flask`."
        ) from exc
    raise
from questions import questions, MARKS

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", questions = questions, marks = MARKS)

def get_score(answers):
    score = 0
    for i, answer in enumerate(answers):
        if answer == questions[i]["answer"]:
            score += MARKS[questions[i]["difficulty"]]
    return score

if __name__ == "__main__":
    app.run(port=3506)