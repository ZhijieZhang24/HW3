from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle='My Calculator')


@app.route('/add', methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
      form = request.form
      try:
          numberOne = int(form['numOne'])
          numberTwo= int(form['numTwo'])
          calc = numberOne + numberTwo
          return render_template('index.html', display=calc, pageTitle='My Calculator')

      except ValueError:
          return render_template('index.html', display="Please enter two integers.", pageTitle='My Calculator')

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
