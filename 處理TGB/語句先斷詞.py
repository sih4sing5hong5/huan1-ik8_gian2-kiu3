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
	def 國語斷詞(self, 分數檔名,):
		全部 = self.__資料檔.讀(分數檔名)
		猶未斷 = set()
		TGB=解析TGB()
		for 一逝 in TGB.提一逝一逝資料出來(分數檔名):
			猶未斷.add(一逝)
		print('猶未斷',len(猶未斷))
		for 一逝 in 猶未斷:
			判斷.分數(一逝)
	def 全部句分數(self, 分數檔名, 海東檔名, 句對應分數檔名):
		解析 = 解析TGB()
		全部句 = set(解析.提一逝一逝資料出來(分數檔名))
		for 一逝 in 解析.海東分析(海東檔名):
			全部句.add(一逝)
		if os.path.isfile(句對應分數檔名):
			句對應分數 = self.__資料檔.讀(句對應分數檔名)
		else:
			句對應分數 = {}
		print('全部有：',len(全部句),'已經有:', len(句對應分數))
		for 一逝 in 全部句:
			if 一逝 not in 句對應分數:
				句對應分數[一逝] = 判斷.分數(一逝)

if __name__ == '__main__':
	TGB = 語句先斷詞()
# 	TGB.國語斷詞('../語料/TGB/分數.json.gz',)
	TGB.全部句分數('../語料/TGB/分數.json.gz',
			'../語料/TGB/原來Hai2Tong1.json.gz',
			'../語料/TGB/全部句分數.json.gz')
