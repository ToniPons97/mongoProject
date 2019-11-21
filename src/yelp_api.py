import requests
from dotenv import load_dotenv
import os
import json
import pandas as pd

load_dotenv()
search_url = "https://api.yelp.com/v3/businesses/search"
api_key = os.getenv("YELP_API_KEY")
headers = {'Authorization': 'Bearer %s' % api_key}


def get_coords(company, city):
    params = {'term': company, 'location': city, "limit": 50}
    req = requests.get(search_url, params=params, headers=headers)
    print('The status code is {}'.format(req.status_code))

    api_response = json.loads(req.text)

    coords = []
    names = []
    city = []
    yelp_rating = []
    yelp_dict = {}
    coords_list = []
    coords_2 = []

    for i in api_response["businesses"]:
        if i["coodinates"] != None:
            coords.append(i["coordinates"])
            names.append(i["name"])
            city.append(i["location"]["city"])
            yelp_rating.append(i["rating"])

    for i in coords:
        coords_list.append([i["longitude"], i["latitude"]])

    for i in range(len(coords_list)):
        longitude = coords_list[i][0]
        latitude = coords_list[i][1]
        coords_2.append(
            {"type": "Point", "coordinates": [longitude, latitude]})

    yelp_dict = {"Name": names, "City": city, "Raiting": yelp_rating,
                 "Coordinates": coords_list, "Geometry": coords_2}

    return pd.DataFrame(yelp_dict)
