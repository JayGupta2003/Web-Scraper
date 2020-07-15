#encoding - chcp 65001
import bs4 as bs
import urllib.request

link = input("Enter Your Link:")
source = urllib.request.urlopen(link).read()
soup = bs.BeautifulSoup(source,'lxml')

name = soup.find(id='productTitle').get_text()
price = soup.find(id='priceblock_ourprice').get_text()
price_beaut = float(price[2:].replace(',',''))

print(name.strip(),':',price_beaut)