from flask import Flask, render_template, request

from config import load_style
from rewriter import rewrite


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    original_text = ""
    rewritten_text = ""

    if request.method == "POST":
        original_text = request.form.get("text", "").strip()

        if original_text:
            config = load_style()
            rewritten_text = rewrite(original_text, config)

    return render_template(
        "index.html",
        original_text=original_text,
        rewritten_text=rewritten_text,
    )


if __name__ == "__main__":
    app.run(debug=True)