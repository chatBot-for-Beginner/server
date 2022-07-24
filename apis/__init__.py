from flask import Flask, request
from flask_restx import Resource, Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config # 데이터베이스 기초정보 불러오기

import os
import random

db = SQLAlchemy()
migrate = Migrate()

# orm을 실행할 데이터베이스 연결

app = Flask(__name__)

app.config.from_object(config) # config 읽어오기

# 앱에 db 등록
db.init_app(app)
migrate.init_app(app, db) 

api = Api(app)

todos = {}
count = 1

@api.route('/todos')
class TodoPost(Resource):
    def post(self):
        global count
        global todos

        idx = count
        count += 1
        todos[idx] = request.json.get('data')

        return {'todo_id': idx, 'data': todos[idx]}

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=80)