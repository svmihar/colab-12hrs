from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import time
import logging
import random
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.INFO)
logger = logging.getLogger(__name__)

chrome_option = Options()
chrome_option.add_argument("--start_maximized")
if Path('./config').is_file:
    CONFIG = open('config').read().splitlines()
    EMAIL, PASS, GOOGLE_COLAB_LINK,CHROMEDRIVER_PATH  = CONFIG[0], CONFIG[1], CONFIG[2], CONFIG[3]
else:
    logger.info('sing nggena ae')

logger.info(f'using {EMAIL}')

driver = webdriver.Chrome(
    executable_path=CHROMEDRIVER_PATH, options=chrome_option)


def sleeper(t, silent=True):
    for i in range(t, 0, -1):
        if silent:
            pass
        else:
            print(i)
        time.sleep(1)
    print(f'finished sleeping for {t} seconds')


def login():
    driver.get('https://mail2.its.ac.id/index.php')
    driver.find_element_by_xpath(
        '//*[@id="content"]/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input').send_keys(EMAIL)
    driver.find_element_by_xpath(
        '//*[@id="content"]/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input').send_keys(PASS)
    driver.find_element_by_xpath(
        '//*[@id="content"]/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input').click()
    sleeper(3, silent=False)
    logger.info(driver.current_url)
    if 'speedbump' in driver.current_url:
        logger.info('google speed bump detected, clicking continue now')
        driver.find_element_by_xpath(
            '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span').click()
    driver.get('https://google.com/')
    logger.info('logged in to integra')
    logger.info('logged in to gmail')
    driver.get(GOOGLE_COLAB_LINK)


def main():
    logger.info('clicking connect')
    sleepy_time = random.randint(10,20)
    logging.info(f'sleeping for {sleepy_time}  seconds')
    sleeper(sleepy_time)
    driver.find_element_by_xpath(
        '//*[@id="top-toolbar"]/colab-connect-button').click()


if __name__ == "__main__":
    c = 0
    login()
    while True:
        try:
            main()
        except Exception as e:
            logger.info('failed, retrying now')
            logger.info(e)
            c = 0
            continue
        c += 1
        logger.info(f'clicked for {c}')
