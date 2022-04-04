from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html' , pageTitle='Flask Server Honme page')

@app.route('/jin')
def mike():
    return render_template('jin.html', pageTitle='ALL About Jin')

if __name__ == '__main__':
    app.run(debug=True)