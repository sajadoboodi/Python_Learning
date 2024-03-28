import requests

req = requests.get('https://api.stockdata.org/v1/data/quote?symbols=AAPL%2CTSLA%2CMSFT&api_token=my_token')
my_req = req.json()
print(my_req)

for item in my_req['data']:  # Replace 'data' with the actual key if it's different
    print(f"Name: {item.get('name', 'N/A')}, Price: {item.get('price', 'N/A')}, Day_high: {item.get('day_high', 'N/A')}, Data & Time: {item.get('previous_close_price_time', 'N/A')}")
