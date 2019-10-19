import urllib.parse
import requests

main_api = ('https://indian-cities-api-nocbegfhqg.now.sh/')
address = ('lhr')
url = main_api + urllib.parse.urlencode({'address': address})
# urlencode is gonna deal with things like if you have an
# space in your url 
# go to this url and gets response back and it's gonna get
# the response from the URL 
json_data = requests.get(url).json()
# you should get the response from the API
print(json_data)
