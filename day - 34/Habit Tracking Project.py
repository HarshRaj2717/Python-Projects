import requests
from datetime import datetime

USERNAME = "trialusername1212"
TOKEN = input("Enter token(passcode): ")
GRAPH_ID = "graph1"


def create_user():
    try:
        user_json = {
            "token":TOKEN,
            "username":USERNAME,
            "agreeTermsOfService":"yes",
            "notMinor":"yes"
        }
        pixela_response = requests.post(url="https://pixe.la/v1/users", json=user_json)
        print(pixela_response.text)
        pixela_response.raise_for_status()

    except Exception as e:
        print("Error:", e)


def create_graph():
    try:
        graph_json = {
            "id":GRAPH_ID,
            "name":"Cycling Graph",
            "unit":"km",
            "type":"int",
            "color":"sora"
        }
        pixela_response = requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs",headers={"X-USER-TOKEN":TOKEN}, json=graph_json)
        print(pixela_response.text)
        pixela_response.raise_for_status()


    except Exception as e:
        print("Error:", e)


def create_pixel():
    try:
        pixel_json = {
            "date":datetime.now().strftime("%Y%m%d"),
            "quantity":input("Enter pixel quantity as an int: ")
        }
        pixela_response = requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}",headers={"X-USER-TOKEN":TOKEN}, json=pixel_json)
        print(pixela_response.text)
        pixela_response.raise_for_status()


    except Exception as e:
        print("Error:", e)


# create_user()
# create_graph()
create_pixel()
