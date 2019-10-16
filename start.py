from Flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')
    
if __name__ == '__main__':
    app.run(host= '192.168.1.210', port=5000,debug=True)