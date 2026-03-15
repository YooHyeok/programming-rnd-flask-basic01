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

if __name__ == '__main__':
    app.run()