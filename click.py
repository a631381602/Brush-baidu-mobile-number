#coding:utf-8

'''导入selenium中的webdriver包，只有导入这个包才能使用webdriver api 进行自动化脚本开发'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
import time,re,random

myProxy_list = []

def getUA():
    uaList = [
    	#ios user agent
    	'Mozilla/5.0 (iPhone 5CGLOBAL; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/6.0 MQQBrowser/5.8 Mobile/12F70 Safari/8536.25',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4',
    	'Mozilla/5.0 (iPhone 5CGLOBAL; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/6.0 MQQBrowser/5.7 Mobile/12B466 Safari/8536.25',
    	'Mozilla/5.0 (iPhone 5CGLOBAL; CPU iPhone OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/6.0 MQQBrowser/5.6 Mobile/12B440 Safari/8536.25',
    	'Mozilla/5.0 (iPhone 5CGLOBAL; CPU iPhone OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/6.0 MQQBrowser/5.5 Mobile/12B435 Safari/8536.25',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/12B411 UCBrowser/10.0.5.508 Mobile',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/12A405 UCBrowser/10.0.2.497 Mobile',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/12B411 UCBrowser/10.1.0.518 Mobile WindVane tae_sdk_ios_1.0.1',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B411 MicroMessenger/6.0 NetType/WIFI',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/12B411 UCBrowser/10.0.5.508 Mobile',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A405 Safari/600.1.4',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B651 Safari/9537.53',
    	'Mozilla/5.0 (iPhone 5CGLOBAL; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/6.0 MQQBrowser/5.0.5 Mobile/11B651 Safari/8536.25',
    	'Mozilla/5.0 (iPhone 5CGLOBAL; CPU iPhone OS 7_0_5 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/6.0 MQQBrowser/5.0.4 Mobile/11B601 Safari/8536.25',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/31.0.1650.18 Mobile/11B554a Safari/8536.25',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B554a',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B554a UCBrowser/9.3.1.339 Mobile',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B554a Safari/7534.48.3',
    	'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53',

    	#android user agent
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; MI 4LTE Build/KTU84P) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/6.5.1 (Baidu; P1 4.4.4)",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; MI 4LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.1.1",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; MI 4LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.8 Mobile Safari/537.36",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTE Build/KTU84P) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/6.5 (Baidu; P1 4.4.4)",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.8 Mobile Safari/537.36",
		"Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; SCH-N719 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; X9180 Build/KVT49L) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025411 Mobile Safari/533.1 MicroMessenger/6.1.0.66_r1062275.542 NetType/WIFI",
		"Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; 2013022 Build/HM2013022) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.1.1",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; HM NOTE 1LTE Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.2.0.535 U3/0.8.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; HM NOTE 1LTE Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.1.0.527 U3/0.8.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.6 Mobile Safari/537.36",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTE Build/KTU84P) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.1.0.40_r1018582.540 NetType/WIFI",
		"Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; MI 2S Build/JRO03L) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/6.0.2.58_r984381.520 NetType/WIFI",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTETD Build/KTU84P) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.5 Mobile Safari/533.1 MicroMessenger/6.0.0.54_r849063.501 NetType/WIFI",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTETD Build/KTU84P) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/6.1 (Baidu; P1 4.4.4)",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTETD Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.5 Mobile Safari/537.36",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; HM NOTE 1LTETD Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.7.500 U3/0.8.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTETD Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.0.1",
		"Mozilla/5.0 (Linux; Android 4.4.4; M351 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.0.0.50_r844973.501 NetType/WIFI",
		"Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; Q3迷你版 Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3.5 (Baidu; P1 4.2.2)",
		"Mozilla/5.0 (Linux; Android 4.4.4; Hisense E621T Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 baiduboxapp/5.0 (Baidu; P1 4.4.4)",
		"Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; HS-EG906 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/5.3.1.67_r745169.462",
		"Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; GT-N7000 Build/IML74K) AppleWebKit/533.1 (KHTML, like Gecko) Mobile MQQBrowser/4.0 Safari/533.1",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; M351 Build/KTU84P) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/6.0 (Baidu; P1 4.4.4)",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; M351 Build/KTU84P) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.5.489 U3/0.8.0 Mobile Safari/533.1",
		"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; M351 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Linux; Android 4.2.1; M040 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Mobile Safari/537.36 OPR/20.0.1396.72047",
		"Mozilla/5.0 (Linux; U; Android 4.2.1; zh-CN; M040 Build/JOP40D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.6.0.378 U3/0.8.0 Mobile Safari/533.1",
		"Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; M040 Build/JOP40D) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baidubrowser/4.3.16.2 (Baidu; P1 4.2.1)",
		"Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; M040 Build/JOP40D) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.1 (Baidu; P1 4.2.1)",
		"Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; M040 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 Mobile Safari/537.36",
		"Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; M040 Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baidubrowser/4.2.9.2 (Baidu; P1 4.2.1)",
		"Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; M040 Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; M040 Build/JOP40D) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baidubrowser/4.1.3.1 (Baidu; P1 4.2.1)",
		"Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; M040 Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Maxthon/4.1.3.2000",
		"Mozilla/5.0 (Linux; Android 4.2.1; M040 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36",
		"Mozilla/5.0 (Linux; U; Android 4.1.1; zh-CN; M040 Build/JRO03H) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.4.1.362 U3/0.8.0 Mobile Safari/533.1",
		"Mozilla/5.0 (Linux; Android 4.1.1; M040 Build/JRO03H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36",
		"Mozilla/5.0 (Linux; Android 4.1.1; M040 Build/JRO03H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.64 Mobile Safari/537.36",
		"Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; M040 Build/JRO03H) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baidubrowser/4.2.4.0 (Baidu; P1 4.1.1)",
		"Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; M031 Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Linux; U; Android 4.1.1; zh-CN; M031 Build/JRO03H) AppleWebKit/534.31 (KHTML, like Gecko) UCBrowser/8.8.3.278 U3/0.8.0 Mobile Safari/534.31",
		"Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; M040 Build/JRO03H) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/4.1 Mobile Safari/533.1",
		"Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; M040 Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3) AppleWebKit/534.31 (KHTML, like Gecko) Chrome/17.0.558.0 Safari/534.31 UCBrowser/2.3.1.257",
		"Mozilla/5.0 (Linux; U; Android 3.2; zh-cn; GT-P6200 Build/HTJ85B) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
		"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; U8800 Build/HuaweiU8800) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
		"Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M031 Build/IML74K) AppleWebKit/530.17 (KHTML, like Gecko) FlyFlow/2.3 Version/4.0 Mobile Safari/530.17 baidubrowser/023_1.41.3.2_diordna_069_046/uzieM_51_3.0.4_130M/1200a/963E77C7DAC3FA587DF3A7798517939D%7C408994110686468/1",
		"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; U8800 Build/HuaweiU8800) AppleWebKit/530.17 (KHTML, like Gecko) FlyFlow/2.3 Version/4.0 Mobile Safari/530.17 baidubrowser/042_1.6.3.2_diordna_008_084/IEWAUH_01_5.3.2_0088U/1001a/BE44DF7FABA8768B2A1B1E93C4BAD478%7C898293140340353/1",
		"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; U8800 Build/HuaweiU8800) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
		"Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; HTC S720e Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; HTC S720e Build/IMM76D) UC AppleWebKit/534.31 (KHTML, like Gecko) Mobile Safari/534.31",
		"Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M031 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
		"MQQBrowser/4.0/Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M031 Build/IML74K) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
		"MQQBrowser/3.7/Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M9 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M9 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
		"MQQBrowser/3.5/Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M9 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M031 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; U8800 Build/HuaweiU8800) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
		"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; U8800 Build/HuaweiU8800) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
		"MQQBrowser/3.7/Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; U8800 Build/HuaweiU8800) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
		"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; U8800 Build/HuaweiU8800) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
		"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn) AppleWebKit/530.17 (KHTML, like Gecko) FlyFlow/2.2 Version/4.0 Mobile Safari/530.17",
		"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; U8800 Build/HuaweiU8800) UC AppleWebKit/534.31 (KHTML, like Gecko) Mobile Safari/534.31",
		"Mozilla/5.0 (Linux; Android 4.0.3; M031 Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
		"Opera/9.80 (Android 4.0.3; Linux; Opera Mobi/ADR-1210241511) Presto/2.11.355 Version/12.10",
		"Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M031 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn) AppleWebKit/530.17 (KHTML, like Gecko) FlyFlow/2.2 Version/4.0 Mobile Safari/530.17",
		"Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M031 Build/IML74K) UC AppleWebKit/534.31 (KHTML, like Gecko) Mobile Safari/534.31"

    ]
    headers = random.choice(uaList)
    return headers

'''设置query、目标网站、总点击次数，原始排名如下：

		杭州捷蓝科技招聘    m.wealink.com	14
		翔鹭工贸招聘    m.job1001.com	19
		山西科达自控工程技术有限公司招聘    m.job1001.com	17
		杭州史图尔兹环境设备有限公司招聘    m.zhaopin.com	19
		杭州泰格招聘    3g.51job.com	19
		住友商事招聘    m.liepin.com	14
		北京永和投资管理有限公司招聘    m.zhaopin.com	15
		上海沪正纳米科技有限公司招聘    m.pincai.com	11
		郑州市舒记餐饮有限公司招聘    m.zhaopin.com	11
		大丰收招聘    m.jobui.com	13
		加拿大美加国际投资招聘    m.wealink.com	16
		英德台泥招聘    m.wealink.com	19
		协和医学院招聘    m.chinahr.com	16
		马安堤围管理处招聘    m.chinahr.com	12
		辽宁冠业招聘    m.jobui.com	14
		广州有铭人力资源顾问有限公司招聘    m.zhaopin.com	16
		深圳市凯誉资源投资有限公司招聘    m.jobui.com	16
		丹菲诗服饰有限公司招聘    m.jobui.com		19
		北京中天顺泰科贸有限责任公司招聘    m.liepin.com	14
		揭阳市正而惠商贸有限公司招聘    m.chinahr.com	13
		法莱利化工涂料招聘    m.dajie.com	15	
		苏州永真房地产经纪有限公司招聘    m.zhaopin.com	13

