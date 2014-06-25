from 處理TGB.資料檔 import 資料檔
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 翻譯研究.讀語料 import 讀語料
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 翻譯研究.一逝翻譯 import 一逝翻譯
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器

class 對齊語料:
	_資料檔 = 資料檔()
	_讀語料 = 讀語料()
	_分析器 = 拆文分析器()
	_粗胚 = 文章粗胚()
	_譀鏡 = 物件譀鏡()

	_編碼器 = 語句編碼器()
	翻做國語埠 = 8301
	翻做國語用戶端 = None
	def __init__(self):
		self.翻做閩南 = 一逝翻譯(8205, 8105)
		self.翻做國語用戶端 = 摩西用戶端('localhost', self.翻做國語埠)
	def 產生翻譯(self, 編號):
		國語翻閩南語 = []
		for 國語斷詞 in 	self._讀語料.讀語料檔案('../語料/TGB/分開對齊/{0:04}.國'.format(編號)):
			翻譯結果 = self.翻做閩南.譯(國語斷詞)
			print(翻譯結果)
			國語翻閩南語.append(翻譯結果)
		閩南語翻國語 = []
		for 閩南語斷詞 in self._讀語料.讀語料檔案('../語料/TGB/分開對齊/{0:04}.閩'.format(編號)):
			翻譯結果 = self.翻做國語用戶端.翻譯(
				閩南語斷詞, self._編碼器,)
			整理結果 = []
			for 國語詞 in 翻譯結果['text'].split():
				if self.翻做國語用戶端.是未知詞(國語詞):
					閩南語分詞 = self.翻做國語用戶端.提掉後壁未知詞記號(國語詞)
					詞物件 = self._分析器.轉做詞物件(閩南語分詞)
					整理結果.append(self._譀鏡.看型(詞物件))
				else:
					整理結果.append(國語詞)
			閩南語翻國語.append(' '.join(整理結果))
# 講-來｜kong2-lai5|UNK|UNK|UNK
			print(閩南語翻國語[-1])

if __name__ == '__main__':
	TGB = 對齊語料()
# 	TGB.段落字分析('../語料/TGB/原來TGB.json.gz', '../語料/TGB/分數.json.gz')
	TGB.產生翻譯(1166)
