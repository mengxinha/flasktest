from flask import Flask, request
from flask_cors import CORS
import openai

openai.api_key = "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"


app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/getMsg', methods=['POST'])
def hello():
    result = request.json.get('message'),
    response = openai.Completion.create(
        # text-davinci-003 是指它的模型
        model="text-davinci-003",
        prompt=result,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None
    )
    print(response.choices[0].text)
    return {
        "code": 200,
        "message": "操作成功",
        "data": response.choices[0].text
    }

if __name__ == '__main__':
    app.run()
