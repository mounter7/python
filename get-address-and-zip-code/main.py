from geopy.geocoders import Nominatim

# Create the geolocator object with a user agent
geoLocator = Nominatim(user_agent = "geoapiExercises")

def show():

    # Get the city name from the user
    place = input("Place: ")

    # Geocode the location
    location = geoLocator.geocode(place)

    # Print the geolocation details
    print(location)

    show()

show()


