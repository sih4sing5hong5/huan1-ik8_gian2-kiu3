import json
import gzip
import os
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.斷詞.中研院工具.斷詞結構化工具 import 斷詞結構化工具
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 處理TGB.資料檔 import 資料檔
from 分言語.語言判斷 import 判斷
from 處理TGB.解析TGB import 解析TGB

class 語句先斷詞:
	__斷詞剖析工具 = 官方斷詞剖析工具()
	__斷詞結構化工具 = 斷詞結構化工具()
	__譀鏡 = 物件譀鏡()
	__粗胚 = 文章粗胚()
	__資料檔 = 資料檔()
	def 國語斷詞(self, 分數檔名, 斷詞檔名,):
		全部 = self.__資料檔.讀(分數檔名)
		if os.path.isfile(斷詞檔名):
			斷詞 = self.__資料檔.讀(斷詞檔名)
		else:
			斷詞 = {}
		猶未斷 = set()
		for 資料 in 全部:
			國語, 教羅, 通用 = 資料['分數']
			for 一逝 in 資料['內容'].split('\n'):
				一逝 = 一逝.strip()
				if 一逝 != '':
					if 一逝 not in 斷詞:
						猶未斷.add(一逝)
		for 一逝 in 猶未斷:
			try:
				處理減號 = self.__粗胚.建立物件語句前處理減號(教會羅馬字音標, 一逝)
				斷詞結果 = self.__斷詞剖析工具.斷詞(處理減號, 等待 = 3.0)
			except Exception as 問題:
				print(問題)
			else:
				章物件 = self.__斷詞結構化工具.斷詞轉章物件(斷詞結果)
				斷了 = self.__譀鏡.看型(章物件, 物件分字符號 = '', 物件分詞符號 = ' ')
				斷詞[一逝] = 斷了
# 				print('haha',斷了)
		self.__資料檔.寫(斷詞檔名, 斷詞)

	def 全部句分數(self, 分數檔名, 海東檔名, 句對應分數檔名):
		全部 = self.__資料檔.讀(分數檔名)
		全部句 = set()
		for 資料 in 全部:
			國語, 教羅, 通用 = 資料['分數']
			for 一逝 in 資料['內容'].split('\n'):
				一逝 = 一逝.strip()
				if 一逝 != '':
					全部句.add(一逝)
		for 一逝 in 解析TGB().海東分析(海東檔名):
			全部句.add(一逝)
		print(len(全部句))
		句對應分數 = {}
		for 一逝 in 全部句:
			句對應分數[一逝] = 判斷.分數(一逝)
			if len(句對應分數) % 100 == 0:
				print('第', len(句對應分數), '句')
		self.__資料檔.寫(句對應分數檔名, 句對應分數)

if __name__ == '__main__':
	TGB = 語句先斷詞()
# 	TGB.國語斷詞('../語料/TGB/分數.json.gz', '../語料/TGB/斷詞.json.gz')
	TGB.全部句分數('../語料/TGB/分數.json.gz',
			'../語料/TGB/原來Hai2Tong1.json.gz',
			'../語料/TGB/全部句分數.json.gz')
