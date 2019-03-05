from lxml import html
import requests

url = "http://youtube.com"
page = requests.get(url)

tree = html.fromstring(page.text)
print tree
