from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import numpy as np
import numpy.random as rd
import time
import datetime


if __name__ == '__main__':

    mu = 1   #平均ログイン間隔 = 1分

    while True:
        driver = webdriver.Ie("C:\\Program Files\\Anaconda3\\IEDriverServer.exe")
        driver.get("http://localhost/MetricServer/")

        elem_username = driver.find_element_by_name("UserName")
        elem_username.clear()
        elem_username.send_keys("admin")

        elem_password = driver.find_element_by_name("Password")
        elem_password.clear()
        elem_password.send_keys("admin")
        elem_password.send_keys(Keys.RETURN)

        time.sleep(2)

        now = datetime.datetime.today()
        f = open('ms_login_test.log', 'a')

        if "MetricServer - プロセスマネージャー" in driver.title:
            outstr = "Login Succeeded at " + now.strftime("%Y/%m/%d %H:%M:%S")

        elif "Key Manager" in driver.title:
            outstr = "Unable to access to dongle license at" + now.strftime("%Y/%m/%d %H:%M:%S")

        else:
            outstr = "Login Failed at" + now.strftime("%Y/%m/%d %H:%M:%S")
        
        print(outstr)
        f.write(outstr + "\n")
        f.close()
        
        driver.get("http://localhost/MetricServer/Account/LogOff")
        driver.quit()

        x = rd.exponential(mu)
        time.sleep(60 * x)
        #print("Next login after elapse of {0} min.".format(x))
    
