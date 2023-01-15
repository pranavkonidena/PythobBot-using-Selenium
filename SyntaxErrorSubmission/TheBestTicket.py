from time import sleep, strftime
import pync
import time
from random import randint
from selenium.webdriver.common.by import By
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart


chromedriver_path = '/Users/Pranav_1/Desktop/chromedriver_win32/chromedriver.exe'


driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)



makemytrip = "https://www.makemytrip.com/flight/search?itinerary=DEL-BLR-16/01/2023&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng"

driver.get(makemytrip)

popup_close = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/span'
l = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div[2]/div/span')
l.click()

def popupclose():
    try:
        popup_close = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/span'
        l = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div[2]/div/span')
        l.click()
        print("I have clicked the popup buttton. Now time for me to sleep.zzzzzz")
        sleep(randint(25,35))
        
    except:
        pass

master_list_price = []
master_list_airline = []
master_list_depandarrtimes = []


def page_scraping():
    
   

    prices = []


    price_class = 'blackText fontSize18 blackFont white-space-no-wrap'

    price = driver.find_elements(By.XPATH , "//p[@class = 'blackText fontSize18 blackFont white-space-no-wrap']")
    prices.extend(price)
    prices_list = [value.text.replace('₹','') for value in prices if value.text != '']
    prices_list = list(map(str, prices_list))
    min_val = prices_list[0]
    min_val_index = 0
   


    airlines = []

    airlines_class = 'boldFont blackText airlineName'
    airline = driver.find_elements(By.XPATH , "//p[@class = 'boldFont blackText airlineName']")

    airlines.extend(airline)
    airlines_list = [airli.text for airli in airlines]
    airlines_list = list(map(str, airlines_list))
    

    dep_times_arrival_times = []

    dep_times_arrival_times_class = 'appendBottom2 flightTimeInfo'

    times = driver.find_elements(By.XPATH , "//p[@class = 'appendBottom2 flightTimeInfo']")
    dep_times_arrival_times.extend(times)
    dep_times_arrival_times_list = [difftimes.text for difftimes in dep_times_arrival_times]
    dep_times_arrival_times_list = list(map(str , dep_times_arrival_times_list))

    


    for i in range(len(prices_list)):
        if prices_list[i] < min_val:
            min_val = prices_list[i]
            min_val_index = i
    master_list_price.append(min_val)
    master_list_airline.append(airlines_list[min_val_index])
    master_list_depandarrtimes.append(dep_times_arrival_times_list[min_val_index])
    
    min_value_final_index = 0
    min_master_final = master_list_price[0]
    for i in range(len(master_list_price)):
        if master_list_price[i] < min_master_final:
            min_master_final = master_list_price[i]
            min_value_final_index = i
    

    
    print("The reqd flight fr u at this time is : ")
    print("Price is: ₹" + min_master_final + " Departure time of the flight: " + master_list_depandarrtimes[min_value_final_index] + " The airline is: " + master_list_airline[min_value_final_index] )
    try:
        if(master_list_price[0] == master_list_price[1]):
            pync.notify("The flight 's price hasn't changed. Please wait for a while!!!")
            time.sleep(20)
        elif(master_list_price[0] < master_list_price[1]):
            pync.notify("The flight's price has incereased. U might want to buy soon. The increase was of : " + master_list_price[1] - master_list_price[0])
            time.sleep(20)
        elif(master_list_price[0] > master_list_price[1]):
            pync.notify("The flight's price has decreased. Grab them asap!!!. The decrease was of: " + master_list_price[0] - master_list_price[1])
            time.sleep(20)
    
    except:
        pass

    

    

def make_my_trip(city_departure , city_arrival , date_dep):
    # The departure airport must be in it's abbreviated form. Eg -  Delhi - DEL
    # The same for arrival airport as well.
    # The date of departure must be of the form DD/MM/YYYY   Eg - 14/01/2023
    make_my_trip_cutsom_website = ("https://www.makemytrip.com/flight/search?itinerary=" + city_departure + "-" + city_arrival + "-" + date_dep + "&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng")
    driver.get(make_my_trip_cutsom_website)
    sleep(randint(8,10))


    # In case of a new popup
    try:
        popup_close = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/span'
        s = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div[2]/div/span')
        s.click()
    except Exception as e:
        pass
    sleep(randint(15,45))   #just in case a captcha comes again
    print("searching ...")
    page_scraping()
    try:
        popup_close = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/span'
        s = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div[2]/div/span')
        s.click()
    except Exception as e:
        pass
    sleep(20)  # For the demo, we have done it for 20 secs. We can use it for 2hrs by saying sleep(2*60*60).

    
    
    
    

 
    

   
city_dep = input("Enter the city u want to fly from: ")
city_arr = input("Enter the city u want to fly to: ")
date_depa = input("Enter the day in DD/MM/YYYY: ")    

n = int(input("Enter the amount of times u want the bot to check. (They are repeated after 2 hrs) "))
count = 0
while n > 0:
    make_my_trip(city_dep , city_arr , date_depa)
    count += 1
    
    n -= 1


print("All done!!")


driver.quit()






while(True): 
    pass


    

















