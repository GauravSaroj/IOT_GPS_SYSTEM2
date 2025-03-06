import firebase_admin
from firebase_admin import credentials, db
import time
from geopy.distance import geodesic
import folium
import webbrowser

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-gps-system-1-default-rtdb.firebaseio.com/'  # Replace with your actual database URL
})

# Store the starting location (initialize as None)
starting_location = None

# Create a folium map centered at the default location
m = folium.Map(location=[26.7482, 83.4465], zoom_start=15)  # Default location (Gorakhpur, India)

def send_to_firebase(lat, lng):
    global starting_location, m

    # If starting location is not set, set it to the current location
    if starting_location is None:
        starting_location = (lat, lng)
        print(f"Starting location set to: {starting_location}")
        # Add a marker for the starting location
        folium.Marker(
            location=starting_location,
            popup="Starting Point",
            icon=folium.Icon(color="green")
        ).add_to(m)

    # Calculate the distance from the starting location
    current_location = (lat, lng)
    distance = geodesic(starting_location, current_location).meters  # Distance in meters

    # Log the distance
    print(f"Distance from starting location: {distance:.2f} meters")

    # Trigger an alert if the distance exceeds 500 meters
    if distance > 500:
        print("Alert: You have moved more than 500 meters from your starting point!")

    # Send data to Firebase
    ref = db.reference('gps_data')
    ref.set({
        'latitude': lat,
        'longitude': lng,
        'timestamp': int(time.time()),
        'distance_from_start': distance  # Optional: Store distance in Firebase
    })

    # Update the map with the current location
    folium.Marker(
        location=current_location,
        popup=f"Current Location\nDistance: {distance:.2f} meters",
        icon=folium.Icon(color="blue")
    ).add_to(m)

    # Save the map to an HTML file and open it in the browser
    m.save("real_time_map.html")
    webbrowser.open("real_time_map.html")

# Simulate GPS updates (replace with real-time GPS data)
def simulate_gps_updates():
    # Example: Simulate movement by changing coordinates
    locations = [
        (26.7482, 83.4465),  # Starting point (Gorakhpur, India)
        (26.7500, 83.4500),  # Slight movement
        (26.7600, 83.4600),  # Further movement (> 500 meters)
    ]

    for lat, lng in locations:
        print(f"\nUpdating location to: ({lat}, {lng})")
        send_to_firebase(lat, lng)
        time.sleep(10)  # Wait for 10 seconds before the next update

# Run the simulation
simulate_gps_updates()