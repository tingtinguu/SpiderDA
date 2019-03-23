'''
Created on 2018年7月13日
微博爬虫
@author: woshiuu
'''
import sys
import urllib3
import requests
from lxml import etree

def Weibocrawler(userid, cookie):
    
    user_id = userid
    mycookie = str(cookie)
    urllib3.disable_warnings()
    cookie = {"Cookie":mycookie}
    url = 'http://weibo.cn/u/%d?filter=1&page=1'%user_id
    html = requests.get(url, cookies = cookie, verify = False).content
    print('user_id和cookie读入成功')
    selector = etree.HTML(html)
    word_count = 1
    sys.stdout.flush()
    result = ""
    # times = 5
    for page in range(1, 4):
        #获取lxml页面
        try:
            url = 'http://weibo.cn/u/%d?filter=1&page=%d'%(user_id,page) 
            lxml = requests.get(url, cookies = cookie, verify = False).content
            #文字爬取
            selector = etree.HTML(lxml)#获取网页
            content = selector.xpath('//span[@class="ctt"]')#获取微博
            for each in content:            
                text = each.xpath('string(.)')
                if word_count >= 4:
#                     text = "%d: "%(word_count-3) +text+"\r\n"
                    text = text+"\r\n"
                else :
                    text = text+"\r\n"
                result = result + text
                word_count += 1
                        
            print(page,'word ok')
            sys.stdout.flush()
        except:
            print(page,'error')
        print(page, 'sleep')
    sys.stdout.flush()
    print(result)
    return result