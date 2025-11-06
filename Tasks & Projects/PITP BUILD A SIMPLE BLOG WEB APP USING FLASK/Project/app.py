from flask import Flask, render_template, request, redirect, url_for
import os

# Get current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Tell Flask exactly where the templates are
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'))

# Temporary database (list of posts)
posts = []

# Homepage - Show all posts
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# Add Post Page
@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # Save post in list
        posts.append({'title': title, 'content': content})

        return redirect(url_for('index'))

    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
