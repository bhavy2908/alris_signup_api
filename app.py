from flask import Flask, jsonify
from werkzeug.wrappers import request
app = Flask(__name__)

@app.route('/signin/<string:inpt_acc_no>', methods = ['POST'])
def alris_ie(inpt_acc_no):
    if request.method == 'POST':
        inpt = inpt_acc_no
        inpt_arr = inpt.split("_")
        usrname = int(inpt_arr[0])
        passwrd = int(inpt_arr[1])
        string = "no"
        if usrname - passwrd == 987650000:
            string = "yes"
        else:
            string = "no"
        print(request.get_json())
        return jsonify(string) 


@app.route('/')
def alris():
    return "Welcome to alris' API"


if __name__ == "__main__":
    app.run(debug=True)