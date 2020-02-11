import cv2
import os
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
#enter browser name
browser = webdriver.Firefox(executable_path = "E:/geckodriver")
#enter link from page
browser.get("https://duckduckgo.com")
soup = bs(browser.page_source,"html.parser")
element = soup.findAll("span",{"class":"tile--img__media__i"})
import os
os.mkdir("images")
count = 1
for i in range(1,len(element)):
    a = element[i].find("img").attrs["src"].split("//external-content")[1]
    r = requests.get("https://www"+a)
    f = open("./body_images/"+str(count)+".jpg","wb")
    f.write(r.content)
    f.close()
    count = count+1
    print("image "+str(count)+" saved")
