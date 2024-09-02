# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/project/<name>')
def hello_name(name):
   return 'project %s!' % name

if __name__ == '__main__':
   app.run()
