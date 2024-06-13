from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
   if request.method == "POST":
      user= request.form["nm"]
      return f"<h1>Hi {user}</h1>"
   else:
      return render_template("login.html")

@app.route("/add", methods=["POST", "GET"])
def add():
   if request.method == "POST":
      num1= request.form["num1"]
      num2= request.form["num2"]
      ans=int(num1)+int(num2)
      return f"<h1>{ans}</h1>"
   else:
      return render_template("add.html")
   


if __name__ == '__main__':
   app.run(debug=True)