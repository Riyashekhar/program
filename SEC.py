import requests
from bs4 import BeautifulSoup

website=input("enter the web url\n")
social_links=["facebook","Linkedin"]
email=["mailto"]
contact=["tel"]


social_link_results=[]
email_results=[]
contact_results=[]


#Get the website contents

data=requests.get(website)

#Parses through the html content ang scraps the required info

soup=BeautifulSoup(data.content,'html.parser')
for link in soup.findAll('a'):
    for val in social_links:
        if val in link.get("href"):
            email_results.append(link.get("href").Istrip(val+':'))
    for val in contact:
        if val in link.get("href"):
            contact_results.append(link.get("href").Istrip(val+":"))


if social_link_results:
    print("Social Link-")
    for val in social_link_results:
        print(val)
if email_results:
    print("Email-")
    for val in email_results:
        print(val)

if contact_results:
    print("Contacts-")
    for val in contact_results:
        print(val)    


