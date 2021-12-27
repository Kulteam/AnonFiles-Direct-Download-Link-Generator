from bs4 import BeautifulSoup
import requests
#import urllib2
import re



list_links=[]

file = open("link.txt", "r")

file_link = file.read()
links_to_get = file_link.split("\n")

print(links_to_get)

for index in range(len(links_to_get)): 
    req = requests.get(links_to_get[index])
    soup = BeautifulSoup(req.text, "html.parser")
    print(soup.title)
    for link in soup.findAll('a', attrs={'href': re.compile("^https://cdn-")}):
         link_direct = (link.get('href'))
         print(link_direct)
         list_links.append(link_direct)
         
with open("direct.txt", mode='w+') as f:
    f.write('\n'.join(list_links))         

file = open("direct.txt", "r")
file_link = file.read()
links_direct = file_link.split("\n")


#print(links_direct)
#for index in range(len(links_direct)):
#    r = requests.get(links_direct[index], allow_redirects=True)
#   if links_direct[index].find('/'):
#        namefile=(links_direct[index].rsplit('/', 1)[1])
#        open(namefile, 'wb').write(r.content)
#        print("Đã tải xong: "+namefile)
