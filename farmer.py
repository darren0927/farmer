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
        try:
            response = urllib3.urlopen(self.url, timeout=3).read()
            selector = html.fromstring(response)
        except Exception as e:
            print('An error occurred while fetching the content of the page: %s' % str(e))
            selector = None
        finally:
            return selector

    def work(self):
        html_content = requests.get(self.url).text
        soup = BeautifulSoup(html_content, 'lxml', from_encoding="UTF-8")
        mm_img_content = soup.find_all('div', {"class": "list"})
        for ul in mm_img_content:
            mm_img_list = ul.find_all('img')
            for img in mm_img_list:
                url = img['src']
                r = requests.get(url, stream=True)
                image_name = url.split('/')[-1]
                print('the href of image is %s' % url)
                print('the name of image is %s' % image_name)
        return


f = Farmer('http://www.netbian.com/s/qingchunmeinv/index.htm')
f.work()
