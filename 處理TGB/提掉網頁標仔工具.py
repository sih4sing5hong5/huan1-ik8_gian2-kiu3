# -*- coding: utf-8 -*-
from html.parser import HTMLParser

class 提掉網頁標仔工具(HTMLParser):
	剖析結果 = []
	def __init__(self):
		super(提掉網頁標仔工具, self).__init__()
		self.剖析結果 = []
	def handle_starttag(self, tag, attrs):
		pass
	def handle_endtag(self, tag):
		pass
	def handle_data(self, data):
		self.剖析結果.append(data.strip())
		self.剖析結果.append(' ')
	def 結果(self):
		return ''.join(self.剖析結果)
