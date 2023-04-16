import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index_html():
    return render_template("index.html")

@app.route('/generic')
def generic_html():
    return render_template("generic.html")

@app.route('/')
def updates():
    
    url = "https://newsapi.org/v2/top-headlines"
    api_key = "fdc4b1f955dd4abdb25196d0491da958" 
    params = {
        "country": "in", 
        "category": "sports", 
        "apiKey": api_key

    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        
        data = response.json()
        
        
        articles = data["articles"]
        
        
        return render_template('generic.html', articles=articles)
    else:
        
        return f"Error: {response.status_code} - {response.text}"

if __name__ == '__main__':
    app.run()