from sqlalchemy import create_engine
from flask import Flask, request, jsonify
from flask_resful import Resource, Api

db_connect = create_engine('sqlite:///exemplo.db')

app = Flask(__name__)
api = Api(app)
