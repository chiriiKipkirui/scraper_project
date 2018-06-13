from urllib import request
from bs4 import  BeautifulSoup


def products_id():
    url = "http://127.0.0.1:8000/home"
    resp = request.urlopen(url)
    soup = BeautifulSoup(resp,'lxml')
    product_name = soup.find_all("div",{"class":"product-name"})
    products = product_name.find("p")
    print(products)



products_id()
