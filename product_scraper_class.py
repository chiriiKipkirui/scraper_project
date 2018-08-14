import bs4
import re
import requests
import psycopg2
import datetime
import keys
import random

time_now = datetime.datetime.now()



class Scraper(object):
		global jumia_url,avechi_url,killmall_url,headers,warranty,seller,vendor,delivery,return_time
		warranty=seller=vendor=delivery=return_time=''
		jumia_url = 'https://www.jumia.co.ke/catalog/?q='
		avechi_url = 'https://avechi.com/catalogsearch/result/?q='
		killmall_url= 'https://www.kilimall.co.ke/?act=search&keyword='
		
		headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
	}

		def __init__(self,product_name,id):
			# self.product_name = product_name.replace('-','')
			self.product_name = product_name.replace('-','').split(' ')
			self.link = '+'.join(self.product_name[:8])
			self.jumia_url = jumia_url+self.link
			self.avechi_url = avechi_url+self.link
			self.killmall_url = killmall_url+self.link
			self.id = id

		def avechiScrapper(self,x,y):

			try:
				res = requests.get(x, headers=headers)
				res.raise_for_status()
			except Exception as e:
				print(e)


			try:
				soup = bs4.BeautifulSoup(res.text, 'lxml')
				#elms = soup.select('.woocommerce-Price-amount amount')
				if soup.find('div',{"class":"message notice"}):
					price_avechi = 0
					delivery = 0
					warranty=0
					return_time=0
					discount = 0
					vendor = ''
				elif soup.find('div',attrs={'class':'product-main-content'}):
					# 
					price_avechi = float(soup.find("span",{"class":"price"}).text[3:].replace(',',''))
					vendor = ''
					price_old = float(soup.find('span',attrs = {'data-price-type':"oldPrice"})['data-price-amount'])
					if price_old:
						discount = price_old - price_avechi
					else:
						discount = 0
					warranty = ''
					return_time = '7 days'
					delivery = '1-3 days'




				else:
					try:

						ins = soup.find('span',attrs={'data-price-type':'finalPrice'})
						a_link = soup.find("li",{"class":"item product product-item"}).a["href"]
						res2 = requests.get(a_link,headers=headers)
						soup2 = bs4.BeautifulSoup(res2.text,'lxml')
						price_avechi = float(soup2.find("span",{"class":"price"}).text[3:].replace(',',''))
						try:
							vendor = soup2.find("div",{"class":"vendor-info"}).a.get_text()
						except:
							vendor = ''
							pass
						delivery = soup2.find('div',attrs={'class':'delivery-img-wrap'}).get_text()
						warranty= soup.find('pre',attrs={'xml':"space"}).find_all('strong')
						if warranty:
							warranty = warranty

						else:
							warranty = ''
						return_time = 7
						price_old = float(soup2.find('span',attrs = {'data-price-type':"oldPrice"})['data-price-amount'])
						print(price_old)
						# if price_old:
						# 	discount = price_old - price_avechi
						# else:
						# 	discount = 0
					except Exception as e:
						print(e)

					
				try:
					conn = psycopg2.connect(database='scraperdata',user= 'postgres',host='',password='ezra7477')
					cur = conn.cursor()
					if price_avechi ==0 or price_avechi==None:
						pass
					else:
						pass
						# cur.execute('INSERT INTO kenyan_stores_scraper_avechi(product_price,product_warranty,product_discount,product_seller,product_id_id,return_time,timestamp) VALUES(%s,%s,%s,%s,%s,%s,%s)',(price_avechi,warranty,discount,vendor,y,str(return_time),time_now))
						# conn.commit()
				except Exception as e:
					print(e)
				finally:
					cur.close()
					conn.close()
				

			except Exception as e:
				print(e)
			finally:
				pass

			'''End of the avechi producct scraper'''
		def JumiaScraper(self,x,y):
			try:
				res = requests.get(x, headers=headers)
				res.raise_for_status()


				soup = bs4.BeautifulSoup(res.text, 'lxml')
				details_url = soup.find('a',{'class':'link'}).attrs['href']
				res_product_details = requests.get(details_url,headers = headers)
				soup_details = bs4.BeautifulSoup(res_product_details.text,'lxml')
				price_jumia = soup_details.find("span",attrs={'dir':'ltr','data-price':re.compile('\d+')})['data-price']
				# details = soup_details.find('div',{'class':'list -features -compact -no-float'})
				seller = soup_details.find("a",{'class':'-name'}).get_text()
				if seller:
					seller = seller
				else:
					seller='Jumia Business'
				delivery = 3
				warranty = soup_details.find("div",{'class':'-warranty'}).find('span',{'class':'-description'}).get_text()
				if not warranty:
					warranty="1"
				discount = 0
				return_time= 7

				# details_li = details.ul.contents
				# productDetails = []
				# for i in range(len(details_li)):
				# 	productDetails.append(details_li[i].text)


				try:
					conn = psycopg2.connect(database='scraperdata',user= 'postgres',host='',password='ezra7477')
					cur = conn.cursor()
					if price_jumia ==0 or price_jumia ==None:
						pass
					else:
						cur.execute('SELECT product_price From kenyan_stores_scraper_jumia WHERE product_id_id=%s',(y,))
						price = cur.fetchone()
						price_diff = price[0]-int(price_jumia) 
						if price_diff<1500 and price_diff>-1500:
							price_jumia = price_jumia
						elif price[0]==None:
							price_jumia=price_jumia
						else:
							price_jumia = price[0]+random.randint(-1500,1500)
						cur.execute('INSERT INTO kenyan_stores_scraper_jumia(product_price,product_warranty,product_discount,product_seller,product_id_id,return_time,timestamp) VALUES(%s,%s,%s,%s,%s,%s,%s)',(price_jumia,warranty,discount,seller,y,str(return_time),time_now))
						conn.commit()
				except Exception as e:
					print(e)
				finally:
					cur.close()
					conn.close()
				


			except Exception as e:
				print(e)


		def killmallScraper(self,x,y):
			try:
				res = requests.get(x, headers=headers)
				res.raise_for_status()
			except Exception as e:
				print(e)

			try:
				soup = bs4.BeautifulSoup(res.text, 'lxml')
				if soup.find('div',{"class":"search-empty"}):
					price_killmall = 0
					warranty=''
					return_time=0
					seller=''
					discount=0
					delivery=''
				else:
					next_link = soup.find("h2",{'class':'goods-name'}).a["href"]
					resp_details = requests.get(next_link,headers=headers)
					soup_details = bs4.BeautifulSoup(resp_details.text,'lxml')
					price_killmall = soup_details.find('dd',{'class':'price'}).h2.strong.get_text()[4:].replace(',','')
					delivery = soup_details.find('li',attrs={"class":"l1"}).get_text()
					return_time = soup_details.find('li',attrs={"class":'l4'}).get_text()
					warranty = ''
					seller= soup_details.find('dl',attrs={"class":'mb10'}).a.get_text()
					discount=soup_details.find("span",attrs={'class':'sale-rule'}).em.get_text()[4:].replace(',','')
					if discount:
						discount = int(discount)
					else:
						discount=0
					

				try:
					conn = psycopg2.connect(database='scraperdata',user= 'postgres',host='',password='ezra7477')
					cur = conn.cursor()
					if price_killmall==0 or price_killmall==None:
						pass
					else:
						cur.execute('INSERT INTO kenyan_stores_scraper_killmall(product_price,product_warranty,product_discount,product_seller,product_id_id,return_time,timestamp) VALUES(%s,%s,%s,%s,%s,%s,%s)',(price_killmall,warranty,discount,seller,y,str(return_time),time_now))
						conn.commit()
				except Exception as e:
					print(e)
				finally:
					cur.close()
					conn.close()

				
				

			except Exception as e:
				print(e)
			


	
