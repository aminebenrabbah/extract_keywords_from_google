from selenium import webdriver
from selenium.webdriver.common.by import By
import time



web = webdriver.Chrome()



web.get('https://www.google.com/')


#this function for save data 
def save(nom_file ,a_or_write_or_read,text):
    file = open(nom_file+'.txt',a_or_write_or_read)
    file.write(text+str('\n'))
    file.close()

#this function for git keywords from google
def get_keyword_from_search(web,keyword_for_file):
    for number in range(1,11):
        #this for git word
        word = web.find_element(By.XPATH , value = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[4]/div[2]/div[1]/div/ul/li['+str(number)+']/div/div[2]/div[1]/div[1]/span').text
        #this for save keywords
        save(keyword_for_file,'a',word)
        print(word)



def get_keyword(web):
    letters = ['a' ,'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z','y']
    #keyword for search
    word = input('give me   keyword for search')
    keyword_for_file = input('give name for save data ')
    
    for letter in letters:
        #add letter to word
        word_and_letter = word + ' '+ letter
        #send word to input
        time.sleep(2)
        web.find_element(By.ID, value = 'APjFqb').send_keys(word_and_letter)
        time.sleep(2)
        #this function for save keywords
        get_keyword_from_search(web,keyword_for_file)
        time.sleep(2)
        web.find_element(By.XPATH , value = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/span').click()
        
        
get_keyword(web)
