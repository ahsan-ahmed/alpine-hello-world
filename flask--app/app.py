from flask import Flask
app = Flask(__name__)

@app.route('/')
def mean():
    return 'my name is ahsan ahmed!!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')