import json
from 處理TGB.提掉網頁標仔工具 import 提掉網頁標仔工具
from 處理TGB.提掉文章標仔工具 import 提掉文章標仔工具
import gzip
from 分言語.語言判斷用戶端 import 判斷
import os
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.斷詞.中研院工具.斷詞結構化工具 import 斷詞結構化工具
from 臺灣言語工具.字詞組集句章.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 臺灣言語工具.字詞組集句章.解析整理.文章粗胚 import 文章粗胚

class 解析TGB:
	__斷詞剖析工具 = 官方斷詞剖析工具()
	__斷詞結構化工具 = 斷詞結構化工具()
	__譀鏡=物件譀鏡()
	__粗胚 = 文章粗胚()
	def 段落字分析(self, json檔名, 分數檔名):
		json檔案 = gzip.open(json檔名, 'rt')
		全部 = json.loads(json檔案.read())
		json檔案.close()
		分數狀況 = []
		for 資料 in 全部:
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
			for 段 in 文章:
				分數 = (判斷.有偌濟漢字(段),) + 判斷.有偌濟音標(段)
				分數狀況.append({
					'網址':資料['url'],
					'標題':標題工具.結果(),
					'發表日':時間工具.結果(),
					'第幾段':第幾段,
					'攏總幾段':len(文章),
					'內容':段.strip(),
					'分數': 分數
					})
				第幾段 += 1
# 			print(分數狀況[-1])
		分數檔案 = gzip.open(分數檔名, 'wt')
		json.dump(分數狀況, 分數檔案)
		分數檔案.close()
		print(len(全部))
	def 分國閩句(self, 分數檔名, 國閩句檔名):
		分數檔案 = gzip.open(分數檔名, 'rt')
		全部 = json.load(分數檔案,)
		分數檔案.close()

# 					'網址':資料['url'],
# 					'標題':標題工具.結果(),
# 					'發表日':時間工具.結果(),
# 					'第幾段':第幾段,
# 					'攏總幾段':len(文章),
# 					'內容':段.strip(),
# 					'分數': 分數
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
						if 判斷.有偌濟音標(一逝)[0]>0.1:
							漢羅句.append(一逝)
		國閩句檔案 = gzip.open(國閩句檔名, 'wt')
		json.dump((國語句, 漢羅句), 國閩句檔案)
		國閩句檔案.close()
# 		print(國語句[:5])
# 		print(漢羅句[:5])
# 		print('\n'.join(國語句[:]),file=open('../國語句.txt','w'))
# 		print('\n'.join(漢羅句[:]),file=open('../漢羅句.txt','w'))
	def 國閩分數(self, 國閩句檔名,分數檔名 ):
		國閩句檔案 = gzip.open(國閩句檔名, 'rt')
		國語句, 漢羅句 = json.load(國閩句檔案,)
		國閩句檔案.close()
		問題=[]
		答案=[]
		for 一逝 in 國語句:
			問題.append(判斷.閩南語相關分數(一逝))
			答案.append(0)
		for 一逝 in 漢羅句:
			問題.append(判斷.閩南語相關分數(一逝))
			答案.append(1)
		分數檔案 = gzip.open(分數檔名, 'wt')
		json.dump((問題, 答案), 分數檔案)
		分數檔案.close()
	def 國語斷詞(self, 分數檔名,斷詞檔名, ):
		分數檔案 = gzip.open(分數檔名, 'rt')
		全部  = json.load(分數檔案,)
		分數檔案.close()
		if os.path.isfile(斷詞檔名):
			斷詞檔案 = gzip.open(斷詞檔名, 'rt')
			斷詞  = json.load(斷詞檔案,)
			斷詞檔案.close()
		else:
			斷詞  = {}
		猶未斷=set()
		for 資料 in 全部:
			國語, 教羅, 通用 = 資料['分數']
			for 一逝 in 資料['內容'].split('\n'):
				一逝=一逝.strip()
				if 一逝!='':
					if 一逝 not in 斷詞:
						猶未斷.add(一逝)
		for 一逝 in 猶未斷:
			try:
				處理減號 = self.__粗胚.建立物件語句前處理減號(教會羅馬字音標, 一逝)
				斷詞結果 = self.__斷詞剖析工具.斷詞(處理減號,等待=3.0)
			except Exception as 問題:
				print(問題)
			else:
				章物件 = self.__斷詞結構化工具.斷詞轉章物件(斷詞結果)
				斷了=self.__譀鏡.看型(章物件, 物件分字符號='', 物件分詞符號=' ')
				斷詞[一逝]=斷了
# 				print('haha',斷了)
		斷詞檔案 = gzip.open(斷詞檔名, 'wt')
		json.dump(斷詞, 斷詞檔案)
		斷詞檔案.close()

if __name__ == '__main__':
	TGB = 解析TGB()
# 	TGB.段落字分析('../語料/TGB/原來TGB.json.gz', '../語料/TGB/分數.json.gz')
# 	TGB.分國閩句('../語料/TGB/分數.json.gz', '../語料/TGB/國閩句.json.gz')
	TGB.國語斷詞('../語料/TGB/分數.json.gz','../語料/TGB/斷詞.json.gz')
# 	TGB.國閩分數('../語料/TGB/國閩句.json.gz','../語料/TGB/逐句訓練分數.json.gz')
