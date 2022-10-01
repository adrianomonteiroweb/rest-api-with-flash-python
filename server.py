from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///exemplo.db')
app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        conn = db_connect.connect()

        query = conn.execute("select * from user")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]

        return jsonify(result)

    def post(self):
      conn = db_connect.connect()

      name = request.json['name']
      email = request.json['email']

      conn.execute("insert into user values(null, '{0}','{1}')".format(name, email))

      query = conn.execute("select * from user order by id desc limit 1")
      result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]

      return jsonify(result)

class UserById(Resource):
  def get(self, id):
    conn = db_connect.connect()

    query = conn.execute("select * from user where id =%d " % int(id))
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]

    return jsonify(result)

api.add_resource(Users, '/users') 
api.add_resource(UserById, '/users/<id>') 

if __name__ == '__main__':
    app.run()
