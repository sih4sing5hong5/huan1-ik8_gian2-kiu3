import json
from 處理TGB.提掉網頁標仔工具 import 提掉網頁標仔工具
from 處理TGB.提掉文章標仔工具 import 提掉文章標仔工具
import gzip
from 分言語.語言判斷 import 判斷
from 處理TGB.資料檔 import 資料檔

class 解析TGB:
	__資料檔=資料檔()
	def 段落字分析(self, json檔名, 分數檔名):
		全部 = self.__資料檔.讀(json檔名)
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
	def 國閩分數(self, 國閩句檔名, 分數檔名):
		國語句, 漢羅句 = self.__資料檔.讀(國閩句檔名)
		問題 = []
		答案 = []
		for 一逝 in 國語句[:5]:
			問題.append(判斷.分數(一逝))
			答案.append(0)
		for 一逝 in 漢羅句[:5]:
			問題.append(判斷.分數(一逝))
			答案.append(1)
		self.__資料檔.寫(分數檔名, (問題, 答案))

if __name__ == '__main__':
	TGB = 解析TGB()
# 	TGB.段落字分析('../語料/TGB/原來TGB.json.gz', '../語料/TGB/分數.json.gz')
# 	TGB.分國閩句('../語料/TGB/分數.json.gz', '../語料/TGB/國閩句.json.gz')
	TGB.國閩分數('../語料/TGB/國閩句.json.gz', '../語料/TGB/逐句訓練分數.json.gz')
