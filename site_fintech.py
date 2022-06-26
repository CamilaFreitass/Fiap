from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return render_template('teste2.html')

@app.route('/login')
def login():
    return render_template('teste1.html')

app.run(debug=True)
