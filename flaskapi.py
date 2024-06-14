from flask import Flask, render_template, url_for, request, redirect, has_request_context, jsonify
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()

class NewFormatter(logging.Formatter):
   def format(self,record):
      if has_request_context():
         record.url = request.url
         record.remote = request.remote_addr
      else:
         record.url = None
         record.remote = None
      return super().format(record)
         


logformatter = NewFormatter("%(asctime)s - %(url)s - %(remote)s - %(levelname)s - %(message)s", datefmt = "%Y-%m-%d %H:%M:%S")

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logformatter)
logger.addHandler(consoleHandler)

fileHandler = RotatingFileHandler("logs.log", maxBytes=1024)
fileHandler.setFormatter(logformatter)
logger.addHandler(fileHandler)

app = Flask(__name__)

@app.route('/')
def index():
   app.logger.info("From route handler..")
   return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
   # app.logger.info("From login route handler..")
   errors={}
   if request.method == "POST":
      uname= request.form["nm"]
      
      if not uname[0].isalpha():
         errors["uname"]=["Name should start with an aplphabet"]
      # return f"<h1>Hi {uname} and your mail id is : {request.form["mail"]}</h1>"
   return render_template("login.html", errors=errors)

@app.route("/add", methods=["POST", "GET"])
def add():
   if request.method == "POST":
      
      num1= request.form["num1"]
      num2= request.form["num2"]

      
      try:
         ans=int(num1)+int(num2)
      except Exception:
         error_msg = 'Both values must be numbers'
         app.logger.error(error_msg)
         return jsonify({'error': error_msg}), 400

      return f"<h1>{num1} + {num2} = {ans}</h1>"
   else:
      return render_template("add.html")
   
@app.route("/param")
def par():
   q= request.args.to_dict()
   return "Hi {0}".format(q.get("city","No city"))

if __name__ == '__main__':
   app.run(debug=True)