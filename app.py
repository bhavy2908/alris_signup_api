from flask import Flask, request, jsonify, render_template
import pandas as pd
from flask_cors import CORS

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

@app.route('/return/index')
def return_index():
    return render_template('return calculator/index.html')

@app.route("/api", methods = ['POST', 'GET'])
def function():
    if request.method == 'POST':
        acc_no = request.json['acc_no']
        return jsonify(str(data(int(acc_no))))
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)