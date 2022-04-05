from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html' , pageTitle='Flask Server Honme page')

@app.route('/about')
def jin():
    return render_template('about.html', pageTitle='About VTM')

@app.route('/estimate', methods=['POST','GET'])
def estimate():
    Estimate=''
    if request.method == 'POST':
        form=request.form
        Radius = float(form['Radius'])
        Height = float(form['Height'])
        pi=3.14
        
        tanktoparea=pi*(Radius*Radius)

        tanksidearea= 2*(pi*(Radius*Height))

        totalarea= tanktoparea+tanksidearea

        inchtosq= totalarea/144

        materialcost=25
        totalmaterialcost=materialcost*inchtosq

        laborcost=15
        totallaborcost=laborcost*inchtosq

        Estimate = totalmaterialcost + totallaborcost

        #return redirect(url_for('index'))
        return render_template('estimate.html', pageTitle='Estimation',Estimate=Estimate) 
    #return redirect(url_for('estimate'))
    return render_template('estimate.html', pageTitle='Estimation',Estimate=Estimate)

if __name__ == '__main__':
    app.run(debug=True)