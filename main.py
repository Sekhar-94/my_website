from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')

def home():
    #return "Hello, Shekhar how are you!"
    return render_template('index.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)