import requests
import bs4
import re
import psycopg2
import os
import keys
import time
import product_scraper_class


ids = []
names_test = []

try:
    conn = psycopg2.connect(database='scraper',user='postgres',password=keys.password)
    cur = conn.cursor()
    cur.execute('select id,prod_name from kenyan_stores_scraper_products')
    products_list= cur.fetchall()
    for row in products_list:
        ids.append(row[0])
        names_test.append(row[1])
        
  
        

except Exception as e:

    print(e)
finally:
    cur.close()
    conn.close()
##print(names_test)


for x in range(len(ids)):
   prod_name = names_test[x]
   prod_id = ids[x]
   item  =product_scraper.Scraper(prod_name,prod_id)
   item.avechiScrapper(item.avechi_url,item.id)
   item.killmallScraper(item.killmall_url,item.id)
   item.JumiaScraper(item.jumia_url,item.id)
   
      


