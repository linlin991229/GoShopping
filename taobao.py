from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

from PyQTUI import UIInit
from ViewModel import ViewMode

SHOPPING_CAR = 'https://cart.taobao.com/cart.htm'

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = "D:\\Unzip\\chromedriver\\chromedriver-win64\\chromedriver.exe"
driver = webdriver.Chrome()

# edge_options=webdriver.EdgeOptions()
# edge_options.executable_path="D:\\Downloads\\Programs\\msedgedriver.exe"
# driver=webdriver.Edge(options=edge_options)


def on_confirm_login():
    print('确认登录')
    # 转到购物车
    driver.get(SHOPPING_CAR)

    if SHOPPING_CAR==driver.current_url:
        now = datetime.now()
        print("登录成功", now)
        return True
    else:
        return False


def login():
    driver.get("https://www.taobao.com")
    # time.sleep(1)
    # 点击跳转登录
    # driver.find_element(By.LINK_TEXT, "亲，请登录").click()
    WebDriverWait(driver,1*60).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "亲，请登录"))
    ).click()
    # driver.find_element(By.CLASS_NAME, "icon-qrcode").click()
    WebDriverWait(driver,1*60).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "icon-qrcode"))
    ).click()
    print('等待用户扫码登录')
    UIInit(on_confirm_login, buy)


def buy(buy_time):

    print('进入购买', datetime.now(), buy_time)
    while True:
        if datetime.now() >= datetime.strptime(buy_time, '%Y-%m-%d %H:%M:%S'):
            # print("开始抢购！")
            # for i in range(0, 10):
            #     time.sleep(0.02)
            #     print('第'+str(i+1)+'次尝试')
            #     driver.find_element(By.ID, "J_Go").click()
            #     if driver.current_url != current_url:
            #         print('已抢购')
            #         break
            settlement = WebDriverWait(driver, 60*5).until(
                EC.element_to_be_clickable((By.ID, "J_Go"))
            )
            settlement.click()
            submit_order = WebDriverWait(driver, 3*60).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "go-btn"))
            )
            submit_order.click()
            print('抢购结束')
            break


if __name__ == '__main__':
    login()
