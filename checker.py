import psycopg2
import os
import keys
import product_scraper



with open('products.txt','r')as f:
	contents = f.read()

	f.close()
prod_names= contents.split(',')


try:
	conn = psycopg2.connect(database='scraper',user='postgres',password=keys.password)
	cur = conn.cursor()
	cur.execute('delete from kenyan_stores_scraper_products')
	con.commit()
	print("deleted")
	
	
	





except Exception as e:

	print(e)
finally:
        cur.close()
        conn.close()
##print(names_test)


##for x in range(len(ids)):
##    prod_name = names_test[x]
##    prod_id = ids[x]
##    item  =product_scraper.Scraper(prod_name,prod_id)
##    item.avechiScrapper(item.avechi_url,item.id)
##    item.killmallScraper(item.killmall_url,item.id)
##    item.JumiaScraper(item.jumia_url,item.id)
##    
##       


