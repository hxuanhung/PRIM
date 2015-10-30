from flask import Flask
import MySQLdb

app = Flask(__name__)

mysql = None
def connect_db(host, user, pwd, db):
    global mysql
    mysql = MySQLdb.connect(host=host, user=user, passwd=pwd, db=db)
    if mysql is not None:
        app.logger.info("connected to database %s", db)
    cursor = mysql.cursor()
    return cursor

def close_db():
    if mysql is not None:
        mysql.close()
        app.logger.debug("Closing db")

from api import hello
from api import wind_service
from api import wind
