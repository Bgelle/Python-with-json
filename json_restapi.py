import json
import argparse
from flask import Flask
app = Flask(__name__)
@app.route('/')
class ArithmeticAdd(Resource):
    # @app.route('/add/<int:num1>/<int:num2>')
    def get(self, num1, num2):
        return flask.jsonify({'add': num1 + num2})


class ArithmeticSub(Resource):
    # @app.route('/add/<int:num1>/<int:num2>')
    def post(self, num1, num2):
        return flask.jsonify({'sub': num1 - num2})


api.add_resource(ArithmeticAdd, '/add/<int:num1>/<int:num2>')

api.add_resource(ArithmeticSub, '/sub/<int:num1>/<int:num2>')

def get_data(filename):
   with open (filename,"r") as file:
       data=json.load(file)
   return data
parser = argparse.ArgumentParser()#//to get the parser object
parser.add_argument('-fn','--file_name',required=True, help="Please pass the file name to read")
args = parser.parse_args()
get_data(filename=args.file_name)
app.run()
