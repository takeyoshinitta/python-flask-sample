from flask import Flask, render_template, request

app = Flask(__name__)

names = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def greet():
    name = request.form.get('name')

    if name:
        greeting = generate_greeting(name)
        return render_template('result.html', greeting=greeting, error=None, names=names)
    else:
        error_message = "Please enter your name."
        return render_template('result.html', greeting=None, error=error_message, names=names)

def generate_greeting(name):
    names.append(name)
    greeting = f"Hello, {name}!"
    return greeting

if __name__ == '__main__':
    app.run(debug=True)
