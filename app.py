from flask import Flask
import folium

app = Flask(__name__)

@app.route('/')
def index():
    # Create a map centered on India
    map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Centered on India
    folium.Marker([20.5937, 78.9629], popup='Center of India').add_to(map)  # Optional marker
    return map._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)