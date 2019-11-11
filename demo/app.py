from flask import Flask, escape, url_for, request,render_template
app = Flask(__name__)

#@app.route("/")
#def main():
#    return "Welcome!"


#@app.route('/index')
#def index():
#    return 'Index Page'

#@app.route('/hello')
#def hello():
#    return 'Hello, World'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
    
#@app.route('/user/<username>')
#def show_user_profile(username):
#    # show the user profile for that user
#    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#       return do_the_login()
#    else:
#        return show_the_login_form()


@app.route('/profile/<username>')
def profile(username):
    return render_template('username.html', username=username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    #print(url_for('static', filename='style.css'))

if __name__ == "__main__":
    app.run(debug=True)