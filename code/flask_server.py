from flask import Flask
from flask import request, make_response, redirect, abort
app = Flask(__name__)


users = [{'name': 'Anastasia', 'id': 1, 'surname': 'Karpunova', 'age': 21},
         {'name': 'Vadim', 'id': 2, 'surname': 'Secret', 'age': 20}]

@app.route('/')
def index():
    return redirect('http://127.0.0.1:5000/users')

@app.route('/users')
def user():
    data = ''
    for i in users:
        data += f'<h1><a href=http://127.0.0.1:5000/users/{i["id"]}>{i["name"]} {i["surname"]}</a></h1>'
        data += '\n'
    return data

@app.route('/users/<ID>')
def user_name(ID):
    for i in users:
        if i['id'] == int(ID):
            return f'<h2>{i["name"]} {i["surname"]}</h2>\n' \
                   f'<p>age: {i["age"]}</p>\n' \
                   f'<p>id: {i["id"]}</p>'
    return abort(404)

if __name__ == '__main__':
    app.run(debug=True)
