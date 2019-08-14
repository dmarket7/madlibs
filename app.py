from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    """Return homepage."""

    return render_template("form.html", prompts=story.prompts, title='Madlibs')


@app.route('/story', methods=["POST"])
def create_story():
    """ Creating the story from user prompt """
    story_text = story.generate(request.form)
    return render_template("story.html", story=story_text, title='Your Story')
