from flask import Flask# jsonify

#from db_logic import User, Db
from choose_by import check_fridge

#import json
#from operator import itemgetter
#from machine_learning import get_suggested


app = Flask(__name__)

app.secret_key = "v101-3"

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS,HEAD')
  return response

@app.route('/')
def home():
    return 'hello'

@app.route('/check')
def get_recipes():
    products = check_fridge()
    return products




#@app.route('/api/recipes', methods =['GET'])
#def get_recipes():
#    return jsonify({'recipes': recipes})
