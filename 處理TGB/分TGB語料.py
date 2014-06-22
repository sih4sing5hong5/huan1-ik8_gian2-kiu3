import json
import gzip
from 處理TGB.資料檔 import 資料檔
import os
import re
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 翻譯研究.讀語料 import 讀語料

class 分TGB語料:
	_資料檔 = 資料檔()
	_讀語料 = 讀語料()
	_粗胚 = 文章粗胚()
	def 分國閩句(self, 分數檔名, 國語檔, 閩南檔):
		國語句 = set(self._讀語料.讀語料檔案(國語檔))
		閩南句 = set(self._讀語料.讀語料檔案(閩南檔))
		全部 = self._資料檔.讀(分數檔名)
		切標題 = re.compile('(.*)／(.*)@(.*)')
		狀況 = {}
		分析 = {}
		for 資料 in 全部:
			網址 = 資料['網址']
			if 網址 not in 分析:
				分析[網址] = {'國語':[], '閩南語':[]}
			分開 = 分析[網址]
# 			標題 = 資料['標題']
# 			結果 = 切標題.split(標題)
# 			if len(結果)==5:
# 				分開['國語'].append(結果[1])
# 				分開['閩南語'].append(結果[2])
			for 逝 in 資料['內容'].split('\n'):
				逝 = 逝.strip()
				if 逝 != '':
					if 逝 in 國語句:
						分開['國語'].append(逝)
					elif 逝 in 閩南句:
						分開['閩南語'].append(逝)
					else:
						print(逝)
		國集, 閩集 = [], []
		編號 = 0
		for 網址, 分開 in 分析.items():
			國 = '\n'.join(分開['國語'])
			閩 = '\n'.join(分開['閩南語'])
			國集.append(國)
			閩集.append(閩)
			for 文, 類 in zip([國, 閩], ['國', '閩']):
				if 文 != '':
					檔 = open('../語料/TGB/分開/{0:04}.{1}'.format(編號, 類), 'w')
					print(文, file = 檔)
					檔.close()
			編號 += 1

		for 文, 類 in zip([國集, 閩集], ['國', '閩']):
			檔 = open('../語料/TGB/分開/{1}'.format(編號, 類), 'w')
			print('\n'.join(文), file = 檔)
			檔.close()
		for a, b in 狀況.items():
			print (a, b)
if __name__ == '__main__':
	TGB = 分TGB語料()
# 	TGB.段落字分析('../語料/TGB/原來TGB.json.gz', '../語料/TGB/分數.json.gz')
	TGB.分國閩句('../語料/TGB/分數.json.gz',
		'../語料/TGB/分國閩/國語.gz',
		'../語料/TGB/分國閩/閩南.gz')
