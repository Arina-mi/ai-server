from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="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")  # 👈 вставь свой ключ

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
        return jsonify({"topic": "Без темы", "error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)