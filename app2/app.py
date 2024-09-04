from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'demo app2'

if __name__ == '__main__':
   app.run(debug=True, port=8081, host='0.0.0.0')
