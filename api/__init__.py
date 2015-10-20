from flask import Flask
import numpy as np

app = Flask(__name__)
grb_wind = None


def create_dev_data():
    csv = np.genfromtxt('data/raw/20151017/OUT.TXT', delimiter=",")
    global grb_wind
    grb_wind = csv[:, 4:7]


create_dev_data()

from api import hello
from api import wind_service
from api import wind
