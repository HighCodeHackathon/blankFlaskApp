"""
The flask application package.
"""

import os
import urllib.parse
import pyodbc
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

params = urllib.parse.quote_plus("Driver={ODBC Driver 17 for SQL Server};Server=tcp:hackathonsss.database.windows.net,1433;Database=test;UID=Hackathon;Pwd=P@ssw0rd;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

import blankFlaskApp.views