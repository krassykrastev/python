import phonenumbers
from phonenumbers import geocoder, timezone, carrier

import folium
from opencage.geocoder import OpenCageGeocode

number = input("Enter the phone number with country code: ")
phoneNumber = phonenumbers.parse(number)
key = "676e130541ca4576b445fa7990467620" #opencage API

your_location = geocoder.description_for_number(phoneNumber, 'en')
print(f'Location: {your_location}')

timezone = timezone.time_zones_for_number(phoneNumber)
print(f'Timezone: {timezone}')

your_carrier = carrier.name_for_number(phoneNumber, 'en')
print(f'Carrier: {your_carrier}')

# Using opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(key)
query = str(your_location)
results = geocoder.geocode(query)

# Assigning the latitude and longitude values to the lat and lng variables
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

# Getting the map for the given latitude and longitude
myMap = folium.Map(loction=[lat, lng], zoom_start=9)

# Adding a Marker on the map to show the location name
folium.Marker([lat, lng], popup=your_location).add_to(myMap)

# save map to html file to open it and see the actual location in map format
myMap.save("Location.html")