'''
word_dict = {
		"杭州捷蓝科技招聘":{'domain':'wealink.com','all_count':7,'count':0},
		"翔鹭工贸招聘":{'domain':'job1001.com','all_count':6,'count':0},
		"山西科达自控工程技术有限公司招聘":{'domain':'m.job1001.com','all_count':5,'count':0},
		"杭州史图尔兹环境设备有限公司招聘":{'domain':'m.zhaopin.com','all_count':4,'count':0},
		"杭州泰格招聘":{'domain':'51job.com','all_count':4,'count':0},
		"住友商事招聘":{'domain':'liepin.com','all_count':4,'count':0},
		"北京永和投资管理有限公司招聘":{'domain':'zhaopin.com','all_count':5,'count':0},
		"上海沪正纳米科技有限公司招聘":{'domain':'pincai.com','all_count':5,'count':0},
		"郑州市舒记餐饮有限公司招聘":{'domain':'zhaopin.com','all_count':5,'count':0},
		"大丰收招聘":{'domain':'jobui.com','all_count':5,'count':0},
		"加拿大美加国际投资招聘":{'domain':'wealink.com','all_count':5,'count':0},
		"英德台泥招聘":{'domain':'wealink.com','all_count':6,'count':0},
		"协和医学院招聘":{'domain':'chinahr.com','all_count':5,'count':0},
		"马安堤围管理处招聘":{'domain':'chinahr.com','all_count':5,'count':0},
		"辽宁冠业招聘":{'domain':'jobui.com','all_count':4,'count':0},
		"广州有铭人力资源顾问有限公司招聘":{'domain':'zhaopin.com','all_count':5,'count':0},
		"深圳市凯誉资源投资有限公司招聘":{'domain':'jobui.com','all_count':4,'count':0},
		"北京中天顺泰科贸有限责任公司招聘":{'domain':'liepin.com','all_count':5,'count':0},
		"揭阳市正而惠商贸有限公司招聘":{'domain':'chinahr.com','all_count':4,'count':0},
		"法莱利化工涂料招聘":{'domain':'m.dajie.com','all_count':5,'count':0},
		"苏州永真房地产经纪有限公司招聘":{'domain':'zhaopin.com','all_count':5,'count':0},

		# "北京房价":{'domain':'taofang.com','all_count':5,'count':0},
		# "上海房价":{'domain':'taofang.com','all_count':5,'count':0},
		# "北京奥迪二手车":{'domain':'baixing.com','all_count':5,'count':0},
		# "北京奥迪二手车交易市场":{'domain':'sohu.com','all_count':5,'count':0},
	}

'''domain出现在第一页，则根据排名指定如下点击顺序'''
click_list_rank1 = {
	1:[1],
	2:[1,2],
	3:['%s' % random.randint(1,2),3] , 
	4:['%s' % random.randint(1,3),4],
	5:['%s' % random.randint(1,4),5],
	6:['%s' % random.randint(1,5),6],
	7:['%s' % random.randint(1,6),7],
	8:['%s' % random.randint(1,7),8],
	9:['%s' % random.randint(1,8),9],
	10:['%s' % random.randint(1,9),10],
	11:['%s' % random.randint(1,5),'%s' % random.randint(6,10),11],
	12:['%s' % random.randint(1,5),'%s' % random.randint(6,11),12],
	13:['%s' % random.randint(1,5),'%s' % random.randint(6,12),13],
	14:['%s' % random.randint(1,5),'%s' % random.randint(6,13),14],
	15:['%s' % random.randint(1,5),'%s' % random.randint(6,14),15],
	16:['%s' % random.randint(1,10),'%s' % random.randint(11,15),16],
	17:['%s' % random.randint(1,10),'%s' % random.randint(11,16),17],
	18:['%s' % random.randint(1,10),'%s' % random.randint(11,17),18],
	19:['%s' % random.randint(1,10),'%s' % random.randint(11,18),19],
	20:['%s' % random.randint(1,10),'%s' % random.randint(11,19),20]
}

def word_list():
	word_list = word_dict.keys()
	word = random.choice(word_list)
	return word

def wait():
	return random.uniform(20,60) 

def export():
	export_ip = re.search(r'\d+\.\d+\.\d+\.\d+',urllib2.urlopen("http://www.whereismyip.com").read()).group(0)
	return export_ip
	
'''adsl切换出口ip'''
g_adsl_account = {"name": "ADSL",
				"username": "99392213",
				"password": "123456"}

'''adsl拨号'''	 
class Adsl(object):
	def __init__(self):
		self.name = g_adsl_account["name"]
		self.username = g_adsl_account["username"]
		self.password = g_adsl_account["password"]
	
	def set_adsl(self, account):
		self.name = account["name"]
		self.username = account["username"]
		self.password = account["password"]
 
	def connect(self):
		cmd_str = "rasdial %s %s %s" % (self.name, self.username, self.password)
		os.system(cmd_str)
		time.sleep(5)
 
	def disconnect(self):
		cmd_str = "rasdial %s /disconnect" % self.name
		os.system(cmd_str)
		time.sleep(5)
 
	def reconnect(self):
		self.disconnect()
		self.connect()

for ip in open('hege_daili.txt'):
	if ip.strip in myProxy_list:
		continue
	else:
		myProxy_list.append(ip)
		
		newip = ip.strip()

	'''加载代理ip'''
	proxy = Proxy({
	    'proxyType': ProxyType.MANUAL,
	    'httpProxy': newip,
	    'ftpProxy': newip,
	    'sslProxy': newip,
	    'noProxy': '' # set this value as desired
	    })

	useragent = getUA()

	'''加载代理，写入配置文件'''
	profile = webdriver.FirefoxProfile()
	profile.set_preference("general.useragent.override","%s" % useragent)  

	'''打开浏览器窗口'''
	# browser = webdriver.Firefox(profile,proxy=proxy)
	browser = webdriver.Firefox(profile)

	try:
		'''设置浏览器窗口'''
		browser.set_window_size(300,800)
	except:
		print '浏览器窗口调整错误，重启浏览器'
		browser.quit()
		continue

	word = word_list()
	domain = word_dict[word]['domain']
	all_count = word_dict[word]['all_count']
	count = word_dict[word]['count']

	print '>>>>>>>>>>>>>>>>>>开始查询:%s，已点击%s次>>>>>>>>>>>>>>>>>' % (word,count)

	if count > all_count:
		print '%s已刷满' % word
		browser.delete_all_cookies()
		browser.quit()
		continue
	else: 
		try:
			print 'user agent: %s' % useragent

			'''设置30s超时'''
			browser.implicitly_wait(10)

			browser.get("http://m.baidu.com")
			time.sleep(1)
			
			'''定位input元素'''
			# browser.find_element_by_id("index-kw").send_keys(word.decode('utf-8'))
			
			input_element_list = ['index-kw','word']
			for input_element in input_element_list:
				try:
					browser.find_element_by_id("%s" % input_element).is_displayed() 
				except:
					print '未找到%s，开始查找下一个input元素' % input_element
				else:
					#print '%s元素存在，跳出循环' % input_element
					input_dw = input_element
					break
			
			#print 'input'
			browser.find_element_by_id("%s" % input_dw).send_keys(word.decode('utf-8'))
			
			'''定位click元素'''
			#browser.find_element_by_id("index-bn").click()
			
			click_element_list = ['index-bn:id','ct_2:name']
			for click_element_trem in click_element_list:
				click_element = click_element_trem.split(':')[0]
				method = click_element_trem.split(':')[1]
				
				try:
					if method == 'id':
						browser.find_element_by_id("%s" % click_element).is_displayed() 
					else:
						browser.find_element_by_name("%s" % click_element).is_displayed() 
				except:
					print '未找到%s，开始查找下一个input元素' % click_element
				else:
					#print '%s元素存在，跳出循环' % click_element
					click_dw_trem = click_element_trem
					break
			
			time.sleep(1)
			
			#print 'click'
			if click_dw_trem.split(':')[1] == 'id':
				browser.find_element_by_id("%s" % click_dw_trem.split(':')[0]).click()
			else:
				browser.find_element_by_name("%s" % click_dw_trem.split(':')[0]).click()
			
					
			'''暂停3s'''
			time.sleep(5)

			'''定位搜索结果块级元素'''
			#number = len(browser.find_elements_by_class_name("result"))
			block_element_list = ['result','resitem','result']
			block_number = len(block_element_list)

			for block_element in block_element_list:
				try:
					browser.find_element_by_class_name("%s" % block_element).is_displayed()
					time.sleep(1)
				except:
					try:
						browser.find_element_by_id("se-bn").click()
					except:
						print '查找下一元素'
				else:
					#print '%s元素存在，跳出循环' % block_element
					block_dw = block_element
					break
			
			#print 'serp analytics'
			number = len(browser.find_elements_by_class_name("%s" % block_dw))
			#print '%s,%s' % (word,number)
	 		
			'''查看当前关键词是或否在第一页出现'''
			#print '查看关键词第一页是否出现'
			verify = 'no'
			rank = 0
			for i in range(1,number):
				lines = browser.find_elements_by_class_name("%s" % block_dw)
				rank += 1
				if domain in lines[i].text:
					verify = 'yes'
					break
				else:
					continue

			'''if判定，根据domain是否在第一页出现，执行不同动作'''
			if verify == 'yes':
				print '排在第一页，点击第一页结果'
				print '%s , rank one page , rank is %s' % (word,rank)

				for i in click_list_rank1[rank]:

					print '%s rank is %s , domain is %s , new click is result %s' % (word,rank,domain,i)

					b_tags = browser.find_elements_by_class_name("%s" % block_dw)
					tags = b_tags[int(i)]

					browser.implicitly_wait(10)
					tags.find_element_by_tag_name("a").click()
					time.sleep(5)
					browser.back()
					time.sleep(5)

					if i == rank:
						word_dict[word]['count'] = count + 1
						print '%s , succeed click %s num' % (word,word_dict[word]['count'])

			else:
				'''检测分页特征'''
				#print '检测第二页是否包含排名，开始点击下一页，进入第二页'
				browser.find_element_by_id('pagenav').click()
				time.sleep(3)

				number = len(browser.find_elements_by_class_name("%s" % block_dw))
				rank = 0
				for i in range(1,number):
					lines = browser.find_elements_by_class_name("%s" % block_dw)
					rank += 1
					if domain in lines[i].text:
						verify = 'yes'
						break
					else:
						continue

				if verify == 'yes':
					print '已确认排名第二页'
					print '%s , rank one page , rank is %s' % (word,rank)

					for i in click_list_rank1[rank]:

						print '%s rank is %s , domain is %s , new click is result %s' % (word,rank,domain,i)
						browser.find_element_by_id('pagenav').click()
						time.sleep(3)
						b_tags = browser.find_elements_by_class_name("%s" % block_dw)
						tags = b_tags[int(i)]

						browser.implicitly_wait(10)
						tags.find_element_by_tag_name("a").click()
						time.sleep(5)
						browser.back()		
						time.sleep(5)

						if i == rank:
							word_dict[word]['count'] = count + 1
							print '%s , succeed click %s num' % (word,word_dict[word]['count'])	

				else:
					print 'word不在前两页，放弃点击'
					browser.delete_all_cookies()
					browser.quit()
					continue
				
		except:
			print 'error'
			browser.delete_all_cookies()	
			browser.quit()
			continue

	browser.delete_all_cookies()
	browser.quit()

	'''执行adsl拨号'''
	# export = Adsl()
	# export.reconnect()
	
	
	# sleep = int(wait())
	# print '>>>>>>>>>等待%ss>>>>>>>>>' % sleep
	# time.sleep(sleep)
