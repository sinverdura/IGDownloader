from selenium import webdriver
import time
import getpass
import urllib.request
#from selenium.webdriver.common.keys import Keys

list_urls=[] #se crea una lista vacia, para almacenar más tarde las URLs
f=open('C:\\Users\\ogome\\Desktop\\Python\\WS_InstagramDownloader\\links.txt','r')
f_lines=f.readlines()   #f_lines es la lista donde se guradan los links que 
                        #vienen en la lista

username_xpath='//html//body//div[1]//section//main//article//div[2]//div[1]//div//form//div//div[1]//div//label//input'
password_xpath='//html//body//div[1]//section//main//article//div[2]//div[1]//div//form//div[3]//div//label//input'

#loginbutton_xpath='//html//body//div[1]//section//main//article//div[2]//div[1]//div//form//div[4]//button'
#ahorano_xpath='//html//body//div[4]//div//div//div[3]//button[2]'

#password=getpass.getpass(prompt='your IGpswrd, please: ')
#number_to_save=int(input('consecutive number to your 1st video: '))
#base_ar="C:\\Users\\ogome\\Videos\\Blue Shark\\"
# for x in range(len(f_lines)): #se crea la lista de URLs
#     i=number_to_save+x
#     name_video=base_ar+str(i)+'.mp4'
#     list_urls.append(name_video)
# print('Automation working...')

# profile = webdriver.FirefoxProfile() #for mute firefox
# profile.set_preference("media.volume_scale", "0.0") #for mute firefox
browser=webdriver.Firefox(executable_path=r"C:\\Users\\ogome\\Desktop\\Python\\WS_InstagramDownloader\\geckodriver-v0.26.0-win64\\geckodriver.exe") #,firefox_profile=profile) 

browser.set_window_position(0,40)
browser.set_window_size(1366/2,(768-40)) 

time.sleep(2)
browser.get("https://www.instagram.com")