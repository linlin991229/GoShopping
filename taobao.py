from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from PyQt5.QtWidgets import QApplication,QLabel

app=QApplication([])
driver = webdriver.Chrome()


def login():
    driver.get("https://www.taobao.com")
    time.sleep(2)
    # 点击跳转登录
    driver.find_element(By.LINK_TEXT, "亲，请登录").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "icon-qrcode").click()
    input('请扫码登录，然后回车')

    QLabel('请扫码登录').show()
    app.exec_()

    # 转到购物车
    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(2)
    now = datetime.now()
    print("登录成功", now)


def buy(buy_time):
    input("请选中你商品后回车")
    while True:
        if datetime.now() >= buy_time:
            print("开始抢购！")
            driver.find_element(By.ID, "J_Go").click()


if __name__ == '__main__':
    # login()
    buy(input('请输入抢购时间:'))
