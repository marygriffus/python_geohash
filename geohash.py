# characters for encoding
BASE_32 = "0123456789bcdefghjkmnpqrstuvwxyz"

def geohash(lat, lon):
    lat_range = [-90, 90]
    lon_range = [-180, 180]
    # find column for lon and 'label' it with binary

    # find row for lat and 'label' it with binary

    # interleave (alternate) the lon and lat bits

    # encode the resulting number in base 32 (easier to use than a big long binary string!)

    return None

if __name__ == '__main__':
    hash1 = geohash(52.61911, -10.40744)
    print(hash1)
