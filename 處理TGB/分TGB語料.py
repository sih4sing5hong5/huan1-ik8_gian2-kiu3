import json
from 處理TGB.提掉網頁標仔工具 import 提掉網頁標仔工具
from 處理TGB.提掉文章標仔工具 import 提掉文章標仔工具
import gzip
from 分言語.語言判斷 import 判斷
from 處理TGB.資料檔 import 資料檔
import os
import re
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標

class 分TGB語料:
	__資料檔 = 資料檔()
	__粗胚 = 文章粗胚()
	def 分國閩句(self, 分數檔名):
		全部 = self.__資料檔.讀(分數檔名)
		切標題 = re.compile('(.*)／(.*)@(.*)')
		狀況 = {}
		分析 = {}
		for 資料 in 全部:
			無空白=[]
			for 逝 in 資料['內容'].split('\n'):
				逝=逝.strip()
				if 逝!='':
					無空白.append(逝)
			資料['內容']='\n'.join(無空白)
			標題 = 資料['標題']
			結果 = 切標題.split(標題)
			網址 = 資料['網址']
			if 網址 not in 分析:
				分析[網址] = {'國語':[], '閩南語':[]}
			分開 = 分析[網址]
			if 資料['攏總幾段'] > 1:
				國語, 教羅, 通用 = 資料['分數']
				if 國語 > 0.2 and 教羅 < 0.02:
					分開['國語'].append(資料['內容'])
				elif 教羅 > 0.1:
					分開['閩南語'].append(資料['內容'])
				else:
					國語票, 閩南語票 = self.一逝一逝投票(資料['內容'])
							
# 					狀況[(國語票, 閩南語票,)] = 1
					if 閩南語票 >= 3 and 國語票 > 閩南語票:
						國語逝, 閩南語逝, 毋知逝 = self.一逝一逝分開(資料['內容'])
						分開['閩南語'].append('\n'.join(閩南語逝))
						分開['國語'].append('\n'.join(國語逝))
# 						print('\n'.join(毋知逝))
# 						print(國語票, 閩南語票)
					elif 國語票 > 閩南語票:
						分開['國語'].append(資料['內容'])
					else:
						分開['閩南語'].append(資料['內容'])
			else:
				國語票, 閩南語票 = self.一逝一逝投票(資料['內容'])
				try:
					狀況[(國語票, 閩南語票,)] += 1
				except:
					狀況[(國語票, 閩南語票,)] = 1
				if 閩南語票 >= 5 and 國語票 <= 1:
					分開['閩南語'].append(資料['內容'])
				elif 國語票 >= 5 and 閩南語票 <= 1:
					分開['國語'].append(資料['內容'])
				else:
					國語逝, 閩南語逝, 毋知逝 = self.一逝一逝分開(資料['內容'])
					分開['閩南語'].append('\n'.join(閩南語逝))
					分開['國語'].append('\n'.join(國語逝))
# 					print('\n'.join(毋知逝))
		國集, 閩集 = [], []
		編號 = 0
		for 網址, 分開 in 分析.items():
			國 = '\n'.join(分開['國語'])
			閩 = '\n'.join(分開['閩南語'])
			國集.append(國)
			閩集.append(閩)
			for 文, 類 in zip([國, 閩], ['國', '閩']):
				if 文!='':
					檔 = open('../語料/TGB/分開/{0:04}.{1}'.format(編號, 類), 'w')
					print(文, file=檔)
					檔.close()
			編號 += 1
		
		for 文, 類 in zip([國集, 閩集], ['國', '閩']):
			檔 = open('../語料/TGB/分開/{1}'.format(編號, 類), 'w')
			print('\n'.join(文), file=檔)
			檔.close()
		for a, b in 狀況.items():
			print (a, b)
# 		self.__資料檔.寫(國閩句檔名, (國語句, 漢羅句))
	def 一逝一逝投票(self, 規區):
		國語票 = 0
		閩南語票 = 0
		for 一逝 in 規區.split('\n'):
			一逝 = 一逝.strip()
			if 一逝 != '':
				處理減號 = self.__粗胚.建立物件語句前處理減號(教會羅馬字音標, 一逝)
				國語 = 判斷.有偌濟漢字(處理減號)
				教羅, 通用 = 判斷.有偌濟音標(處理減號)
				if 國語 > 0.2 and 教羅 < 0.001:
					國語票 += 1
				elif 教羅 > 0.1:
					閩南語票 += 1
		return 國語票, 閩南語票
	def 一逝一逝分開(self, 規區):
		國語逝 = []
		閩南語逝 = []
		毋知逝 = []
		for 一逝 in 規區.split('\n'):
			一逝 = 一逝.strip()
			if 一逝 != '':
				處理減號 = self.__粗胚.建立物件語句前處理減號(教會羅馬字音標, 一逝)
				國語 = 判斷.有偌濟漢字(處理減號)
				教羅, 通用 = 判斷.有偌濟音標(處理減號)
				if 國語 > 0.2 and 教羅 < 0.02:
					國語逝.append(一逝)
				elif 教羅 > 0.02:
					閩南語逝.append(一逝)
				else:
					毋知逝.append(一逝)
		return 國語逝, 閩南語逝, 毋知逝

if __name__ == '__main__':
	TGB = 分TGB語料()
# 	TGB.段落字分析('../語料/TGB/原來TGB.json.gz', '../語料/TGB/分數.json.gz')
	TGB.分國閩句('../語料/TGB/分數.json.gz')
