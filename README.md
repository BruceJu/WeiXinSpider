
# 微信公众号定向爬虫
-----------

## 简介

* 用于爬取某个微信公众号的所有文章列表信息
* 提供运行状态的语音播报。
* 提供MySQL，MongDB，俩种存储方式


## 使用前准备

* 需要准备至少2个微信公众订阅号，这个需要自己申请，
* 如果需要使用语音播报模块，需要安装 win32com


## 配置项

### 
> 下载项目后，打开`setting.py`文件，进行配置
* 下载延迟项，过快会被ban,建议在 20到30之前
```python
DOWNLOAD_DELAY = 30
```
* 选择默认的本地存储管道，
```python

ITEM_PIPELINES = {
   'WeXinCrawler.pipelines.MongDBPipeline': 300
  # 'WeXinCrawler.pipelines.MysqlTwistedPipline': 300,
}
```

* 公账号授权的信息的list，用于在爬虫被禁掉时，自动切换账户,无上限，至少2个
* 这个需要自己在微信公众开放平台上，注册，注意是订阅号，不是小程序
```python
AUTH_LIST = [
             {'Account':'160xxxxxx@qq.com','PassWord':'xxxxxxx'},
             {'Account':'119xxxxxx@qq.com','PassWord':'xxxxxxx'}
            ]
```


* 需要爬取的公帐号的名称，暂不支持同时爬取多个公帐号
```python
OFFICIAL_ACCOUNTS = '李叫兽'
#OFFICIAL_ACCOUNTS = '咪蒙'
#OFFICIAL_ACCOUNTS = 'Python中文社区'
```
* 是否需要使用语音播报爬虫运行状态,当为True时，需要安装 python win32com 模块
```python
SPEEK_ALLOW = False
```

* MongDB数据库配置，需要配置ITEM_PIPELINES种MongDBPipeline存储
```python
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "Weixin_Spider"  # 库名
MONGO_COLLECTION = "weixin_article"  # collection名
```
* MySQL数据库连接配置，需要配置ITEM_PIPELINES种的MysqlTwistedPipline存储
* 需要自行建立数据表
  * 表名：weixin_spider
  * 字段：id
     * 类型：int
     * 主键
     * 自增长
  * 字段：cover
     * 类型：varchar
  * 字段：appmsgid
     * 类型：varchar
  * 字段：diqest
     * 类型：varchar 
  * 字段：link
     * 类型：varchar
  * 字段：title
     * 类型：varchar  
  * 字段：update_time
     * 类型：datetime   
```python

MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "Weixin_Spider"
MYSQL_USER = "root"
MYSQL_PASSWORD = "xxxxxx"
```
## 使用

* 启动
* 扫码登录
* 等待爬虫执行完成


## 详细制作说明

### 登陆部分

* 使用多线程构建登录模块（同步模式）
* `selenium`打开网页，输入设置的账户和密码信息
* 需要手动进行扫码登录，这个是微信的登录机制导致的
* 返回`token`,`cookies`
* 具体的逻辑可以查看 `AuthManager.py`这个文件

### 进行爬取

* 根据登录获取的`token`和`cookies`进行`headers`构建
* 发起请求进行 公帐号的获取，返回数据格式为json,需要获取`fakeid`
* 根据获取的`fakeid`进行具体的文章列表解析。返回数据为json
* 解析总页数，进行数据的递归爬取
 

## 待完善

* 多个公帐号同时爬取
* 授权账户的本地化
* 