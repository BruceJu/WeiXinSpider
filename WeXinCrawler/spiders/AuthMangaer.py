# -*- coding: utf-8 -*-
import cookielib
import threading
import urlparse

import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WeXinLogin(threading.Thread):

    def __init__(self, username=None, password=None, callback=None):
        super(WeXinLogin, self).__init__()
        '''
        初始化参数
        Parameters
        ----------
        username: str
            用户账号
        password: str
            用户密码

        Returns
        -------
            cookies
            token
        '''
        self.driver = webdriver.Chrome()
        self.callback = callback
        if username != None and password != None:
            self.__check_str(username, "username")
            self.username = username
            self.__check_str(password, "password")
            self.password = password
        else:
            raise SystemError('params error pleasure check')

    def run(self):
        cookies, token = self.__start_login(username=self.username, password=self.password)
        self.callback(token, cookies)

    def __check_str(self, input_string, param):
        """
        验证输入是否为字符串
        Parameters
        ----------
        input_string: str
            输入
        param: str
            需要验证的参数名
        Returns
        ----------
            None
        """
        if not isinstance(input_string, str):
            raise TypeError("{} must be an instance of str".format(param))

    def __start_login(self, username, password):
        """
        正式登录微信公众号平台，获取token和Cookies
        Parameters
        ----------
        username: str
            用户账号
        password: str
            用户密码
        Returns
        -------
            cookies:
            token:
        """
        self.driver.get('https://mp.weixin.qq.com')
        self.driver.find_element_by_name("account").clear()
        self.driver.find_element_by_name("account").send_keys(username)  # 修改为自己的用户名
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)  # 修改为自己的密码
        self.driver.find_element_by_class_name("btn_login").click()
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "weui-desktop-account__info"))
            )
            cookies = self.driver.get_cookies()
            current_url = self.driver.current_url
            token = self.__splite_token(current_url)
            return cookies, token


        except TimeoutException:
            print u'加载页面失败'

            return None, None
        finally:
            self.driver.close()
            self.driver.quit()

    def __splite_token(self, current_url):
        """
        从当前页面的url中获取出token字段以及值
        Parameters
         ----------
        current_url: str
            当前页面的url
        Example
         ----------
             https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=85024811

        Returns
        ------
        Token
        """
        return urlparse.parse_qs(current_url).get('token')[0]

    def __save_cookie(self, username, cookies):
        """
        存储cookies, username用于文件命名
        Parameters
        ----------
        username: str
            用户账号

        Returns
        -------
            None
        """
        # 实例化一个LWPcookiejar对象
        new_cookie_jar = cookielib.LWPCookieJar(username + '.txt')

        # 将转换成字典格式的RequestsCookieJar保存到LWPcookiejar中
        requests.utils.cookiejar_from_dict({c.name: c.value for c in cookies}, new_cookie_jar)

        # 保存到本地文件
        new_cookie_jar.save('cookies/' + username + '.txt', ignore_discard=True, ignore_expires=True)
