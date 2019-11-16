import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
search_url = "https://api.yelp.com/v3/businesses/search"
match_url = "https://api.yelp.com/v3/businesses/matches"
api_key = os.getenv("YELP_API_KEY")
headers = {'Authorization': 'Bearer %s' % api_key}

def get_coords(company, city):
    params = {'term' : company,'location' : city}
    req=requests.get(search_url, params=params, headers=headers)
    print('The status code is {}'.format(req.status_code))

    api_response = json.loads(req.text)

    coords = []

    for i in api_response["businesses"]:
        coords.append(i["coordinates"])

    print(api_response)

    return coords




print(get_coords("Rockstar Games", "New York City"))
