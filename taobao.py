from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

from UI import initUI

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = "D:\\Unzip\\chromedriver\\chromedriver-win64\\chromedriver.exe"
driver = webdriver.Chrome()

# edge_options=webdriver.EdgeOptions()
# edge_options.executable_path="D:\\Downloads\\Programs\\msedgedriver.exe"
# driver=webdriver.Edge(options=edge_options)

global frame


def onclick():
    print('确认登录')
    # 转到购物车
    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(1)
    now = datetime.now()
    print("登录成功", now)


def login():
    driver.get("https://www.taobao.com")
    time.sleep(1)
    # 点击跳转登录
    driver.find_element(By.LINK_TEXT, "亲，请登录").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "icon-qrcode").click()
    print('等待用户扫码登录')

    initUI('请扫码登录', onclick)



def buy(buy_time):
    input("请选中你商品后回车")
    while True:
        if datetime.now() >= buy_time:
            print("开始抢购！")
            driver.find_element(By.ID, "J_Go").click()


if __name__ == '__main__':
    login()
    buy(input('请输入抢购时间:'))
