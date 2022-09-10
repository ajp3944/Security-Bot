import requests
import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


def check_ip(user_input):
    if(re.search(regex, user_input)):
        return True
    else:
        return False


def get_location(user_input):
    if check_ip(user_input) == False:
        return "The IP '", user_input, "' is not valid"
    ip_address = user_input
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "IP": ip_address,
        "City": response.get("city"),
        "State": response.get("region"),
        "Country": response.get("country_name"),
        "Country Population": response.get("country_population"),
        "Postal Code": response.get("postal"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "Time Zone": response.get("timezone"),
        "Currency": response.get("currency"),
        "Languages": response.get("languages"),
        "Organization Name": response.get("org")
    }
    if location_data["Country"] != "United States":
        return("For the sake of this project, we will not be showing the IP addresses outside of the U.S")
    else:
        return ("IP: " + location_data["IP"] + "\nCity: " + location_data["City"] + "\nState: " + location_data["State"] + "\nCountry: " + location_data["Country"] + 
                "\nCountry Pop.: " + str(location_data["Country Population"]) + "\nLatitude: " + str(location_data["latitude"]) + "\nLongitude: " + str(location_data["longitude"]) + "\nTime Zone: " +
                location_data["Time Zone"])
