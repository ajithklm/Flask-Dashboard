from flask import Flask, render_template,jsonify,Response
import json

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/dashboard/')
def dashboard():
    with open('stk.json') as json_data:
        list = json.load(json_data)
    return Response(render_template('dashboard.html', result=list, mimetype='text/html'))
    
if __name__=="__main__":
    app.run(debug=True)
