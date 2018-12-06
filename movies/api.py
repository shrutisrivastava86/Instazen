from .models import Location, Movies
import requests, json
from geopy.geocoders import Nominatim


def get_cordinates(query):
    '''
    #need google api key to access its maps using a dummy out here
    api_key = 'AIzaSyA6DnYxRWYYXBSUXxXOslr5Rof0G1Zpcsc'

    GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

    params = {
        'address': 'san francisco',
        'sensor': 'false',
        'region': 'usa'
    }

    # Do the request and get the response data
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()

    # Use the first result
    result = res['results'][0]

    lat = result['geometry']['location']['lat']
    lng = result['geometry']['location']['lng']
    '''
    geolocator = Nominatim()
    print(query)
    if '(' in query:
        query = str(query.split('(')[1].rstrip(')'))+', San Francisco'
    else:
        query = str(query)+', San Francisco'
    location = geolocator.geocode(query)
    lat = location.latitude
    lng = location.longitude
    return{'lat': lat,'lng': lng}


def get_movie_locations(movie_name):
    locations = Movies.objects.get(name=movie_name).location_set.all()
    location_list=[]

    for location in locations:
        location_list.append(get_cordinates(location.location))
    return location_list
