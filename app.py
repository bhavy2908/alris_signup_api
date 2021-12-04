from flask import Flask, request, jsonify, render_template
import pandas as pd
from flask_cors import CORS
import random
from lstm import alris_lstm

app = Flask(__name__)
CORS(app)
df = pd.read_csv('data.csv')
df2 = pd.read_csv('res.csv')



def data(acc_number):
    cur_df = df.loc[df['Account Number'] == acc_number].reset_index()
    cur2_df = df2.loc[df2['account number'] == acc_number]
    factor = cur2_df['FACTOR'].to_numpy()[0]
    invest_to = cur2_df['Invest to'].to_numpy()[0]
    bal = cur_df['Savings'].sum()
    avg_exp = cur_df['Expenditure'].sum()/24
    avg_inc = cur_df['Income'].sum()/24
    name = cur_df['Name'].iloc[0]
    cur_df = cur_df.drop(range(19))
    inc = cur_df['Income'].to_numpy()
    exp = cur_df['Expenditure'].to_numpy()
    sav = cur_df['Savings'].to_numpy()
    annual = random.randint(50,80)
    monthly = random.randint(30,50)
    return {
        "inc": list(inc),
        "exp": list(exp),
        "sav": list(sav),
        "bal": bal,
        "name": name,
        "exptd_inc": avg_inc,
        "exptd_exp": avg_exp,
        "invest_to": invest_to,
        "ati": bal*0.08/(1+factor),
        "exptd_ret": bal*0.08,
        "annual": annual,
        "monthly": monthly,
        "annual_x": 100-annual,
        "monthly_x": 100-monthly,

    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/signIn')
def signIn():
    return render_template('login/signIn.html')

@app.route('/alris-main/index')
def alris_main_index():
    dics = data(int(request.args.get('username')))
    return render_template('alris-main/index.html', data=dics)

@app.route('/alris-main/about')
def alris_main_about():
    return render_template('alris-main/about.html')

@app.route('/alris-main/profile')
def alris_main_profile():
    return render_template('alris-main/profile.html')

@app.route('/return/index', methods = ['POST', 'GET'])
def return_index():

    if request.method == "POST":
        s1 = int(request.form['s1'])
        s2 = int(request.form['s2'])
        s3 = int(request.form['s3'])
        khatka = request.form['khatka']
        res = alris_lstm(s1, s2, s3, khatka)
        data = {
            "m1": res[0][0],
            "m2": res[0][1],
            "m3": res[0][2],
            "m4": res[0][3],
            "m5": res[0][4],
            "i1": res[1][0],
            "i2": res[1][1],
            "i3": res[1][2],
            "i4": res[1][3],
            "i5": res[1][4],
            "risk_factor": khatka,
            "exptd_ret": s2,
            "exptd_tp": s3,
        }
        return render_template('return calculator/index.html', data=data)

    return render_template('return calculator/index.html', data = {
            "m1": None,
            "m2": None,
            "m3": None,
            "m4": None,
            "m5": None,
            "i1": None,
            "i2": None,
            "i3": None,
            "i4": None,
            "i5": None,
            "risk_factor":None,
            "exptd_ret": None,
            "exptd_tp": None,
        })

@app.route("/api", methods = ['POST', 'GET'])
def function():
    if request.method == 'POST':
        acc_no = request.json['acc_no']
        return jsonify(str(data(int(acc_no))))
    return "<p>Hello, World!</p>"



if __name__ == '__main__':
    app.run(debug=True)