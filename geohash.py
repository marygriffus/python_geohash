# characters for encoding
BASE_32 = "0123456789bcdefghjkmnpqrstuvwxyz"

def geohash(lat, lon):
    lat_range = [-90, 90]
    lon_range = [-180, 180]
    # find column for lat and 'label' it with binary

    # find row for lon and 'label' it with binary

    # interleave (alternate) the lat and lon bits

    # encode the resulting number in base 32 (easier to use than a big long binary string!)

    return None
