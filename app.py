import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

dream_list = []

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        dream = request.form["dream"]
        dream_list.append(dream)
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(),
            temperature=1,
            max_tokens=100,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result, dream_list=dream_list)


def generate_prompt():

    # open text file in read mode
    text_file = open("example_prompts.txt", "r")
    text_file.close()

    return """Generate a new prompt with the phrases {}""".format(
        dream_list
    )


