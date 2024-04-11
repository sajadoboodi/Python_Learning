from selenium import webdriver

dr = webdriver.Chrome()

url = 'https://www.eghtesadnews.com/'
input = dr.get(url)
text = dr.page_source
print(text)
dr.close()