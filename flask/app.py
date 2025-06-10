from flask import Flask
###WsGI app basix\c setup
app=Flask(__name__)
@app.route('/')
def welcome():
    return 'Welcome to the Flask app.This is a amazing course!.yes it is'
@app.route('/index')
def index():
    return 'This is the index page'

if __name__ == '__main__':
    app.run(debug=True)
