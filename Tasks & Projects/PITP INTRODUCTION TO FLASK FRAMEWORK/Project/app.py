from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # yahan se variable HTML ko bhej rahe hain
    return render_template('index.html', name='Saeed', message='Flask + Jinja2 is working perfectly!')

if __name__ == '__main__':
    app.run(debug=True)
