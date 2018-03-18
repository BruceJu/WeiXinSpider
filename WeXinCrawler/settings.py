# -*- coding: utf-8 -*-

# Scrapy settings for WeXinCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WeXinCrawler'

SPIDER_MODULES = ['WeXinCrawler.spiders']
NEWSPIDER_MODULE = 'WeXinCrawler.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 30



#DOWNLOADER_MIDDLEWARES = {
#    'WeXinCrawler.middlewares.WexincrawlerDownloaderMiddleware': 543,
#}

#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}


ITEM_PIPELINES = {
  # 'WeXinCrawler.pipelines.MongDBPipeline': 300,
    'WeXinCrawler.pipelines.MysqlTwistedPipline': 300,
}



# 公账号授权的信息的list，用于在爬虫被禁掉时，自动切换账户
AUTH_LIST = [
             {'Account':'1603255098@qq.com','PassWord':'woshi007008'},
             {'Account':'1198746549@qq.com','PassWord':'woshi007008'}
            ]

OFFICIAL_ACCOUNTS = '李叫兽'


# MongDB数据库配置
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "Weixin_Spider"  # 库名
MONGO_COLLECTION = "weixin_article"  # collection名
# MONGO_USER = "zhangsan"
# MONGO_PSW = "123456"



# MySQL数据库连接
MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "spiderdata"
MYSQL_USER = "root"
MYSQL_PASSWORD = "woshi007008"