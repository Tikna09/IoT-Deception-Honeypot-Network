import requests
import folium

ip = "8.8.8.8"

response = requests.get(f"http://ip-api.com/json/{ip}")
data = response.json()

lat=data["lat"]
lon=data["lon"]
country=data["country"]

m = folium.Map(loction=[lat, lon], zoom_start=5)
folium.Marker([lat, lon], popup=f"Attacker IP: {ip} | Country:{country} ").add_to(m)
m.save("attack_map.html")

print("Map   saved as attack_map.html")
