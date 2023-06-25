import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.urbanladder.com/products/landry-filled-bean-bag?sku=FVSTBG53BL10639&utm_source=google&utm_medium=pla&utm_campaign=PLAhero_UL_SPECIALS&gclid=EAIaIQobChMIoJLrpbTU9AIV7INLBR2PHAabEAQYASABEgJmifD_BwE")

content = request.content
soup = BeautifulSoup(content,"html.parser")
element = soup.find("div",{ "class" : "price discounted-price" })
#div class=price

string_price = element.text.strip()

actual_price =  string_price[5:]

final_price = actual_price

if final_price < 100 :
    print("You can buy the chair ")

else:
    print("Don't buy the chair")

print(final_price)
