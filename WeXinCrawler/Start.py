# -*- coding: utf-8 -*-
import datetime
from scrapy import cmdline



if __name__ == '__main__':

    cmdline.execute('scrapy crawl WeXinSpider'.split())


data = '''
"app_msg_list": [
        {
            "aid": "2655820225_1",
            "appmsgid": 2655820225,
            "cover": "https://mmbiz.qlogo.cn/mmbiz_jpg/cnLxyJPKUPkrKlxrf4RWV8tNrS8EG4ibTJU0pJ1Fxl6eV2I6ibs67K7Oo9TCKic1PRepgN7G2BmnchGJurRFFyEng/0?wx_fmt=jpeg",
            "digest": "如何毁掉自己的生活：生！儿！子！",
            "itemidx": 1,
            "link": "http://mp.weixin.qq.com/s?__biz=MjM5MTI0NjQ0MA==&mid=2655820225&idx=1&sn=c5638a6178bfe3a512a2916999779c23&chksm=bd0048c68a77c1d0ce0753088af8f14fb9d51a043108aa03725b3830ec880bdde163bb0a3f5e#rd",
            "title": "大多数男孩的妈妈将死于嫉妒。",
            "update_time": 1518274348
        },
        {
            "aid": "2655820209_1",
            "appmsgid": 2655820209,
            "cover": "https://mmbiz.qlogo.cn/mmbiz_jpg/cnLxyJPKUPm1rdEvYdacQGojCeGk9MCibnUhbkSvwDhorjpFhUOicZbzxbIRTSibTIK3tRIzsxunNdzdlfv7KlNzA/0?wx_fmt=jpeg",
            "digest": "我用这9款百元包，背出了LV的气场。",
            "itemidx": 1,
            "link": "http://mp.weixin.qq.com/s?__biz=MjM5MTI0NjQ0MA==&mid=2655820209&idx=1&sn=7f27e51e340e08e4e3e4fcda484f2c9b&chksm=bd0048b68a77c1a049dd9b0c7ee4f505580be92c45ea1f22c358150a5df0c8e5c131cf333e48#rd",
            "title": "妈蛋！我2万块的包输给了同事300块的！",
            "update_time": 1518187822
        },
        {
            "aid": "2655820192_1",
            "appmsgid": 2655820192,
            "cover": "https://mmbiz.qlogo.cn/mmbiz_jpg/cnLxyJPKUPnyq2miaXGAbm59uT5XYUH7gbcpW259uhpeOX9ibq55eORNdWQXiap6bK1fbRwhiaeTjMjP5eONGMlukQ/0?wx_fmt=jpeg",
            "digest": "这个世界上，不用穿胸罩的地方只有一个。",
            "itemidx": 1,
            "link": "http://mp.weixin.qq.com/s?__biz=MjM5MTI0NjQ0MA==&mid=2655820192&idx=1&sn=111b3866230816547c3de27cf6868683&chksm=bd0048a78a77c1b111162e1251b974c551bff4afa4040cd87aa9d5d4bd1fafa785318314cfc1#rd",
            "title": "“要是我按下home键，就可以回到家该多好”",
            "update_time": 1518101466
        },
        {
            "aid": "2655820192_2",
            "appmsgid": 2655820192,
            "cover": "https://mmbiz.qlogo.cn/mmbiz_jpg/cnLxyJPKUPnyq2miaXGAbm59uT5XYUH7gmvTvlhGk7Dz8rDZ7n0HHiafjibPOEKiaRpibcSI16C3c5KlnOTVe6zGHYQ/0?wx_fmt=jpeg",
            "digest": "白天在办公室卑微，夜晚在地铁上崩溃。",
            "itemidx": 2,
            "link": "http://mp.weixin.qq.com/s?__biz=MjM5MTI0NjQ0MA==&mid=2655820192&idx=2&sn=f8652bb92487fb58c62c8496907da004&chksm=bd0048a78a77c1b17ea5beb79b68b24a364af52e92ec9492224afb48e6e78e126ff53126f1c4#rd",
            "title": "1张图，带你看遍地铁里的1000万种人生",
            "update_time": 1518101466
        },
        {
            "aid": "2655820165_1",
            "appmsgid": 2655820165,
            "cover": "https://mmbiz.qlogo.cn/mmbiz_jpg/cnLxyJPKUPm6zFmmTZs3dYw3NiaAePKYJlm1e1u6bgNqn6fLmRGs4namDJlYhF0shcsmIptUuh7zIVhubc29GdA/0?wx_fmt=jpeg",
            "digest": "员工比老板有钱是什么体验？我！知！道！",
            "itemidx": 1,
            "link": "http://mp.weixin.qq.com/s?__biz=MjM5MTI0NjQ0MA==&mid=2655820165&idx=1&sn=e61115a01eb4265fd7b030a5d02e1ed8&chksm=bd0048828a77c1945a22c80d890cda15be8f065f655d7e85183c45cbe2a6e7218a759ad12ad0#rd",
            "title": "那天我骑自行车，蹭到了员工的玛莎拉蒂……",
            "update_time": 1518016939
        },
        {
            "aid": "2655820165_2",
            "appmsgid": 2655820165,
            "cover": "https://mmbiz.qlogo.cn/mmbiz_jpg/cnLxyJPKUPm6zFmmTZs3dYw3NiaAePKYJQtdicowtbYluyS0jn9ObicwKMBYH3QrbiblsV2j0h8HGRbarxviaByR4JA/0?wx_fmt=jpeg",
            "digest": "撩汉看完这一篇，包你泡到胡一天。",
            "itemidx": 2,
            "link": "http://mp.weixin.qq.com/s?__biz=MjM5MTI0NjQ0MA==&mid=2655820165&idx=2&sn=623ee10bd18d08bd48fbe162484b8a7d&chksm=bd0048828a77c194fc5d6ef434e3df8da92b9c72d2ed873dd06a46c646de55d5606fd0b674ad#rd",
            "title": "只有用不好的套路，没有撩不到的男神",
            "update_time": 1518016939
        },
        {
            "aid": "2655820124_1",
            "appmsgid": 2655820124,
            "cover": "https://mmbiz.qlogo.cn/mmbiz_jpg/cnLxyJPKUPnl4fGyRiaibYRgBv86sgv3goway60X7iatrKX5GwNKGF5SX9TR2hfDicic4UfRdOWqyJfRjXLjzxDyOcQ/0?wx_fmt=jpeg",
            "digest": "老板你不发钱就算了，为什么要恶心我？",
            "itemidx": 1,
            "link": "http://mp.weixin.qq.com/s?__biz=MjM5MTI0NjQ0MA==&mid=2655820124&idx=1&sn=df3a154d7adace6fb297a71861d141d0&chksm=bd00485b8a77c14d351d7e6c96cc921a78b087e70bee78ad36cbbbf689e0e5fdca7725b619a3#rd",
            "title": "谁能想到，我的年终奖是10个馒头",
            "update_time": 1517931527
        },
        {
            "aid": "2655820124_2",
            "appmsgid": 2655820124,
            "cover": "https://mmbiz.qlogo.cn/mmbiz_jpg/cnLxyJPKUPnl4fGyRiaibYRgBv86sgv3goVs0gONVEUEAt6DJSibgqo9XxgugyNFlLYD50BicHQozbIUCMibJibPhv7w/0?wx_fmt=jpeg",
            "digest": "我有一个恋爱，想和小奶狗谈谈。",
            "itemidx": 2,
            "link": "http://mp.weixin.qq.com/s?__biz=MjM5MTI0NjQ0MA==&mid=2655820124&idx=2&sn=6b350474265ae20d53731923a02226b6&chksm=bd00485b8a77c14dc6cf7c5a8e7cda7760eefc81c85ad2abeb2aa876c92d0d2bc189c34932e0#rd",
            "title": "自从交往小奶狗，生活甜到没朋友！",
            "update_time": 1517931527
        }
    ]
'''



