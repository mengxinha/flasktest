from flask import Flask, request, json
from flask_cors import CORS
import openai


openai.api_key = "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"

app = Flask(__name__)
cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})

# @app.route('/')
# def hello_world():
#     return 'Hello World!'


@app.route('/getMsg', methods=['GET'])
def home(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = prompt,
        temperature=0.5,
        max_tokens=2048,
        n=1,
        stop=None
    )
    message = response.choices[0].text
    return message

prompt = request.json['message']
mes=home(prompt)


##启动运行
if __name__ == '__main__':
    app.run()