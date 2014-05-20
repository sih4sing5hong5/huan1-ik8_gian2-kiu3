import json
import gzip
import os
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.斷詞.中研院工具.斷詞結構化工具 import 斷詞結構化工具
from 臺灣言語工具.字詞組集句章.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 臺灣言語工具.字詞組集句章.解析整理.文章粗胚 import 文章粗胚

class 語句先斷詞:
	__斷詞剖析工具 = 官方斷詞剖析工具()
	__斷詞結構化工具 = 斷詞結構化工具()
	__譀鏡 = 物件譀鏡()
	__粗胚 = 文章粗胚()
	def 國語斷詞(self, 分數檔名, 斷詞檔名,):
		分數檔案 = gzip.open(分數檔名, 'rt')
		全部 = json.load(分數檔案,)
		分數檔案.close()
		if os.path.isfile(斷詞檔名):
			斷詞檔案 = gzip.open(斷詞檔名, 'rt')
			斷詞 = json.load(斷詞檔案,)
			斷詞檔案.close()
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
				斷詞結果 = self.__斷詞剖析工具.斷詞(處理減號, 等待=3.0)
			except Exception as 問題:
				print(問題)
			else:
				章物件 = self.__斷詞結構化工具.斷詞轉章物件(斷詞結果)
				斷了 = self.__譀鏡.看型(章物件, 物件分字符號='', 物件分詞符號=' ')
				斷詞[一逝] = 斷了
# 				print('haha',斷了)
		斷詞檔案 = gzip.open(斷詞檔名, 'wt')
		json.dump(斷詞, 斷詞檔案)
		斷詞檔案.close()

if __name__ == '__main__':
	TGB = 語句先斷詞()
	TGB.國語斷詞('../語料/TGB/分數.json.gz', '../語料/TGB/斷詞.json.gz')
