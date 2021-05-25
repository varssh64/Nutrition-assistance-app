from flask import Flask ,render_template, request
app = Flask(__name__)
@app.route('/login')
def run_code():
    return render_template("login page.html")
@app.route('/uploaddata', method=["POST"])
def uploaddata():
    if request.method=="POST":
        name=request.form[""]

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=9000,debug = True) 