import os
import sys
import time
from selenium import webdriver

def log(string):
    print(string)
    sys.stdout.flush()
    
def build_driver():
    log("Getting Chrome binary location from the environment...")
    GOOGLE_CHROME_SHIM = os.environ["GOOGLE_CHROME_SHIM"]
    log("Found GOOGLE_CHROME_SHIM > {}".format(GOOGLE_CHROME_SHIM))
    
    WAIT = 10
    log("Setting Driver implicit wait to {} s".format(WAIT))
        
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = GOOGLE_CHROME_SHIM
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(WAIT)
    
    log("Driver successfully built")
    
    return driver

def job():
    log("Pressreader script start...")

    MLOL_USR = os.environ['MLOL_USR']
    MLOL_PSW = os.environ['MLOL_PSW']
    PR_USR = os.environ['PR_USR']
    PR_PSW = os.environ['PR_PSW']

    log("Config vars read")

    try:
        # Building driver
        driver = build_driver()

        # Getting MLOL login page
        driver.get("https://csbno.medialibrary.it/home/cover.aspx")
        log("Connected to MLOL")

        # MLOL Logging in 
        driver.find_element_by_id("lusername").send_keys(MLOL_USR);
        driver.find_element_by_id("lpassword").send_keys(MLOL_PSW);
        driver.find_element_by_xpath("//input[@name='']").click()
        log("Logged in MLOL")

        # Moving to Pressreader
        log("Opening Pressreader...")
        driver.get("https://csbno.medialibrary.it/media/view.aspx?id=550276273")
        log("Connected to Pressreader")

        try:
            log("Closing Alert...")
            driver.find_element_by_class_name("alert-close").click()
        except Exception as e:
            log("Error closing Alert:")
            log(e)

        # Pressreader Logging in 
        log("Logging in Pressreader...")
        driver.find_element_by_xpath("//div[@id='toolbarTop']/div/div[3]/a/span/span[2]").click()
        driver.find_element_by_id("SignInEmailAddress").send_keys(PR_USR)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(PR_PSW)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        log("Logged in!")

        driver.close()
        log("Success!")
    except Exception as e:
        log("Exception occurred")
        log(e)
        log("Execution Failed!")
