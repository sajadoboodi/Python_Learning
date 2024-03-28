import requests

req = requests.get('https://www.mehrnews.com/rss')
print(req)
#print(req.text)

reqall = requests.get('https://eghtesaad24.ir/fa/rss/allnews')
print(reqall)
#print(reqall.text)

req_eco = requests.get('https://eghtesaad24.ir/fa/rss/4/mostvisited')
print(req_eco)
#print(req_eco.text)

eghteda_news = requests.get('https://www.eghtesadnews.com/feeds/')
print(eghteda_news)
print(eghteda_news.text)