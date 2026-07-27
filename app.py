from flask import Flask, render_template, request

from config import load_style
from rewriter import rewrite


app = Flask(__name__)

PROFILES = {
    "concise": "Concise",
    "preserve_punctuation": "Preserve Punctuation",
    "minimal_changes": "Minimal Changes",
}


@app.route("/", methods=["GET", "POST"])
def index():
    original_text = ""
    rewritten_text = ""
    selected_profile = "concise"

    if request.method == "POST":
        original_text = request.form.get("text", "").strip()
        selected_profile = request.form.get("profile", "concise")

        if selected_profile not in PROFILES:
            selected_profile = "concise"

        if original_text:
            config = load_style(profile=selected_profile)
            rewritten_text = rewrite(original_text, config)

    return render_template(
        "index.html",
        original_text=original_text,
        rewritten_text=rewritten_text,
        selected_profile=selected_profile,
        profiles=PROFILES,
    )


if __name__ == "__main__":
    app.run(debug=True)