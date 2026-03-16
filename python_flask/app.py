from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def gello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route("/search")
def show_search():
    args_dict = request.args.to_dict()
    print(request.args['word'])
    # print(request.args.word) # MultiDict 객체이므로 지원하지 않음
    print(request.args.get('num'))
    return args_dict

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    print(request.get_json().get('word'))
    # print(request.get_json().word) # Dict이지만, json은 key-value 구조 그 자체이므로 접근 불가
    print(request.get_json()['num'])
    return data

@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    print(request.get_json().get('word'))
    print(request.get_json()['num'])
    return data

@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    print(request.get_json().get('word'))
    print(request.get_json()['num'])
    return data

if __name__ == '__main__':
    app.run()