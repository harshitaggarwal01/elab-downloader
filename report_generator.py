from selenium import webdriver
import os
import time

browser = webdriver.Chrome("C:/Users/Harshit/Downloads/chromedriver_win32/chromedriver.exe") 
browser.maximize_window() 

#URL for eLab
browser.get('https://care.srmist.edu.in/srmktroops/login') 

#Your username and password
username = "username"
password = "password"
  
usr = browser.find_element_by_name('username')
usr.send_keys(username)

pwd = browser.find_element_by_name('password')
pwd.send_keys(password)

browser.find_elements_by_class_name('mat-button-wrapper')[1].click()

time.sleep(10)

browser.find_element_by_class_name('courseName').click()

#set the URL for the question you want to start with
browser.get('https://care.srmist.edu.in/srmktroops/student/solve/2411111')

time.sleep(10)

"""
!!!! BUGS !!!!
->Gets stuck if encounters an unsuccessful evaluation 
->Gets stuck if encounters a problem with single test case
!!! WARNINGS !!!
->Change the sleep time according to the internet speed
"""
A=[17,26,29,37,43,46,47,56,91,94] # Questions numbers which are not evaluated (question number on elab -1)

for x in range(100):

    if x not in A:

        browser.find_elements_by_class_name("mat-button-wrapper")[9].click()
        time.sleep(10)
        path, dirs, files = next(os.walk("D:/CLICK HERE/python/oodp_reports/reports")) # set path for download
        file_count_1 = file_count_2 = len(files)
        while (file_count_1 == file_count_2):
            browser.find_element_by_link_text("file_download").click()
            time.sleep(2)
            #  Set the default download path for chrome
            path, dirs, files = next(os.walk("D:/CLICK HERE/python/oodp_reports/reports"))
            file_count_2 = len(files)
    browser.find_elements_by_class_name("mat-button-wrapper")[4].click()
    time.sleep(10)
    print(x + 1)