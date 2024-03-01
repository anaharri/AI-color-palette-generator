import openai
import json
from dotenv import dotenv_values
from flask import Flask, render_template, request

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

app = Flask(__name__, template_folder="templates")


def get_colors(query):
    prompt = f"""
    You are a color palette generating assistant that responds to text prompts for color palettes. You should generate color palettes that fit the theme, mood, or instructions in the prompt. The palettes should be between 2 and 6 colors, and the output should be in the form of a JSON array.

    Input: ocean landscape
    Output: ["#004f6d", "#0087a8", "#00b2e0", "#29c4ff", "#62d9ff"]

    Input: {query}
    Output:
    """

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50,
    )

    return response.choices[0].message.content


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/palette", methods=["POST"])
def get_palette():
    query = request.form.get("query")
    colors = get_colors(query)
    return json.loads(colors)


if __name__ == "__main__":
    app.run(debug=True)


# extra feature: a partir de un color, solicitar otras paletas que lo contengan
# Para levantar el proyecto:
# .\env\Scripts\activate
# flask run --debug
