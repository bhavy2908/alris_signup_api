from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
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

@app.route("/", methods = ['POST', 'GET'])
def function():
    if request.method == 'POST':
        acc_no = request.form['acc_no']
        return jsonify(str(data(int(acc_no))))
    return "<p>Hello, World!</p>"