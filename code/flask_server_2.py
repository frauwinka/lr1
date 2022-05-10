from flask import Flask
from flask import redirect, abort, render_template
app = Flask(__name__)


users_list = [{'name': 'Anastasia', 'id': 1, 'surname': 'Karpunova', 'age': 21},
         {'name': 'Vadim', 'id': 2, 'surname': 'Secret', 'age': 20}]


@app.route('/')
def index():
    return redirect('http://127.0.0.1:5000/users')


@app.route('/users')
def users():
    return render_template('users.html', users=users_list)


@app.route('/users/<ID>')
def user(ID):
    for some_user in users_list:
        if some_user['id'] == int(ID):
            return render_template('user.html', some_user=some_user)
    return abort(404)


if __name__ == '__main__':
    app.run(debug=True)
