import requests

def get_gps_data():
    """
    Fetch GPS data using the OpenCage Geocoding API.
    Replace 'Gorakhpur' with your location or use IP-based geolocation.
    """
    api_key = "d82e5a3f317547aa9a9631fef007bae0" 
    location = "Gorakhpur" 
    url = f"https://api.opencagedata.com/geocode/v1/json?q={location}&key={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data['results']:
            lat = data['results'][0]['geometry']['lat']
            lng = data['results'][0]['geometry']['lng']
            return lat, lng
        else:
            print("No results found for the location.")
            return None
    except Exception as e:
        print(f"Error fetching GPS data: {e}")
        return None

# Fetch GPS data
gps_data = get_gps_data()

#  GPS data was fetched 
if gps_data is not None:
    latitude, longitude = gps_data
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Unable to fetch GPS data. Using default location.")
    latitude, longitude = 26.7482, 83.4465  # Default location (Gorakhpur, India)
    print(f"Default Latitude: {latitude}, Longitude: {longitude}")