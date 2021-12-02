from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/signin/<string:inpt_acc_no>')
def alris_ie(inpt_acc_no):
    inpt = inpt_acc_no
    inpt_arr = inpt.split("_")
    usrname = int(inpt_arr[0])
    passwrd = int(inpt_arr[1])
    if usrname - passwrd == 987650000:
        dict = {0 : "yes"}
    else:
        dict = {0 : "no"}
    response = app.response_class(
        response=json.dumps(dict),
        status=200,
        mimetype='application/json'
    )
    return response 


@app.route('/')
def alris():
    return "Welcome to alris' API"


if __name__ == "__main__":
    app.run(debug=True)