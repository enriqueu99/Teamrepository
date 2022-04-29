
from flask import Flask, redirect, render_template, url_for, Request,request


app = Flask(__name__)



@app.route('/', methods=["GET","POST"])
def form():
    if request.method == "POST":
        return render_template("display.html") 
    return render_template("website.html")
    

if __name__ == '__main__':
   app.run(debug=True)
   