from flask import Flask
app = Flask(_name_)
@app.route('/')
def index():
    return "Привет, мир!"
app.run(port='8000')
