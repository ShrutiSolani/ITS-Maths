from flask import Flask, render_template, request, flash, redirect, url_for, session
#from flask.ext.session import Session
from fractions import Fraction
import random
import os


app = Flask(__name__)


values = [Fraction('25/8'), Fraction('17/4'), Fraction('38/7'), Fraction('29/3'), Fraction('44/5')]
Image_folder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = Image_folder
full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'cross.jpg')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/mixed-fraction1", methods=['POST'])
def q1():
    if request.method == 'POST':
        num = random.randint(1, 100)
        den = random.randint(1, 25)
        while num < den:
            num = random.randint(1, 100)
        que = 'Express as mixed fraction : ' + str(num) + '/' + str(den) + '.'
        quo = num // den
        rem = num % den
        box_ans = [quo, rem, quo, rem, den]
        answer = {'que': que, 'b0': box_ans[0], 'b1': box_ans[1], 'b2': box_ans[2], 'b3': box_ans[3], 'b4': box_ans[4]}
        hint1 = 'Try dividing numerator by denominator'
        hint2 = 'After dividing N/D, quotient =' + str(quo) + ' remainder = ' + str(rem)
        hint3 = 'Mixed Fraction Answer :' + str(quo) + " (" + str(rem) + "/" + str(den) + ")"
        hints = {'h1': hint1, 'h2': hint2, 'h3': hint3}
        return render_template('display.html', answer=answer, hints=hints)
    else:
        return render_template('login.html')


@app.route("/mixed-fraction")
def question():
    num = random.randint(1, 100)
    den = random.randint(1, 25)
    while num < den:
        num = random.randint(1, 100)
    que = 'Express as mixed fraction : ' + str(num) + '/' + str(den) + '.'
    quo = num // den
    rem = num % den
    box_ans = [quo, rem, quo, rem, den]
    answer = {'que': que, 'b0': box_ans[0], 'b1': box_ans[1], 'b2': box_ans[2], 'b3': box_ans[3], 'b4': box_ans[4]}
    hint1 = 'Try dividing numerator by denominator'
    hint2 = 'After dividing N/D, quotient =' + str(quo) + ' remainder = ' + str(rem)
    hint3 = 'Mixed Fraction Answer :' + str(quo) + " (" + str(rem) + "/" + str(den) + ")"
    hints = {'h1': hint1, 'h2': hint2, 'h3': hint3}
    return render_template('display.html', answer=answer, hints=hints)


@app.route('/score/<counter>/<feedback>', methods=['POST'])
def score(counter, feedback):
    if request.method == 'POST':
        marks = 25-(int(counter)*5) - (int(feedback)*2)
        print(marks)
        if marks == 25:
            comment = "Well Done!!!"
        elif 20 <= marks < 25:
            comment = "You have just about mastered it"
        elif 15 <= marks < 20:
            comment = "Keep working on it you are improving"
        else:
            comment = "That's not half bad"
    else:
        print("Pass")

    show_message1 = 'Your points : '+str(marks)+'/25.'
    print(show_message1)
    flash(show_message1)
    flash(comment)
    return redirect(url_for('question'))


app.secret_key = 'super secret key'
app.run(debug=True)
