from 處理TGB.資料檔 import 資料檔
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 翻譯研究.讀語料 import 讀語料
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 翻譯研究.一逝翻譯 import 一逝翻譯
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 對齊TGB.翻譯評分對齊介面 import 翻譯評分對齊介面
import itertools
from 對齊TGB.空白斷詞分析器 import 空白斷詞分析器
from 臺灣言語工具.基本元素.公用變數 import 分詞符號
from 資料處理.斷一對一字 import 斷一對一字
import os

class 對齊語料:
	一擺上濟翻譯幾句 = 30
	_資料檔 = 資料檔()
	_讀語料 = 讀語料()
	_分析器 = 拆文分析器()
	_粗胚 = 文章粗胚()
	_譀鏡 = 物件譀鏡()
	_斷一對一字 = 斷一對一字()
	編碼器 = 語句編碼器()

	_翻譯評分對齊介面 = 翻譯評分對齊介面()
	翻做國語埠 = 8301
	翻做國語用戶端 = None
	國語檔名 = '../語料/TGB/分開對齊/{0:04}.國'
	閩南語檔名 = '../語料/TGB/分開對齊/{0:04}.閩'
	對齊段國語檔名 = '../語料/TGB/分開對齊/{0:04}.對齊段國語'
	對齊段閩南語檔名 = '../語料/TGB/分開對齊/{0:04}.對齊段閩南'
	對齊句國語檔名 = '../語料/TGB/分開對齊/{0:04}.對齊句國語'
	對齊句閩南語檔名 = '../語料/TGB/分開對齊/{0:04}.對齊句閩南'
	def __init__(self):
		self.翻做閩南 = 一逝翻譯(8205, 8105)
		self.翻做國語用戶端 = 摩西用戶端('localhost', self.翻做國語埠, 編碼器=self.編碼器)
	def 翻譯對齊(self, 國語資料, 閩南語資料, 對齊國語檔 = None, 對齊閩南語檔 = None):
		國語翻閩南語, 閩南語翻國語 = self.翻譯兩爿(
			國語資料, 閩南語資料)
		對齊國語資料, 對齊閩南語資料 = self.對齊兩爿(
			國語資料, 閩南語資料, 國語翻閩南語, 閩南語翻國語,
			對齊國語檔, 對齊閩南語檔)
		return 國語翻閩南語, 閩南語翻國語, 對齊國語資料, 對齊閩南語資料
	def 翻譯兩爿(self, 國語資料, 閩南語資料):
		國語翻閩南語 = []
		for 國語斷詞 in 國語資料	:
			翻譯結果 = self.翻做閩南.譯(國語斷詞)
			print(翻譯結果)
			國語翻閩南語.append(翻譯結果)
		閩南語翻國語 = []
		for 閩南語斷詞 in 閩南語資料:
			章物件 = self._分析器.轉做章物件(閩南語斷詞)
			國語詞陣列 = []
			for 所在 in range(0, len(章物件.內底句), self.一擺上濟翻譯幾句):
				愛翻譯章物件 = self._分析器.建立章物件('')
				愛翻譯章物件.內底句 = 章物件.內底句[所在:所在 + self.一擺上濟翻譯幾句]
				愛翻譯斷詞 = self._譀鏡.看分詞(愛翻譯章物件)
				翻譯結果 = self.翻做國語用戶端.翻譯(愛翻譯斷詞)
				國語詞陣列.extend(翻譯結果['text'].split())
			整理結果 = []
			for 國語詞 in 國語詞陣列:
				if self.翻做國語用戶端.是未知詞(國語詞):
					閩南語分詞 = self.翻做國語用戶端.提掉後壁未知詞記號(國語詞)
					詞物件 = self._分析器.轉做詞物件(閩南語分詞)
					整理結果.append(self._譀鏡.看型(詞物件))
				else:
					整理結果.append(國語詞)
			閩南語翻國語.append(' '.join(整理結果))
# 講-來｜kong2-lai5|UNK|UNK|UNK
			print(閩南語翻國語[-1])
		return 國語翻閩南語, 閩南語翻國語
	def 對齊兩爿(self, 國語資料, 閩南語資料,
			國語翻閩南語, 閩南語翻國語, 對齊國語檔, 對齊閩南語檔):
		return self._翻譯評分對齊介面.對齊(
			國語資料, 閩南語資料,
			[國語翻閩南語], [閩南語翻國語],
			對齊國語檔, 對齊閩南語檔)
	def 對齊一段一段(self, 編號):
		國語資料 = list(self._讀語料.讀語料檔案(self.國語檔名.format(編號)))
		閩南語資料 = list(self._讀語料.讀語料檔案(self.閩南語檔名.format(編號)))
		國語翻閩南語, 閩南語翻國語, 對齊國語資料, 對齊閩南語資料 = self.翻譯對齊(國語資料, 閩南語資料)
		self._讀語料.寫語料檔案(self.對齊段國語檔名.format(編號), 對齊國語資料.getvalue())
		self._讀語料.寫語料檔案(self.對齊段閩南語檔名.format(編號), 對齊閩南語資料.getvalue())
	def 對齊一逝一逝(self, 編號):
		對齊句國語 = open(self.對齊句國語檔名.format(編號), 'w')
		對齊句閩南語 = open(self.對齊句閩南語檔名.format(編號), 'w')
		for 國語分詞, 閩南分詞 in zip(
				self._讀語料.讀語料檔案(
					self.對齊段國語檔名.format(編號)),
				self._讀語料.讀語料檔案(
					self.對齊段閩南語檔名.format(編號))
				):
			_空白斷詞分析器 = 空白斷詞分析器()
			國語物件 = _空白斷詞分析器.切出章物件(國語分詞)
			國語句 = []
			for 句物件 in 國語物件.內底句:
				國語句.append(
					self._譀鏡.看型(句物件, 物件分詞符號 = 分詞符號))

			閩南物件 = self._分析器.轉做章物件(閩南分詞)
			閩南句 = []
			for 句物件 in 閩南物件.內底句:
				閩南句.append(self._譀鏡.看分詞(句物件))
			self.翻譯對齊(國語句, 閩南句, 對齊句國語, 對齊句閩南語)
		對齊句國語.close()
		對齊句閩南語.close()
	def 斷詞轉斷字(self, 斷詞, 斷字):
		斷字資料 = []
		for 一句 in self._讀語料.讀語料檔案(斷詞):
			斷字句 = self._斷一對一字.斷字(一句)
			斷字資料.append(斷字句)
		self._讀語料.寫語料檔案(斷字, '\n'.join(斷字資料))
if __name__ == '__main__':
	TGB = 對齊語料()
	for 編 in range(1179):
		print(編)
		if os.path.isfile(TGB.國語檔名.format(編)) and\
				os.path.isfile(TGB.閩南語檔名.format(編)):
			TGB.對齊一段一段(編)
			TGB.對齊一逝一逝(編)
