import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()


url = "https://api.yelp.com/v3/businesses/search"



api_key = os.getenv("YELP_API_KEY")
headers = {'Authorization': 'Bearer %s' % api_key}
params = {'term':'Starbucks','location':'New York City'}
req=requests.get(url, params=params, headers=headers)
print('The status code is {}'.format(req.status_code))
print(json.loads(req.text))
