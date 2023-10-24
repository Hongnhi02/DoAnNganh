from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_babelex import Babel
import cloudinary
from flask_admin import Admin, BaseView, expose

from flask_login import LoginManager
app = Flask(__name__)
cloudinary.config(
     cloud_name = 'dendeb697',
            api_key = '822515132138445',
            api_secret = 'bBck-UodqY0PZqDOOIjL2nBUHwc'

)
# co so du lieu
app.secret_key = '4567890sdfghjklcvbnvb4567fg6yug'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/data_da?charset=utf8mb4' % quote('318502')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app=app)

app.config['PAGE_SIZE'] = 3


login = LoginManager(app= app)

