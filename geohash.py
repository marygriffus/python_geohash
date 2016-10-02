# define some variables:

# characters for encoding
BASE_32 = "0123456789bcdefghjkmnpqrstuvwxyz"

# ranges - for finding the bin a coordinate belongs to
lat_range = [-90, 90]
lon_range = [-180, 180]


def geohash(lat, lon):
    # find bin for lat and lon and 'label' it with binary

    # interleave (alternate) the lat and lon bits

    # encode the resulting number in base 32 (easier to use than a big long binary string!)

    return None
