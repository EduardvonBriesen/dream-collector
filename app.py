import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        dream = request.form["dream"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(dream),
            temperature=1,
            max_tokens=100,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(dream):
    return """Generate a text-to-image prompt from the following dream: {}""".format(
        dream.capitalize()
    )
