import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

url="https://www.meudon.fr/"

response = requests.get(url)

content = response.content
print(content)

soup = BeautifulSoup(content,'html')

h2 = soup.find('h2')
print(h2)
