from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/<string:inpt_acc_no>')
def alris_ie(inpt_acc_no):
    inpt = str(inpt_acc_no)
    inpt_arr = inpt.split("_")
    usrname = int(inpt_arr[0])
    passwrd = int(inpt_arr[1])
    if usrname - passwrd == 987650000:
        return "yes"
    else:
        return "no"

    
    


if __name__ == "__main__":
    app.run(debug=True)