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
    conn = psycopg2.connect(database='sdd3k5k07r0pec2',user= 'skbfthymdatfrb',host='ec2-54-204-2-26.compute-1.amazonaws.com',password='7380d6d5ad9182a7a79ae581583828814b746ac23da120b7b1404337a3814b10')
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
   
      


