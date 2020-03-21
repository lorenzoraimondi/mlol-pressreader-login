import os
from utilities import log, build_driver

log("Pressreader script start...")

MLOL_USR = os.environ['MLOL_USR']
MLOL_PSW = os.environ['MLOL_PSW']
PR_USR = os.environ['PR_USR']
PR_PSW = os.environ['PR_PSW']

log("Config vars read")

try:
    # Building driver
    driver = build_driver()
    log("Driver created")
    
    # Getting MLOL login page
    driver.get("https://csbno.medialibrary.it/home/cover.aspx")
    log("Connected to MLOL")
    
    # MLOL Logging in 
    driver.find_element_by_id("lusername").send_keys(credentials["MLOL"]["USR"]);
    driver.find_element_by_id("lpassword").send_keys(credentials["MLOL"]["PSW"]);
    driver.find_element_by_xpath("//input[@name='']").click()
    log("Logged in MLOL")
    
    # Moving to Pressreader
    driver.get("https://csbno.medialibrary.it/media/scheda.aspx?id=550276273")
    driver.find_element_by_link_text("SFOGLIA").click()
    time.sleep(10)
    driver.switch_to_window(driver.window_handles[1])
    driver.find_element_by_class_name("alert-close").click()
    log("Connected to Pressreader")
    
    # Pressreader Logging in 
    driver.find_element_by_xpath("//div[@id='toolbarTop']/div/div[3]/a/span/span[2]").click()
    driver.find_element_by_id("SignInEmailAddress").send_keys(credentials["PR"]["USR"])
    driver.find_element_by_xpath("//input[@type='password']").send_keys(credentials["PR"]["PSW"])
    driver.find_element_by_xpath("//button[@type='submit']").click()
    log("Logged in Pressreader")
    
    driver.close()
    log("Success! Exiting...")
except Exception as e:
    log("Exception occurred")
    log(e)
    log("Execution Failed! Exiting...")
