import os
import sys
import time
from selenium import webdriver

def log(string):
    t = time.asctime(time.localtime())
    print("[{}] {}".format(t, string))
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
    
    log("Driver successfully build")
    
    return driver
