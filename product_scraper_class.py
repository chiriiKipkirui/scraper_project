import bs4
import re
import requests
import psycopg2
import time
import keys

time_now = time.time()



class Scraper(object):
		global jumia_url,avechi_url,killmall_url,headers
		jumia_url = 'https://www.jumia.co.ke/catalog/?q='
		avechi_url = 'https://avechi.com/catalogsearch/result/?q='
		killmall_url= 'https://www.kilimall.co.ke/?act=search&keyword='
		
		headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
	}

		def __init__(self,product_name,id):
			self.product_name = product_name.replace('-','')
			self.link = self.product_name[:25].replace(' ','+')
			self.jumia_url = jumia_url+self.product_name[:10]
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
				else:

					ins = soup.find('span',attrs={'data-price-type':'finalPrice'})
					a_link = soup.find("li",{"class":"item product product-item"}).a["href"]
					res2 = requests.get(a_link,headers=headers)
					soup2 = bs4.BeautifulSoup(res2.text,'lxml')
					price_avechi = float(soup2.find("span",{"class":"price"}).text[3:].replace(',',''))
					try:
						vendor = soup2.find("div",{"class":"vendor-info"}).next.next.string
					except:
						vendor = ''
						pass
					delivery = '24 hours'
					warranty=""
					return_time = 7
					discount=0
					print(price)
				try:
					conn = psycopg2.connect(database='sdd3k5k07r0pec2',user= 'skbfthymdatfrb',host='ec2-54-204-2-26.compute-1.amazonaws.com',password='7380d6d5ad9182a7a79ae581583828814b746ac23da120b7b1404337a3814b10')
					cur = conn.cursor()
					if price_avechi ==0 or price_avechi==None:
						pass
					else:
						cur.execute('INSERT INTO kenyan_stores_scraper_avechi(product_price,product_warranty,product_discount,product_seller,product_id_id,return_time,timestamp) VALUES(%s,%s,%s,%s,%s,%s,%s)',(price_avechi,warranty,discount,vendor,y,str(return_time),time_now))
						conn.commit()
				except Exception as e:
					print(e)
				finally:
					cur.close()
					conn.close()
				

			except Exception as e:
				print(e)
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
				details = soup_details.find('div',{'class':'list -features -compact -no-float'})
				seller = soup_details.find("a",{'class':'-name'}).get_text()
				delivery = 3
				warranty = soup_details.find("div",{'class':'-warranty'}).find('span',{'class':'-description'}).get_text()
				discount = 0
				return_time= 7

				details_li = details.ul.contents
				productDetails = []
				for i in range(len(details_li)):
					productDetails.append(details_li[i].text)


				try:
					conn = psycopg2.connect(database='sdd3k5k07r0pec2',user= 'skbfthymdatfrb',host='ec2-54-204-2-26.compute-1.amazonaws.com',password='7380d6d5ad9182a7a79ae581583828814b746ac23da120b7b1404337a3814b10')
					cur = conn.cursor()
					if price_jumia ==0 or price_jumia ==None:
						pass
					else:
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
				else:
					next_link = soup.find("h2",{'class':'goods-name'}).a["href"]
					resp_details = requests.get(next_link,headers=headers)
					soup_details = bs4.BeautifulSoup(resp_details.text,'lxml')

					price_killmall = soup_details.find('dd',{'class':'price'}).h2.strong.get_text()[4:].replace(',','')
					delivery = 3
					return_time =  7
					warranty = ''
					seller= ''
					discount=0
					
				try:
					conn = psycopg2.connect(database='sdd3k5k07r0pec2',user= 'skbfthymdatfrb',host='ec2-54-204-2-26.compute-1.amazonaws.com',password='7380d6d5ad9182a7a79ae581583828814b746ac23da120b7b1404337a3814b10')
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


	
