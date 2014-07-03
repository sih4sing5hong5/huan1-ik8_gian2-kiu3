# -*- coding: utf-8 -*-
from html.parser import HTMLParser

class 提掉文章標仔工具(HTMLParser):
	剖析結果 = []
	def __init__(self):
		super(提掉文章標仔工具, self).__init__()
		self.剖析結果 = []
	def handle_starttag(self, tag, attrs):
		if tag == 'hr':
			self.剖析結果.append('<hr>')
	def handle_endtag(self, tag):
		if tag == 'p':
			self.剖析結果.append('\n')
	def handle_data(self, data):
		self.剖析結果.append(data)
	def 結果(self):
		規的文章 = ''.join(self.剖析結果)
		整理過文章 = []
		for 一逝 in 規的文章.split('\n'):
			無雙空白逝 = ' '.join(一逝.split())
			# <span>5--</span>月
			# 24冬過--去-a
			處理輕聲字 = 無雙空白逝.replace('- ', '-').replace(' -', '-')
			if len(處理輕聲字)>0:
				整理過文章.append(處理輕聲字)
		return '\n'.join(整理過文章)
