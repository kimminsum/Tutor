import requests
from bs4 import BeautifulSoup

URL = "https://www.google.com/search?q=%EB%82%A0%EC%94%A8&sxsrf=AJOqlzXkxhy0asDsZSIbSBUFxLIEhrWY7A%3A1673795990165&ei=lhnEY9HfCZulhwP4gJfoCg&ved=0ahUKEwjRgq7778n8AhWb0mEKHXjABa0Q4dUDCA8&uact=5&oq=%EB%82%A0%EC%94%A8&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwA0oECEEYAEoECEYYAFAAWABgjdYQaA9wAXgAgAEAiAEAkgEAmAEAyAEKwAEB&sclient=gws-wiz-serp"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

weather = soup.find("span", {"id":"wob_dc"}).get_text()

print(weather)