import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def finder(start, end):
    # перед деплоем розкоментити
    # + ше добавити Keys , попрописувать путі до драйверов
    global km
    options = webdriver.ChromeOptions()
    # options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # options.add_argument("--headless")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--no-sandbox")
    # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
    # -----------------------------------------------------------------------------------------------------------------
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com/maps")
    try:
        driver.find_element_by_class_name("searchbox-directions").click()
        time.sleep(5)
        # -----------------------------------------------------------------------------------------------------------------
        entry_start = driver.find_element_by_id("sb_ifc51").find_element_by_class_name("tactile-searchbox-input")
        entry_start.send_keys(start)
        time.sleep(5)
        # -----------------------------------------------------------------------------------------------------------------
        entry_end = driver.find_element_by_id("sb_ifc52").find_element_by_class_name("tactile-searchbox-input")
        entry_end.send_keys(end)
        time.sleep(5)
        entry_end.send_keys(Keys.ENTER)
        time.sleep(2.5)
        # -----------------------------------------------------------------------------------------------------------------
        km = driver.find_element_by_class_name("xB1mrd-T3iPGc-trip-tUvA6e").find_element_by_tag_name("div").text
        time.sleep(7)
    except Exception as e:
        print(e)
        driver.quit()
        finder(start, end)
    finally:
        driver.quit()
        return km


if __name__ == '__main__':
    start = "Харківське Шосе 158"
    end = "Анни ахматової 28"
    print(finder(start, end))
