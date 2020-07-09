from time import sleep
from selenium import webdriver
import os
import time 
import datetime
from random import randint
from configparser import ConfigParser




class InstaBot:
    def __init__(self,username,password,comment1):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usuage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1325x744")
        self.driver =  webdriver.Chrome((r'C:\Users\Shrinivas\Desktop\INSTAGRAMBOT-master\chromedriver.exe'), chrome_options=chrome_options)
        self.username = username
        self.password = password
        self.comment1 = comment1
        
#login part (provide crendentials at the end of coding)
    def login(self):
        bot = self.driver 
        bot.get('https://www.instagram.com/accounts/login/')
        sleep(2)
        bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)
        print('Username entered!!')
        sleep(2)
        bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)
        print('Password entered!!')
        sleep(2)
        bot.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()
        sleep(5)
        print('LOGIN DONE')

#search by hastag (provide hashtag at end of coding)
    def SearchHashtag(self,hashtag):
        print('Like By Tag Cycle Started')
        bot = self.driver
        bot.get('https://www.instagram.com/explore/tags/' + hashtag)
        sleep(5)
        print('HASHTAG SEARCH DONE ')

#skip top posts and navigate to recent posts and like mentioned amount of posts (provide amount at the end of coding)
    def LikePhotos(self,amount1):
        
        bot = self.driver
        bot.find_element_by_class_name('v1Nh3').click() 
        sleep(10)
        a = 1  
        while a <= 9:
            sleep(3)
            bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            print('skipped post - ', a)
            a += 1
        sleep(3)  
        b = 1
        while b <= amount1:
            sleep(10)

            try:
                bot.find_element_by_class_name('fr66n').click()
                sleep(2)
                y = randint(30,50)
                print('waiting time before going to next post - ', y)
                sleep(y)
                bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
                print("liked post - ", b)
                

            except:
                sleep(5)
                print('error occured while liking post - ', b)
                y1 = randint(30,50)
                print('waiting time before going to next post - ', y1)
                sleep(y1)     
                sleep(3)
                bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()

           
            b += 1
            sleep(5) 
        print('LIKED MENTIONED AMOUNT OF POSTS')
        
#this part follows by tag (provide tag and number of accounts to follow at the  end of coding)
    def FollowByTag(self,tag,number1):
        bot = self.driver
        print('Follow By Tag Cycle Started')
        bot.get('https://www.instagram.com/explore/tags/' + tag)
        sleep(10)
        print('search by hashtaag done for follow')
        bot.find_element_by_class_name('v1Nh3').click()
        d = 1  
        while d <= 9:
            sleep(3)
            bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            print('skipped post - ', d)
            d += 1
        e = 1
        while e <= number1:
            sleep(10)
            try:
                 bot.find_element_by_class_name('oW_lN.sqdOP.yWX7d.y3zKF').click()
            except:
                print("Already Following, So Skipped Following the Post - ", e)
            sleep(5)

            try:
                bot.find_element_by_class_name('Ypffh').click()
                print('clicked comment on post - ', e)
                sleep(2)
                bot.find_element_by_class_name('Ypffh').send_keys(self.comment1)
                sleep(3)
                bot.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > button').click()
                print('comment posted on post - ', e)

            except:
                print('error occured!! ,so skipped commenting on post - ', e)    

            sleep(10)

            try:
                bot.find_element_by_class_name('fr66n').click()
                print("liked & commented & followed post ", e)
                z = randint(30,50)
                print('waiting time before going to next post - ', z)
                sleep(z)
                

            except:
                sleep(10)
                print('Error occured while Liking post - ', e)
                z1 = randint(30,50)
                print('waiting time before going to next post - ', z1)
                sleep(z1)
                
  
            sleep(3)
            bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            e += 1  
        print('FOLLOWED MENTIONED NUMBER OF USERS')    

