import requests
from bs4 import BeautifulSoup
url="https://www.bbc.com/news"
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
headlines=soup.find_all('h3')
print("News Headlines:")
for i, headline in enumerate(headlines[:10],1):
    print(f"{i}.{headline.get_text(strip=True)}")
    
