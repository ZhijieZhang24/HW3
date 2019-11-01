from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="Your Discount Factor: ", display2="Your Loan Payment: ", pageTitle='Loan Calculator')


@app.route('/divide', methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
      form = request.form
      try:
          A = float(form['A'])
          n = int(form['n'])
          i = float(form['i'])
          D = (((1 + i)**n)-1)/ (i*( 1 + i)**n)
          P = A/D

          return render_template('index.html', display=(f'Your Discount Factor: {D:.2f}'),display2=(f'Your Loan Payment: ${P:.2f}'),pageTitle='Loan Calculator')

      except ValueError:

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