# this part is for Idling for time between 3600 to 4200 seconds
    def Idle(self):
        bot = self.driver
        try:
            bot.get('https://www.timeanddate.com/stopwatch/')
            sleep(3)
            bot.find_element_by_css_selector('body > div.wrapper > div.main-content-div > div:nth-child(4) > section > div > div > div.tool__inner > div.tool__main.pdflexi > div.c-stopwatch > div.pdflexi.pr > button.c-stopwatch__btn.fadeIn.c-stopwatch__btn--start').click()
            x = randint(3600,4200)
            print('idling for (seconds) - ', x)
            sleep(x)

        except:
            bot.get('https://www.google.com/')
            print('Error occured in stopwatch so timer running in background!!')
            x1 = randint(3600,4200)
            print('idling for (seconds) - ', x1)
            sleep(x1)


        


file = 'config.ini'
config = ConfigParser()
config.read(file)
insta1 = InstaBot(config['instabot']['username'], config['instabot']['password'], config['instabot']['comment1'])
insta1.login()
############################################### PART 1  
stamp18 = time.localtime() 
timestamp18 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp18)     
print('STARTING CYCLE - 1 at - ',timestamp18)
insta1.SearchHashtag(config['instabot']['hashtag1'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag2'], int(config['instabot']['follows']))
stamp1 = time.localtime() 
timestamp1 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp1)
print('COMPLETED CYCLE - 1 at - ', timestamp1)
insta1.Idle()
############################################### PART 2
stamp19 = time.localtime() 
timestamp19 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp19)     
print('STARTING CYCLE - 2 at - ',timestamp19)
insta1.SearchHashtag(config['instabot']['hashtag3'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag4'], int(config['instabot']['follows']))
stamp2 = time.localtime() 
timestamp2= time.strftime("%m/%d/%Y, %H:%M:%S", stamp2)
print('COMPLETED CYCLE - 2 at - ', timestamp2)
insta1.Idle()
############################################### PART 3
stamp20 = time.localtime() 
timestamp20 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp20)     
print('STARTING CYCLE - 3 at - ',timestamp20)
insta1.SearchHashtag(config['instabot']['hashtag5'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag6'], int(config['instabot']['follows']))
stamp3 = time.localtime() 
timestamp3 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp3)
print('COMPLETED CYCLE - 3 at - ', timestamp3)
insta1.Idle()
############################################### PART 4
stamp21 = time.localtime() 
timestamp21 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp21)     
print('STARTING CYCLE - 4 at - ',timestamp21)
insta1.SearchHashtag(config['instabot']['hashtag7'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag8'], int(config['instabot']['follows']))
stamp4 = time.localtime() 
timestamp4 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp4)
print('COMPLETED CYCLE - 4 at - ', timestamp4)
insta1.Idle()
############################################### PART 5
stamp22 = time.localtime() 
timestamp22 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp22)     
print('STARTING CYCLE - 5 at - ',timestamp22)
insta1.SearchHashtag(config['instabot']['hashtag9'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag10'], int(config['instabot']['follows']))
stamp5 = time.localtime() 
timestamp5 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp5)
print('COMPLETED CYCLE - 5 at - ', timestamp5)
insta1.Idle()
############################################### PART 6
stamp23 = time.localtime() 
timestamp23 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp23)     
print('STARTING CYCLE - 6 at - ',timestamp23)
insta1.SearchHashtag(config['instabot']['hashtag11'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag12'], int(config['instabot']['follows']))
stamp6 = time.localtime() 
timestamp6 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp6)
print('COMPLETED CYCLE - 6 at - ', timestamp6)
insta1.Idle()
############################################### PART 7
stamp24 = time.localtime() 
timestamp24 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp24)     
print('STARTING CYCLE - 7 at - ',timestamp24)
insta1.SearchHashtag(config['instabot']['hashtag13'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag14'], int(config['instabot']['follows']))
stamp7 = time.localtime() 
timestamp7 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp7)
print('COMPLETED CYCLE - 7 at - ', timestamp7)
insta1.Idle()
############################################### PART 8
stamp25 = time.localtime() 
timestamp25 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp25)     
print('STARTING CYCLE - 8 at - ',timestamp25)
insta1.SearchHashtag(config['instabot']['hashtag15'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag16'], int(config['instabot']['follows']))
stamp8 = time.localtime() 
timestamp8 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp8)
print('COMPLETED CYCLE - 8 at - ', timestamp8)
insta1.Idle()
############################################### PART 9
stamp26 = time.localtime() 
timestamp26 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp26)     
print('STARTING CYCLE - 9 at - ',timestamp26)
insta1.SearchHashtag(config['instabot']['hashtag17'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag18'], int(config['instabot']['follows']))
stamp9 = time.localtime() 
timestamp9 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp9)
print('COMPLETED CYCLE - 9 at - ', timestamp9)
insta1.Idle()
############################################### PART 10
stamp27 = time.localtime() 
timestamp27 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp27)     
print('STARTING CYCLE - 10 at - ',timestamp27)
insta1.SearchHashtag(config['instabot']['hashtag19'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag20'], int(config['instabot']['follows']))
stamp10 = time.localtime() 
timestamp10 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp10)
print('COMPLETED CYCLE - 10 at - ', timestamp10)
insta1.Idle()
############################################### PART 11
stamp28 = time.localtime() 
timestamp28 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp28)     
print('STARTING CYCLE - 11 at - ',timestamp28)
insta1.SearchHashtag(config['instabot']['hashtag21'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag22'], int(config['instabot']['follows']))
stamp11 = time.localtime() 
timestamp11 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp11)
print('COMPLETED CYCLE - 11 at - ', timestamp11)
insta1.Idle()
############################################### PART 12
stamp29 = time.localtime() 
timestamp29 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp29)     
print('STARTING CYCLE - 12 at - ',timestamp29)
insta1.SearchHashtag(config['instabot']['hashtag23'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag24'], int(config['instabot']['follows']))
stamp12 = time.localtime() 
timestamp12 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp12)
print('COMPLETED CYCLE - 12 at - ', timestamp12)
insta1.Idle()
############################################### PART 13
stamp30 = time.localtime() 
timestamp30 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp30)     
print('STARTING CYCLE - 13 at - ',timestamp30)
insta1.SearchHashtag(config['instabot']['hashtag25'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag26'], int(config['instabot']['follows']))
stamp13 = time.localtime() 
timestamp13 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp13)
print('COMPLETED CYCLE - 13 at - ', timestamp13)
insta1.Idle()
############################################### PART 14
stamp31 = time.localtime() 
timestamp31 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp31)     
print('STARTING CYCLE - 14 at - ',timestamp31)
insta1.SearchHashtag(config['instabot']['hashtag27'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag28'], int(config['instabot']['follows']))
stamp14 = time.localtime() 
timestamp14 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp14)
print('COMPLETED CYCLE - 14 at - ', timestamp14)
insta1.Idle()
############################################### PART 15
stamp32 = time.localtime() 
timestamp32 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp32)     
print('STARTING CYCLE - 15 at - ',timestamp32)
insta1.SearchHashtag(config['instabot']['hashtag29'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag30'], int(config['instabot']['follows']))
stamp15 = time.localtime() 
timestamp15 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp15)
print('COMPLETED CYCLE - 15 at - ', timestamp15)
insta1.Idle()
############################################### PART 16
stamp33 = time.localtime() 
timestamp33 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp33)     
print('STARTING CYCLE - 16 at - ',timestamp33)
insta1.SearchHashtag(config['instabot']['hashtag31'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag32'], int(config['instabot']['follows']))
stamp16 = time.localtime() 
timestamp16 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp16)
print('COMPLETED CYCLE - 16 at - ', timestamp16)
insta1.Idle()
############################################### PART 17
stamp34 = time.localtime() 
timestamp34 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp34)     
print('STARTING CYCLE - 17 at - ',timestamp34)
insta1.SearchHashtag(config['instabot']['hashtag33'])
insta1.LikePhotos(int(config['instabot']['likes']))
insta1.FollowByTag(config['instabot']['hashtag34'], int(config['instabot']['follows']))
stamp17 = time.localtime() 
timestamp17 = time.strftime("%m/%d/%Y, %H:%M:%S", stamp17)
print('COMPLETED CYCLE - 17 at - ', timestamp17)
insta1.Idle()
############################################### END!!



    
    
    
    
    
    






