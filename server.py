from flask import *
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("piano.html")

@app.route("/freq", methods=["GET", "POST"])
def getAction():
    if request.method == "GET":
        f = open('./data.txt', 'r', encoding='UTF-8')
        data = f.read()
        f.close()
        return data

    if request.method == "POST":
        payload = request.json
        freq = str(payload.get('freq'))
        print(freq)
        f = open('./data.txt', 'w', encoding='UTF-8')
        f.write(freq)
        f.close()
        return freq


app.run(host="192.168.0.16", port=8000)