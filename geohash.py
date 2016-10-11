BASE_32 = "0123456789bcdefghjkmnpqrstuvwxyz"

def divide_range(value, bounded_range):
    label = 0
    for i in range(0, 30):
        bisector = (bounded_range[0] + bounded_range[1]) / 2.0
        if (value > bisector):
            label = label << 1 | 1
            bounded_range[0] = bisector
        else:
            label = label << 1
            bounded_range[1] = bisector
    print(label)
    return label

def interleave(lon_bits, lat_bits):
    lat_lon_bin = 0
    for i in range(0, 30):
        next_lon_bit = (lon_bits >> (29 - i)) & 1
        lat_lon_bin = (lat_lon_bin << 1) | next_lon_bit
        next_lat_bit = (lat_bits >> (29 - i)) & 1
        lat_lon_bin = (lat_lon_bin << 1) | next_lat_bit
    return lat_lon_bin

def encode_bits(lat_lon_bin):
    final = ''
    for i in range(0, 12):
        next_char_index = (lat_lon_bin >> (55 - i * 5)) & 31
        final += BASE_32[next_char_index]
    return final

def geohash(lat, lon):
    lat_range = [-90, 90]
    lon_range = [-180, 180]

    # find row for lon and 'label' it with binary
    lon_bits = divide_range(lon, lon_range)

    # find column for lon and 'label' it with binary
    lat_bits = divide_range(lat, lat_range)

    # interleave (alternate) the lat and lon bits
    lat_lon_bin = interleave(lon_bits, lat_bits)

    # encode the resulting number in base 32 (easier to use than a big long binary string!)
    final = encode_bits(lat_lon_bin)

    return final

hash1 = geohash(52.61911, -10.40744)
print(hash1)
