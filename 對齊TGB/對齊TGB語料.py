from 分言語.語言判斷 import 判斷
from 處理TGB.資料檔 import 資料檔
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 翻譯研究.讀語料 import 讀語料
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡

class 對齊TGB語料:
	_資料檔 = 資料檔()
	_讀語料 = 讀語料()
	_粗胚 = 文章粗胚()
	斷詞={}
	_判斷 = 判斷
	_譀鏡=物件譀鏡()
	def 對齊前處理(self, 編號):
		國語斷詞=[]
		for 國語 in 	self._讀語料.讀語料檔案('../語料/TGB/分開/{0:04}.國'.format(編號)):
			國語斷詞.append(self._判斷.斷詞[國語])
		閩南語斷詞=[]
		for 閩南語 in self._讀語料.讀語料檔案('../語料/TGB/分開/{0:04}.閩'.format(編號)):
			處理減號 = self._粗胚.建立物件語句前處理減號(教會羅馬字音標, 閩南語)
			閩南語分數=self._判斷.閩南語分數(處理減號)
			print(self._譀鏡.看斷詞(閩南語分數[0]))

if __name__ == '__main__':
	TGB = 對齊TGB語料()
# 	TGB.段落字分析('../語料/TGB/原來TGB.json.gz', '../語料/TGB/分數.json.gz')
	TGB.對齊前處理(1179)
