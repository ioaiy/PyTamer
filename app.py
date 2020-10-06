import sys
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
# This two string for the log file on Heroku
# app.logger.addHandler(logging.StreamHandler(sys.stdout))
# app.logger.setLevel(logging.ERROR)
app.config.from_object('settings')
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

