import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from flask import Flask, render_template, request,jsonify
from brain.thinker import think

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/ask", methods=["POST"])
def ask():
    user = request.form.get("user","")
    answer = think(user)
    return jsonify({"reply": answer})


if __name__ == "__main__":
    app.run(debug=True)
