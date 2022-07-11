
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import story


app = Flask(__name__)


@app.route("/")
def questions():
    """Asks user questions"""

    prompts = story.prompts

    return render_template("form.html", prompts=prompts)


@app.route('/story')
def display_story():
    """Return story."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)
