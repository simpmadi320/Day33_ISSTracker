import smtplib
import requests
from datetime import datetime
import time

MY_LAT = 43.372971
MY_LON = -80.975090

MY_EMAIL = "simpmadi320@gmail.com"
MY_KEY = "wipn qdsz tdqn hiqc"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json") # End point URL
    response.raise_for_status()
    data = response.json()["iss_position"]
    lon = float(data["longitude"])
    lat = float(data["latitude"])

    position = (lon, lat)
    print(position)

    if MY_LAT-5 <= lat <= MY_LAT+5 and MY_LON-5 <= lon <= MY_LON+5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0 # optional
    }
    response = requests.get("https://api.sunrise-sunset.org/json", parameters)
    response.raise_for_status()
    data = response.json()["results"]
    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_KEY)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
        )