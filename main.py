from bs4 import BeautifulSoup
import requests
#import urllib2
import re
import random
import wget
import time



list_links=[]

file = open("link.txt", "r")

file_link = file.read()
links_to_get = file_link.split("\n")

#print(links_to_get)

for index in range(len(links_to_get)): 
    req = requests.get(links_to_get[index])
    soup = BeautifulSoup(req.text, "html.parser")
   # print(soup.title)
    for link in soup.findAll('a', attrs={'href': re.compile("^https://cdn-")}):
         link_direct = (link.get('href'))
         print("Download file of link: "+links_to_get[index])
         filename=wget.download(link_direct)
         print("Done download filename: "+filename)
         sleep_time=random.randint(5,15)
         print("Pause until next download for %s s" %sleep_time )
         time.sleep(sleep_time)
         
         
