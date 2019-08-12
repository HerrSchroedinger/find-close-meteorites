import requests
import haversine

my_location = [49.45, 11.083333]
meteor_resp = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')

print(meteor_resp.status_code)
meteor_data = meteor_resp.json()

for meteor in meteor_data:
    print(meteor["name"])
    try:
        if meteor["geolocation"]:
            meteor["distance"] = int(
                haversine.calc_dist(my_location[0], my_location[1], float(meteor["geolocation"]["latitude"]),
                                    float(meteor["geolocation"]["longitude"])))
    except KeyError:
        meteor["distance"] = int(1000000)

# print(meteor_data)
sorted_meteor_data = sorted(meteor_data, key=lambda i: (i["distance"]))

for element in range(0, 10):
    print(sorted_meteor_data[element])
