import requests

"""
response = requests.get(url="http://api.open-notify.org/iss-now.json") # End point URL
response.raise_for_status()
data = response.json()["iss_position"]
lon = data["longitude"]
lat = data["latitude"]

position = (lon, lat)
print(position)
"""