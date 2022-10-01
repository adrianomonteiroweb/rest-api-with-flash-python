from sqlalchemy import create_engine
from flask import Flask, request, jsonify
from flask_resful import Resource, Api

db_connect = create_engine('sqlite:///exemplo.db')

app = Flask(__name__)
api = Api(app)

class Users(Resource):
  def get(self):
    conn = db_connect.connect()

    query = conn.execute("select * from user")
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]

    result jsonify(result)
