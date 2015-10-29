from api import app, connect_db, close_db
import numpy as np


def request_data(date, fctime):
    csv = np.genfromtxt('data/raw/20151017/OUT.TXT', delimiter=",")
    grb = csv[:, 4:7]
    return grb


def get_speed_at_point(date, fctime, lat, lon):
    cursor = connect_db('localhost','root','root','meteo')
    query = ('SELECT val FROM wind_speed WHERE lat = %s AND lon = %s AND validtime= %s')
    cursor.execute(query,(lat, lon, fctime))
    val = cursor.fetchall()[0][0] # get only 1 value instead of an array of another array

    cursor.close()
    return val

def find_nearest_idx(array, value):
    idx = (np.abs(array - value)).argmin()
    return array[idx]


def get_value_at_lat_lon(data, lat, lon):
    row_lat = data[abs(data[:, 0] - lat) < 0.024]
    row_lon = row_lat[abs(row_lat[:, 1] - lon) < 0.024]
    print row_lon
    speed_val = np.average(row_lon[:, 2])
    print speed_val
    return speed_val