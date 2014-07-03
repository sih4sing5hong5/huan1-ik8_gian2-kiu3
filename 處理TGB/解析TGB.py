from 處理TGB.提掉網頁標仔工具 import 提掉網頁標仔工具
from 處理TGB.提掉文章標仔工具 import 提掉文章標仔工具
from 分言語.語言判斷 import 判斷
from 處理TGB.資料檔 import 資料檔
import os
from 臺灣言語工具.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
import re

class 解析TGB:
	__資料檔 = 資料檔()
	def 段落字分析(self, json檔名, 分數檔名):
		全部 = self.__資料檔.讀(json檔名)
		分數狀況 = []
		__粗胚 = 文章粗胚()
# 		h = html2text.HTML2Text()
# 		h.ignore_links = True
# 		h.ignore_emphasis=True
# 		h.ignore_images=True
# 		h.google_doc=False
		for 第幾篇, 資料 in enumerate(全部):
			標題工具 = 提掉網頁標仔工具()
			標題工具.feed(資料['title'][0])
# 			 print(標題工具.結果())
			時間工具 = 提掉網頁標仔工具()
			時間工具.feed(資料['date'][0])
# 			 print(時間工具.結果())
			文章工具 = 提掉文章標仔工具()
			文章工具.feed(資料['context'][0])
			文章 = 文章工具.結果().replace('³', '3').split('<hr>')
			第幾段 = 0
			for 第幾段, 段 in enumerate(文章):
				處理減號 = __粗胚.建立物件語句前處理減號(教會羅馬字音標, 段)
				分數 = (判斷.有偌濟漢字(處理減號),) + 判斷.有偌濟音標(處理減號)
				分數狀況.append({
					'網址':資料['url'],
					'標題':標題工具.結果(),
					'發表日':時間工具.結果(),
					'第幾段':第幾段,
					'攏總幾段':len(文章),
					'內容':段.strip(),
					'分數':分數
					})
# 			print(分數狀況[-1])
		self.__資料檔.寫(分數檔名, 分數狀況)
		print(len(全部))
	def 分國閩句(self, 分數檔名, 國閩句檔名):
		全部 = self.__資料檔.讀(分數檔名)
		國語句 = []
		漢羅句 = []
		for 資料 in 全部:
			國語, 教羅, 通用 = 資料['分數']
			for 一逝 in 資料['內容'].split('\n'):
				一逝 = 一逝.strip()
				if 一逝 != '':
					if 國語 > 0.2 and 教羅 < 0.001:
						國語句.append(一逝)
					elif 資料['攏總幾段'] > 1 and 教羅 > 0.1:
						if 判斷.有偌濟音標(一逝)[0] > 0.1:
							漢羅句.append(一逝)
		self.__資料檔.寫(國閩句檔名, (國語句, 漢羅句))
	def 國閩分數(self, 句對應分數檔名, 國閩句檔名, 分數檔名, 海東檔名):
		國語句, 漢羅句 = self.__資料檔.讀(國閩句檔名)
		if os.path.isfile(句對應分數檔名):
			句對應分數 = self.__資料檔.讀(句對應分數檔名)
		else:
			句對應分數 = {}
		問題 = []
		答案 = []
		for 一逝 in 國語句[:]:
			if 一逝 in 句對應分數:
				分數 = 句對應分數[一逝]
				print('cache')
			else:
				分數 = 判斷.分數(一逝)
				print('query', len(分數))
			問題.append(分數)
			答案.append(0)
		for 一逝 in 漢羅句[:]:
			if 一逝 in 句對應分數:
				分數 = 句對應分數[一逝]
			else:
				分數 = 判斷.分數(一逝)
			問題.append(分數)
			答案.append(1)
		for 一逝 in self.海東分析(海東檔名)[:]:
			if 一逝 in 句對應分數:
				分數 = 句對應分數[一逝]
			else:
				分數 = 判斷.分數(一逝)
			問題.append(分數)
			答案.append(2)
		self.__資料檔.寫(分數檔名, (問題, 答案))

	def 海東分析(self, 海東檔名):
		import html2text
		海東網頁 = self.__資料檔.讀(海東檔名)
		逝 = []
		for 資料 in 海東網頁:
			h = html2text.HTML2Text()
			h.ignore_links = True
			h.ignore_emphasis = True
			h.ignore_images = True
			h.google_doc = False
			上尾結果 = h.handle(資料['context']).strip().replace('\\-', '-')
			for 一逝 in 上尾結果.split('\n'):
				一逝 = 一逝.strip()
				if 一逝 != '':
					逝.append(一逝)
# 		print(len(逝))
		return 逝
	切標題 = re.compile('(.*)／(.*)[@＠](.*)')
	揣文章編號 = re.compile(r'/blog/post/(\d+)')
	def 提一逝一逝資料佮編出來(self, 分數檔名 = '../語料/TGB/分數.json.gz'):
		排好順序 = {}
		全部 = self.__資料檔.讀(分數檔名)
		for 資料 in 全部:
# 			http://taioanchouhap.pixnet.net/blog/post/49196746/%20
			if not 資料['網址'][-3].isdigit():
				continue
			網址 = int(self.揣文章編號.search(資料['網址']).group(1))
			if 網址 not in 排好順序:
				排好順序[網址] = [0] * (1 + 資料['攏總幾段'])
			排好順序[網址][資料['第幾段'] + 1] = 資料['內容']
			if 資料['第幾段'] == 0:
				標題 = 資料['標題']
				結果 = self.切標題.split(標題)
				if len(結果) == 5 and 結果[1] != '' and 結果[2] != '':
					排好順序[網址][0] = \
						'\n'.join([結果[1], 結果[2]])
				else:
					排好順序[網址][0] = 標題.strip()
		for 編號, 資料 in sorted(排好順序.items()):
# 			print(編號, 資料)
			for 區 in 資料:
				for 一逝 in 區.split('\n'):
					一逝 = 一逝.strip()
					if 一逝 != '':
						yield 編號, 一逝
	def 提一逝一逝資料出來(self, 分數檔名 = '../語料/TGB/分數.json.gz'):
		for 編號, 一逝 in self.提一逝一逝資料佮編出來(分數檔名):
			yield 一逝

def _main():
	TGB = 解析TGB()
	TGB.段落字分析('../語料/TGB/原來TGB.json.gz', '../語料/TGB/分數.json.gz')
# 	TGB.分國閩句('../語料/TGB/分數.json.gz', '../語料/TGB/國閩句.json.gz')
# 	TGB.國閩分數('../語料/TGB/全部句分數.json.gz',
# 			'../語料/TGB/國閩句.json.gz',
# 			'../語料/TGB/逐句訓練分數.json.gz',
# 			'../語料/TGB/原來Hai2Tong1.json.gz')
# 	TGB.海東分析('../語料/TGB/原來Hai2Tong1.json.gz')

import cProfile
if __name__ == '__main__':
	cProfile.run('_main()')
