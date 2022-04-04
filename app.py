from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html' , pageTitle='Flask Server Honme page')

@app.route('/jin')
def jin():
    return render_template('jin.html', pageTitle='ALL About Jin')

@app.route('/estimate')
def estimate():

    return render_template('estimate.html', pageTitle='Estimation')

if __name__ == '__main__':
    app.run(debug=True)