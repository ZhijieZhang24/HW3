from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle='My Calculator')
    return render_template('index.html', display="Your Discount Factor: ", display2="Your loan payment: ", pageTitle= 'Loan Calculator')

@app.route('/add', methods=['GET', 'POST'])
@app.route('/divide', methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
      form = request.form
      try:
          numberOne = int(form['numOne'])
          numberTwo= int(form['numTwo'])
          calc = numberOne + numberTwo
          return render_template('index.html', display=calc, pageTitle='My Calculator')
          A = float(form['A'])
          n = int(form['n'])
          i = float(form['i'])
          D = (((1 + i)**n)-1)/ (i*( 1 + i)**n)
          P = A/D

          return render_template('index.html', display=D,display2=P,pageTitle='Loan Calculator')

      except ValueError:
          return render_template('index.html', display="Please enter two integers.", pageTitle='My Calculator')

          return render_template('index.html', display="Please enter right number.", display2="Error",pageTitle='Loan Calculator')

    return redirect("/")

#def divide():
    #if request.method == 'POST':
        #form = request.form
        #try:
            #A = float(form['A'])
            #n = int(form['n'])
            #i = float(form['i'])
            #D = (((1 + i)**n)-1)/ ( i * ( 1+ i)**n)
            #P = A/D
            #return render_template('index.html', display2=P, pageTitle='Loan Calculator')

        #except ValueError:
            #return render_template('index.html', display2="Error", pageTitle='Loan Calculator')

        #return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
