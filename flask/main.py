from flask import Flask,render_template
###WsGI app basix\c setup
app=Flask(__name__)
@app.route('/')
def welcome():
    return '<html><h1>Hii this is homepage</h1></html>'
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)