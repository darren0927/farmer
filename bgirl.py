# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

import requests

g_url = "http://www.netbian.com/s/qingchunmeinv/index.htm"
html = requests.get(g_url).text
soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('div', {"class": "list"})

for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        print('美图链接 %s' % url)
        print('美图name %s' % image_name)

        '''
        1、使用urlretrieve下载
        urlretrieve(IMAGE_URL, '/Users/tandong/beautiful/image1.png')
        '''

        '''
        2、第二种下载方式
        with open('/Users/tandong/beautiful/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)
        '''
