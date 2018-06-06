#Robert Thomas June.6th/2018 taken from lesson at clean code camp: https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
#import Libraries
import urllib 
from bs4 import BeautifulSoup


#specifiy url
car_list = 'https://www.kijiji.ca/b-cars-trucks/nova-scotia/honda-civic-2013__-new__used/c174l9002a54a1000054a68a49?price=6000__11000&kilometers=__100000&transmission=1'

# query the page
req = urllib.request.Request(car_list)
page = urllib.request.urlopen(req)

soup = BeautifulSoup(page, 'html.parser')


elements = soup.find_all('div', class_="title price location details".split())
print("\n".join("{}".format(el.get_text()).strip() for el in elements))
