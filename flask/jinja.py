###Building url dynamically,jinja techniques
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
@app.route('/success/<int:score>')
def success(score):
   res=""
   if score > 50:
        res="You have passed the exam"
   else:
        res="You have failed the exam"
   return render_template('result.html', results=res)
if __name__ == '__main__':
    app.run(debug=True)