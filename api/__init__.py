from flask import Flask

app = Flask(__name__)

from api import hello
from api import wind_service