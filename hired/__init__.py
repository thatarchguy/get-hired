from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

from hired.api import snort_api
from hired.views import common
app.register_blueprint(common)
