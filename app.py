from flask import Flask,render_template,request
from traductor import Traductor
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate",methods=["GET"])
def tanslator():
    try:
        langS = request.args.get("langS")
        langE = request.args.get("langE")
        text = request.args.get("text")
        t = Traductor(text,langE,langS)
        return t.trans()
    except:
        return "error"
if __name__ == "__main__":
    app.run(debug=True)