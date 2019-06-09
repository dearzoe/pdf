#!/usr/bin/python
#coding:utf-8

"""
@author: wenzhe
@software: PyCharm
@file: getCmaps.py
@time: 2019/6/9 4:07 PM
"""


import requests
from bs4 import BeautifulSoup

class Cmaps(object):
	def __init__(self):
		self.base_url = "https://unpkg.com/pdfjs-dist@2.0.943/cmaps/"
		self.down_url = self.base_url + "{}/"
		self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
		self.data_list = []
		self.url_obj = {}

	# 获取url字典
	def get_url_obj(self):
		bs4_data = BeautifulSoup(self.send_request(self.base_url), 'lxml')
		cmaps_doms = bs4_data.select('tr td.css-172zwq0 a')
		for cmaps in cmaps_doms:
			if(cmaps.get('href') != '../'):
				self.url_obj[cmaps.get('href')] = self.down_url.format(cmaps.get('href'))

	# 获取页面数据
	def send_request(self, url):
		data = requests.get(url, headers=self.headers).content.decode('utf-8')
		return data

	# 保存字体
	def save_data(self, path):
		# 写入文件 这样些不用打开关闭文件
		downPath = './camps/{}'.format(path)
		print('正在下载' + path + '字体')
		with open(downPath, 'wb') as f:
			f.write(requests.get(self.url_obj[path]).content)
			pass

	# 开始
	def satrt(self):
		self.get_url_obj()
		for cur_path in self.url_obj:
			self.save_data(cur_path)
		print('字体下载完成')

Cmaps().satrt()
