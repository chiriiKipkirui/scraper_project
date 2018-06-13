import requests
from bs4 import BeautifulSoup
import psycopg2
from bs4 import NavigableString
import keys
from itertools import *


urls_mobiles = ["https://www.jumia.co.ke/mobile-phones/"]
audio_tvs_urls = ["https://www.jumia.co.ke/video-audio/"]
computers_urls = ["https://www.jumia.co.ke/computers/"]
def gen_next_url(url):
	audio_url = "https://www.jumia.co.ke/video-audio/"
	comp_url = "https://www.jumia.co.ke/computers/"
	for i in range(24):
		urls_mobiles.append(url+"?page="+str(i+2))
		audio_tvs_urls.append(audio_url+"?page="+str(i+2))
		computers_urls.append(comp_url+"?page="+str(i+2))

gen_next_url("https://www.jumia.co.ke/mobile-phones/")
global image,features,clean_features,prod_rating,name

except_url = []
image= ''
features = []
clean_features = []
prod_rating = ''
name = ''
with open('products.txt','r')as f:
	contents = f.read()

	f.close()
prod_names= contents.split(',')

product_url_link = []
def get_products(url):
	headers = {
	        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
	    }
	try:
		product_response = requests.get(url,headers=headers)
		soup = BeautifulSoup(product_response.text,'lxml')
	except Exception as e:
		print(e)
	try:
		product_holder = soup.find_all("div",{"class":"sku -gallery"})
		for product in product_holder:
			#get's the product urls
			product_links = product.find_all("a",{"class":"link"})
			for link in product_links:
				product_url_link.append(link["href"])
	except Exception as e:
		print(e)

for url in chain(audio_tvs_urls,computers_urls,urls_mobiles): #concatinate (computers_urls+audio_tvs_urls+
	get_products(url)

def get_product_details(url):
	headers = {
	        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
	    }
	if url in except_url:
	    	pass
	else:

		try:
			product_details = requests.get(url,headers=headers)
			soup_details = BeautifulSoup(product_details.text,'lxml')
		except Exception as e:
			print(e)
		try:
			name_holder = soup_details.find("h1",{"class":"title"})
			if name_holder:
				name = name_holder.text

				for i in range(len(prod_names)):

					if prod_names[i]  not in name:
						continue
					else:
                                                name = name
						image_holder = soup_details.find("img",{"id":"productImage"})
						print(url)
						if image_holder :
							image = image_holder["data-src"]
							print(image)
						else:
							pass
					#name holders
						
						#ratings container
						ratings_holder = soup_details.find("div",{"class":"container"})
						if ratings_holder:
							ratings = ratings_holder.span.text
							if ',' in ratings:
								rating,by = ratings.split(',')
							else:
								rating = ratings
							prod_rating = int(rating)
							try:
								features_holder = soup_details.find_all("div",{"class":'list -features'})
								if(features_holder):
									li_container = features_holder[0]
									if li_container.ul:
											for li in li_container.ul:
												if isinstance(li,NavigableString):
													features.append(li)

												elif li.strong:
													features.append(li.strong.text)
												elif li.text:
													features.append(li.text)
												else:
													pass
									elif li_container.p:
											for li in li_container.p:
												if li.text:
													features.append(li.text)
												elif isinstance(li,NavigableString):
													features.append(li)
												elif li.strong:
													features.append(li.strong.text)
												else:
													pass
									elif li_container.ol:
											for li in li_container.ol:
												if li.text:
													features.append(li.text)
												elif isinstance(li,NavigableString):
													features.append(li)
												elif li.strong:
													features.append(li.strong.text)
												else:
													pass
									elif li_container.p and li_container.ul:
										for li in li_container.p:
												if li.text:
													features.append(li.text)
												elif isinstance(li,NavigableString):
													features.append(li)
												elif li.strong:
													features.append(li.strong.text)
												else:
													pass


									else:
											pass

								else:
									pass
							except Exception as e:
								print(e)

						break
				for li in features:
					clean_features.append(li.encode("utf-8"))
			try:
				conn = psycopg2.connect(database='sdd3k5k07r0pec2',user= 'skbfthymdatfrb',host='ec2-54-204-2-26.compute-1.amazonaws.com',password='7380d6d5ad9182a7a79ae581583828814b746ac23da120b7b1404337a3814b10')
				cur = conn.cursor()
				try:
					pass

					cur.execute("""INSERT INTO kenyan_stores_scraper_products(product_name,product_image,product_rating,product_key_features)
								VALUES(%s,%s,%s,%s)""",(name,image,prod_rating,clean_features))
					
				except Exception as e:
					print(e)
				conn.commit()
				cur.close()
				conn.close()

			except Exception as e:
				print(e)
			
					
		except Exception as e:
			print(e)
		#product specs.....



for link in product_url_link:
	get_product_details(link)




