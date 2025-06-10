from flask import Flask,render_template,request
###WsGI app basix\c setup
app=Flask(__name__)
@app.route('/')
def welcome():
    return '<html><h1>Hii this is homepage</h1></html>'
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
      name= request.form['name']
      email= request.form['email']
      return f'Name: {name}, Email: {email}'
    return render_template('form.html')
if __name__ == '__main__':
    app.run(debug=True)