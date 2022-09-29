from transformers import pipeline
from flask import Flask,render_template,request
import os

app = Flask(__name__)
@app.route('/')
def home():
    print("Text generator")
    return("Hello")

@app.route('/gen',methods=["POST"])
def generate():
    t = ""
    txt = ""

    req_Json = request.json
    txt = req_Json['text']

    gen = pipeline(task = 'text-generation', model = 'gpt2')
    t = gen(txt, max_length = 1000, num_return_sequences = 1)

    return(t[0])  

@app.route('/genhtml',methods=["GET", "POST"])
def generatehtml():
    t = ""
    txthtml = ""
    if request.method == "POST":
        txthtml = request.form.get('txt')
        gen = pipeline(task = 'text-generation', model = 'gpt2')
        t = gen(txthtml, max_length = 1000, num_return_sequences = 1)

    return render_template('index.html', generate = t)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT", 8080)))
