
from 處理TGB.資料檔 import 資料檔
import re
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 翻譯研究.讀語料 import 讀語料
from 處理TGB.解析TGB import 解析TGB

class 分TGB語料:
	_資料檔 = 資料檔()
	_讀語料 = 讀語料()
	_粗胚 = 文章粗胚()
	解析 = 解析TGB()
	def 分國閩句(self, 分數檔名, 國語檔, 閩南檔):
		國語句 = set(self._讀語料.讀語料檔案(國語檔))
		閩南句 = set(self._讀語料.讀語料檔案(閩南檔))
		全部 = self._資料檔.讀(分數檔名)
		分析 = {}
		for 編號, 逝 in self.解析.提一逝一逝資料佮編出來(分數檔名):
			if 編號 not in 分析:
				分析[編號] = {'國語':[], '閩南語':[]}
			if 逝 in 國語句:
				分析[編號]['國語'].append(逝)
			elif 逝 in 閩南句:
				分析[編號]['閩南語'].append(逝)
			else:
				print(逝)
		編號 = 0
		for 網址, 分開 in sorted(分析.items()):
			國 = '\n'.join(分開['國語'])
			閩 = '\n'.join(分開['閩南語'])
			for 文, 類 in zip([國, 閩], ['國', '閩']):
				if 文 != '':
					檔 = open('../語料/TGB/分開/{0:04}.{1}'.format(編號, 類), 'w')
					print(文, file = 檔)
					檔.close()
			編號 += 1

if __name__ == '__main__':
	TGB = 分TGB語料()
# 	TGB.段落字分析('../語料/TGB/原來TGB.json.gz', '../語料/TGB/分數.json.gz')
	TGB.分國閩句('../語料/TGB/分數.json.gz',
		'../語料/TGB/分國閩/國語.gz',
		'../語料/TGB/分國閩/閩南.gz')
