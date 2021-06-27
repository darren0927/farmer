# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from lxml import html
from urllib.request import urlretrieve

import requests
import urllib3


class Farmer(object):
    def __init__(self, url):
        self.url = url

    def get_source_page(self):
        """
        返回经过lxml.html.fromstring 模块处理的<Element html at 0x36e8278>
        可以用 XPath 来过滤数据
        """
        try:
            response = urllib3.urlopen(self.url, timeout=3).read()
            selector = html.fromstring(response)
        except Exception as e:
            print('获取网页内容报错 %s' % str(e))
            selector = None
        finally:
            return selector

    def work(self):
        """ 获取妹子图片链接 """
        html_content = requests.get(self.url).text
        soup = BeautifulSoup(html_content, 'lxml')
        mm_img_content = soup.find_all('div', {"class": "list"})
        for ul in mm_img_content:
            mm_img_list = ul.find_all('img')
            for img in mm_img_list:
                url = img['src']
                r = requests.get(url, stream=True)
                image_name = url.split('/')[-1]
                print('mm图片 %s' % url)
                print('mm图片name %s' % image_name)
        return


f = Farmer('http://www.netbian.com/s/qingchunmeinv/index.htm')
f.work()
