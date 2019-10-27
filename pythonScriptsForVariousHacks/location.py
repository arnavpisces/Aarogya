from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="aarogya")
location = geolocator.geocode(raw_input())
print(location.address)
print((location.latitude, location.longitude))
#print(location.raw)