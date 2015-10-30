from api import app, connect_db, close_db
import numpy as np


def request_data(date, fctime):
    csv = np.genfromtxt('data/raw/20151017/OUT.TXT', delimiter=",")
    grb = csv[:, 4:7]
    return grb


def get_speed_at_point(date, fctime, lat, lon):
    # convert date format from yyyy-mm-dd h-m-s to yyyymmddhm (remote seconds)
    date_str = date.replace('-', '').replace(' ', '').replace(':','')[:-2]
    database = "AROME_0.025_" + date_str
    cursor = connect_db('localhost','root','root',database)
    query = ('SELECT val FROM wind_speed WHERE (lat - %s < 0.024) AND (lon - %s) < 0.024 AND validtime= %s')
    cursor.execute(query,(lat, lon, fctime))
    result = cursor.fetchall()

    if len(result) == 0:
        return None

    avg_speed = 0
    for val in result:
        avg_speed = avg_speed + val[0]
    val = avg_speed / len(result)
    cursor.close()
    close_db()
    return val

def get_direction_at_point(date, fctime, lat, lon):
    # convert date format from yyyy-mm-dd h-m-s to yyyymmddhm (remote seconds)
    date_str = date.replace('-', '').replace(' ', '').replace(':','')[:-2]
    database = "AROME_0.025_" + date_str
    cursor = connect_db('localhost','root','root',database)
    query = ('SELECT val FROM wind_direction WHERE (lat - %s < 0.024) AND (lon - %s) < 0.024 AND validtime= %s')
    cursor.execute(query,(lat, lon, fctime))
    result = cursor.fetchall()

    if len(result) == 0:
        return None

    avg_speed = 0
    for val in result:
        avg_speed = avg_speed + val[0]
    val = avg_speed / len(result)
    cursor.close()
    close_db()
    return val