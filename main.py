import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#manipulate above code at your own risk

PATH="PROVIDE PATH TO THE CHROME DRIVER  YOU DOWNLOADED HERE" 
#example PATH="C:/Users/Gamex/Documents/chromedriver.exe"
requsername="PROVIDE YOUR REAL USERNAME HERE!"    #give the your username here
#example requsername="myrealusername"

#make another account a username and password ** this account will be used for logging in **
# note : if you are using private account 
# make sure to make your fake account  'follow' your real account(needed to obtain followers&following  count)!
#example username="myfakeaccountusername"
#example password="myfakeaccountpassword"
username="PROVIDE USERNAME OF FAKE ACCOUNT HERE"
password="PROVIDE PASSWORD OF FAKE ACCOUNT HERE"

if username =="" or password =="":
    print("Enter  account credentials before continuing")
    exit()

#please donot change any code below unless you know what you are doing!
followers_count=0
following_count=0
followers=[]
following=[]

driver=webdriver.Chrome(PATH)
driver.get('https://instagram.com/accounts/login')
print('acessing instagram.com ')
time.sleep(3)

driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input').send_keys(username)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input').send_keys(password)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div').click()
print('logging in as ',username)
time.sleep(4)

try:
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
    print('login info set to "not saved"')
    time.sleep(1.5)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    print('notifcations set to "not receive!"')
except:
    pass

driver.get('https://instagram.com/'+requsername)
print('searching username:',requsername)      

#checking followers now..
el=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
el.click()
followers_count=int(el.text.split(" ")[0])
print('checking followers... totalcount to parse:',followers_count)
time.sleep(1)
foll=""     
while(True):
    h1=driver.execute_script('''
    var element= document.evaluate('/html/body/div[5]/div/div/div[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    element.scroll(0,element.scrollHeight)
    return element.scrollHeight  ''')
    time.sleep(1.5)
    h2 =driver.execute_script('''
    var element= document.evaluate('/html/body/div[5]/div/div/div[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    
    return element.scrollHeight  ''')

    if h1 ==h2 :
        print("parsing ....")
        followers_names=driver.find_elements_by_class_name('wo9IH')
        for names in followers_names:
            name =names.find_elements_by_class_name('d7ByH')
            if '\n' in name[0].text:
                name=name[0].text.split('\n')[0]
                followers.append(name)
            else:
                followers.append(name[0].text)
        print('total accounts parsed : ',len(followers))
        if len(followers) >= followers_count:
            print('entire followers parsed')
        else:
            print('entire followers could not be parsed!')    
        break

driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()

# #checking following now...
el2 =driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
el2.click()
following_count=int(el2.text.split(" ")[0])
print("checking following ..totalcount:",following_count)
while(True):
    h1=driver.execute_script('''
    var element= document.evaluate('/html/body/div[5]/div/div/div[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    element.scroll(0,element.scrollHeight)
    return element.scrollHeight  ''')
    time.sleep(1.5)
    h2 =driver.execute_script('''
    var element= document.evaluate('/html/body/div[5]/div/div/div[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    
    return element.scrollHeight  ''')

    if h1 == h2 :
        print("parsing ....")
        following_names=driver.find_elements_by_class_name('wo9IH')
        for names in following_names:
            name =names.find_elements_by_class_name('d7ByH')
            if '\n' in name[0].text:
                name=name[0].text.split('\n')[0]
                following.append(name)
            else:
                following.append(name[0].text)    

        print('total accounts parsed : ',len(following))
        if len(following) >= following_count:
                print('entire following parsed')
        else:
                print('entire following could not be parsed!')    
        break

driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()

driver.quit()

l=list(set(following) - set(followers))
print("\n\nPEOPLE WHO DON'T FOLLOW ",requsername,": ",len(l))
print(l)


l=list(set(followers) - set(following))
print('\n\nPEOPLE ',requsername," DON'T FOLLOW BACK :",len(l))
print(l)

l=list(set(followers) & set(following))
print("\n\nMUTUAL :",len(l))
print(l)



