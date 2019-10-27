import math
lon0,lat0=77.201854,28.635901
lat = lat0 + float(180/math.pi)*float(10000/6378137)
lon = lon0 + float(180/math.pi)*float(10000/6378137)/float(math.cos(math.pi/180.0*lat0))
print(lat,lon)
 