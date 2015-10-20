import pygrib

path = "../data/raw/20151017/wind.grb"
grbs = pygrib.open(path)

def print_inventory():
    for grb in grbs:
        print grb

def print_first_grib_msg(match_name):
    grb = grbs.select(name=match_name)[0]

def get_msg_from_name(match_name, fcst):
    array = grbs.select(name=match_name)
    if fcst >= len(array):
        return "error"
    grb = array[fcst]
    return grb

def get_idx_from_given_lat(lats,lat):
    idx = 0
    for i in lats:
        if i[0] == lat:
            return idx
        idx = idx + 1

    return "not found"

def get_idx_from_given_lon(lons,lon):
    idx = 0
    for i in lons[0]:
        if abs(i - lon) <= 0.025:
            return idx
        idx = idx + 1

    return "not found"

def get_value_at_lat_lon(grb, lat, lon):
    data = grb.values
    lats,lons = grb.latlons()
    # print lats
    idx_lat = get_idx_from_given_lat(lats,lat)
    print idx_lat
    idx_lon = get_idx_from_given_lon(lons, lon)
    print idx_lon
    return data[idx_lat][idx_lon]

def main():
    print_inventory()
    # grb = get_msg_from_name("Wind speed (gust)",0)
    grb = grbs[2]
    print grb
    # grb = get_msg_from_name("Rain precipitation rate",0)
    vl = get_value_at_lat_lon(grb, 53.000, -8)
    print "%f" % vl

if __name__ == '__main__':
    main()