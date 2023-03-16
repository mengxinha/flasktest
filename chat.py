from flask import Flask, request, json
from flask_cors import CORS
import openai

openai.api_key = "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"

app = Flask(__name__)
cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
@app.route('/getMsg', methods=['POST'])
def completion(prompt):
    response = openai.Completion.create(
        # text-davinci-003 是指它的模型
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None
    )
    message = response.choices[0].text
    return message

def get_data():
    if request.method == 'POST':
        print("fds")
        argsJson = request.data.decode('utf-8')
        argsJson = json.loads(argsJson)
        print(argsJson)
        result = process_json(argsJson)
        result = json.dumps(result, ensure_ascii=False)  # 转化为字符串格式
        mes = completion(result)
        return {
            'code': 200,
            'message': mes, # return会直接把处理好的数据返回给前端
            'data': "成功",
        }
    else:
        return " 'it's not a POST operation! "

def process_json(data):
    return data

if __name__ == '__main__':
    app.run()
