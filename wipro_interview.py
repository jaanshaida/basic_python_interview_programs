from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/greet/<name>') #/greet/shaik
def greet(name):
    return render_template('greet.html', name=name)


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    age = request.form['age']
    return f'Name: {name}, Age: {age}'


if __name__ == '__main__':
    app.run()
