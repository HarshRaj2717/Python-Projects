#################################################
# API keys can be hidden usin env variables : https://www.udemy.com/course/100-days-of-code/learn/lecture/21326814
#################################################

import requests

try:
    # Getting ISS data.
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_data = iss_response.json()

    # Printing live location of ISS in langitudes and longitudes.
    print(f'''Location of ISS :
        Longitude: {iss_data["iss_position"]["longitude"]}
        Latitude: {iss_data["iss_position"]["latitude"]}''')
    
    # Getting live location(from IP) data.
    api_key = "f0723f31952b44e1a9d3e69614654434"
    abstractapi_param = {"api_key":api_key}
    abstractapi_response = requests.get("https://ipgeolocation.abstractapi.com/v1/", params=abstractapi_param)
    abstractapi_response.raise_for_status()

    abstractapi_data = abstractapi_response.json()

    # Printing live location of ISS in langitudes and longitudes.
    print(f'''Your location :
        Longitude: {abstractapi_data["longitude"]}
        Latitude: {abstractapi_data["latitude"]}''')

    # Check if ISS overhead.
    print("Is ISS overhead?", end="\n        ")

    if abstractapi_data["longitude"]-5 < float(iss_data["iss_position"]["longitude"]) < abstractapi_data["longitude"]+5 \
        and abstractapi_data["latitude"]-5 < float(iss_data["iss_position"]["latitude"]) < abstractapi_data["latitude"]+5:
        print("YES")
    else:
        print("NO")

except Exception as e:
    print("Error:", e)
