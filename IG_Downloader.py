from selenium import webdriver
#To work in new laptop
from selenium.webdriver.common.by import By
import time
import getpass
import urllib.request
#from selenium.webdriver.common.keys import Keys

list_urls=[] #se crea una lista vacia, para almacenar más tarde las URLs
f=open('G:\\My Drive\\WS_InstagramDownloader\\links.txt','r')
f_lines=f.readlines()   #f_lines es la lista donde se guradan los links que 
                        #vienen en la lista

username_xpath='//html//body//div[1]//section//main//article//div[2]//div[1]//div//form//div//div[1]//div//label//input'
password_xpath='//html//body//div[1]//section//main//article//div[2]//div[1]//div//form//div[3]//div//label//input'

#loginbutton_xpath='//html//body//div[1]//section//main//article//div[2]//div[1]//div//form//div[4]//button'
#ahorano_xpath='//html//body//div[4]//div//div//div[3]//button[2]'

password=getpass.getpass(prompt='your IGpswrd, please: ')
number_to_save=int(input('consecutive number to your 1st video: '))
base_ar="G:\\My Drive\\WS_InstagramDownloader\\downloaded_videos\\"
for x in range(len(f_lines)): #se crea la lista de URLs
    i=number_to_save+x
    name_video=base_ar+str(i)+'.mp4'
    list_urls.append(name_video)
print('Automation working...')

profile = webdriver.FirefoxProfile() #for mute firefox
profile.set_preference("media.volume_scale", "0.0") #for mute firefox
# browser=webdriver.Firefox(executable_path=r"G:\\My Drive\\WS_InstagramDownloader\\geckodriver-v0.26.0-win64\\geckodriver.exe", firefox_profile = profile) 
browser=webdriver.Firefox(executable_path=r"G:\\My Drive\\WS_InstagramDownloader\\geckodriver-v0.31.0-win64\\geckodriver.exe", firefox_profile = profile) 
browser.set_window_position(0,0)
browser.set_window_size(1366/2,(768)) #1366 x 768 my actual desktop size 

#time.sleep(2)
browser.get("https://www.instagram.com")
time.sleep(2)
# browser.find_element_by_xpath("//input[@name=\"username\"]").send_keys('sinverdura')
browser.find_element("xpath", "//input[@name=\"username\"]").send_keys('sinverdura')
# browser.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
browser.find_element("xpath", "//input[@name=\"password\"]").send_keys(password)
# browser.find_element_by_xpath('//button[@type="submit"]').click()
browser.find_element("xpath", '//button[@type="submit"]').click()
time.sleep(10) #incremento este valor a 10, estaba en 6 s.  
# browser.find_element_by_xpath("//button[contains(text(), 'Ahora no')]").click()
browser.find_element("xpath", "//button[contains(text(), 'Ahora no')]").click()
for (a,b) in zip(f_lines,list_urls): #a==URL per vid, b==acces rute per vid
    browser.get(a)
    time.sleep(1)
    # video_url = browser.find_element_by_tag_name('video').get_attribute('src')
    # video_url = browser.find_element('video').get_attribute('src')
    video_url = browser.find_element(By.TAG_NAME, "video").get_attribute('src')
    browser.get(video_url)
    time.sleep(1)
    urllib.request.urlretrieve(video_url,b)
    print("video ready! @ " + b)
    print("by oscargxmxz, 2020.")
browser.quit()

print('Script finalizado, '+ str(len(f_lines))+' video(s) descargados.')


#To make an executable file:
#pyinstaller --onefile --console --icon=insta.ico IG_Downloader.py