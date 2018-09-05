#Q-1 Use the "https://api.forismatic.com/api/1.0/" api to get random quotes using the correct endpoints.
import requests
parameters = {"method": "getQuote", "format": "json", "key": 457653, "lang":"en" }
response=requests.get("http://api.forismatic.com/api/1.0/", params=parameters)
data=response.json()
print(data["quoteText"])
