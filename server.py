from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # 🔥 ВОТ ЭТО ГЛАВНОЕ

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/detect", methods=["POST"])
def detect():
    data = request.json
    text = data.get("text", "")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
Определи математическую тему задачи.
Верни только одно слово (например: дроби, уравнения, геометрия).

Задача:
{text}
"""
                }
            ]
        )

        topic = response.choices[0].message.content.strip()

        return jsonify({"topic": topic})

    except Exception as e:
        print("AI ERROR:", e)
        return jsonify({"topic": "Без темы"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)