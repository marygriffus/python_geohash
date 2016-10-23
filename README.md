## Starter code:

Provides constants and the necessary steps to create a geohash string.


### Step one:

Write the main program, following the steps provided in comments.

Define the 'labels' for the column and row. We will need the lon/lat value plus the range for each.

```python
# find column for lon and 'label' it with binary
lon_bits = divide_range(lon, lon_range)

# find row for lat and 'label' it with binary
lat_bits = divide_range(lat, lat_range)
```

Interleave the labels to place the point in our quadtree:

```python
# interleave (alternate) the lon and lat bits
lat_lon_bin = interleave(lon_bits, lat_bits)
```

And encode - geohashing uses a special base-32 encoding, so we can't use a library here:

```python
# encode the resulting number in base 32 (easier to use than a big long binary string!)
final = encode_bits(lat_lon_bin)
```

Finally, return the final hash:

```python
return final
```

### Step two:

Write the 'divideRange' function:
The total number of bits we will need is determined by the number of characters we want in our hash (aka, the precision) times 5 (aka, log base 2 of the encoding). We will get half of those bits from longitude, half from latitude. For this example we are creating a 12-character hash, since that is the most precise we can be given the precision problem with floats. That means we need a total of 30 bits for each longitude and latitude label ((12 * 5) / 2). I'm using 30 as a magic number here, but you could define the precision differently if you wanted!

```python
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
    return label
```

### Step three:

Write the interleave function.
For each of the bits in lonBits and latBits, we must isolate that bit and append it to our bin.

```python
def interleave(lon_bits, lat_bits):
    lat_lon_bin = 0
    for i in range(0, 30):
        next_lon_bit = (lon_bits >> (29 - i)) & 1
        lat_lon_bin = (lat_lon_bin << 1) | next_lon_bit
        next_lat_bit = (lat_bits >> (29 - i)) & 1
        lat_lon_bin = (lat_lon_bin << 1) | next_lat_bit
    return lat_lon_bin
```

### Step four:

Encode the bits: isolate each string of 5 bits in order and encode it in base-32.

```python
def encode_bits(lat_lon_bin):
    final = ''
    for i in range(0, 12):
        next_char_index = (lat_lon_bin >> (55 - i * 5)) & 31
        final += BASE_32[next_char_index]
    return final
```
