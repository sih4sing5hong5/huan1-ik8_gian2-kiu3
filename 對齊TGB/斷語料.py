from 分言語.語言判斷 import 判斷
from 處理TGB.資料檔 import 資料檔
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 翻譯研究.讀語料 import 讀語料
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.基本元素.公用變數 import 分詞符號
import os
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
import time

class 斷語料:
	_資料檔 = 資料檔()
	_讀語料 = 讀語料()
	_粗胚 = 文章粗胚()
	斷詞 = {}
	_判斷 = 判斷
	_譀鏡 = 物件譀鏡()
	_篩仔 = 字物件篩仔()
	def 對齊前處理華語(self, 編號):
		國語檔案 = '../語料/TGB/分開/{0:04}.國'.format(編號)
		閩南語檔案 = '../語料/TGB/分開/{0:04}.閩'.format(編號)
		if os.path.isfile(國語檔案) and os.path.isfile(閩南語檔案):
			國語斷詞 = []
			for 國語 in 	self._讀語料.讀語料檔案(國語檔案):
				物件 = self._判斷.標好國語(國語)
				國語斷詞.append(self._譀鏡.看分詞(物件))
			self._讀語料.寫語料檔案('../語料/TGB/分開對齊/{0:04}.華'.format(編號),
						'\n'.join(國語斷詞))
	def 對齊前處理閩南語(self, 編號):
		國語檔案 = '../語料/TGB/分開/{0:04}.國'.format(編號)
		閩南語檔案 = '../語料/TGB/分開/{0:04}.閩'.format(編號)
		if os.path.isfile(國語檔案) and os.path.isfile(閩南語檔案):
			閩南語斷詞 = []
			for 閩南語 in self._讀語料.讀語料檔案(閩南語檔案):
				處理減號 = self._粗胚.建立物件語句前處理減號(教會羅馬字音標, 閩南語)
				閩南語分數 = self._判斷.閩南語分數(處理減號)
				斷詞物件 = 閩南語分數[0]
				閩南語斷詞.append(self._譀鏡.看分詞(斷詞物件))
			self._讀語料.寫語料檔案('../語料/TGB/分開對齊/{0:04}.閩'.format(編號),
						'\n'.join(閩南語斷詞))

if __name__ == '__main__':
	TGB = 斷語料()
	for 編號 in range(1179):
		print(編號, time.ctime())
		TGB.對齊前處理華語(編號)
		TGB.對齊前處理閩南語(編號)
