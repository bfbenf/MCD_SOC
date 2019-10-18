from flask import Flask, render_template, url_for, flash, redirect, request_started, request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')
    
if __name__ == '__main__':
    app.run(host= '192.168.43.143', port=5000,debug=True)