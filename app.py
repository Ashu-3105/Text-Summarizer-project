from flask import Flask, render_template,url_for
from flask import request as req
import requests


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
@app.route("/Summarize",methods=["GET", "POST"])
def Summarize():
    if req.method=="POST":


        API_TOKEN = 'write your own Api key'
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        data=req.form['data']
        minl = 20
        maxl = int(req.form['maxl'])

        def query(payload):

            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json() 

        output = query({"inputs": data, "parameters": {"min_length": minl, "max_length": maxl}})[0]
        return render_template('index.html', result=output['summary_text'])
    else:
        return render_template('index.html')    
    
    
if __name__ == '__main__':
    app.debug = True
    app.run()







