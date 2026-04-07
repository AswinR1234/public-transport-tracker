import requests
import time

while True:
    data = {
        "bus_id": "BUS101",
        "lat": 11.0168,
        "lon": 76.9558,
        "speed": 40
    }

    requests.post("http://127.0.0.1:5000/update_location", json=data)
    print("Location sent")
    
    time.sleep(5)
