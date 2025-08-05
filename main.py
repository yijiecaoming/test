import os
from flask_cors import CORS
from flask import Flask

from api import area_api, evaluation_api
from config import HOST, PORT, DEBUG

from models import init_db

# 初始化数据库表
print(init_db())

# 创建Flask应用
app = Flask(__name__)

app.secret_key = os.urandom(24)
CORS(app)

# 蓝图注册到应用
app.register_blueprint(area_api, url_prefix='/api')
app.register_blueprint(evaluation_api, url_prefix='/api')

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
