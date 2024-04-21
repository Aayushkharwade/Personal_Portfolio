from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def homee():
    return render_template('index.html')

@app.route('/Projects')
def Projects():
    return render_template('Projects.html')

@app.route('/static/image')
def serve_static(path):
    root_dir = os.path.dirname(os.getcwd())
    return render_template(os.path.join(root_dir, 'static'), path)

if __name__ == ('__main__'):
    app.run(host='0.0.0.0')
