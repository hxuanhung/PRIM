import numpy as np


def request_data(date, fctime):
    csv = np.genfromtxt('data/raw/20151017/OUT.TXT', delimiter=",")
    grb = csv[:, 4:7]
    return grb


def get_speed_at_point(date, fctime, lat, lon):
    data = request_data(date, fctime)
    val = get_value_at_lat_lon(data, lat, lon)

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


    # def main():
    #     # print_inventory()
    #     # # grb = get_msg_from_name("Wind speed (gust)",0)
    #     # grb = grbs[2]
    #     # print grb
    #     # # grb = get_msg_from_name("Rain precipitation rate",0)
    #     # vl = get_value_at_lat_lon(grb, 53.000, -8)
    #     # print "%f" % vl
    #     # test = np.array([[1.2,2,3],[2,3,4],[1.2,3,4]])
    #     # row = test[abs(test[:,0]-1)<0.14]
    #     # col = row[row[:,1]==2]
    #     # print row
    #     # print col
    #     # print col[0][2]
    #     get_speed(20151017,5,1.177,40.8)
    #
    # if __name__ == '__main__':
    #     main()
