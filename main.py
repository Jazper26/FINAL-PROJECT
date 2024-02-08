import phonenumbers
from phonenumbers import geocoder
from test import number
import folium

Keys = "e61087ec5aab40af84ad23daacb57d97"

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)


from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print (carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode