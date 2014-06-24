from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 翻譯研究.讀語料 import 讀語料
from 資料處理.產生一對一 import 產生一對一
from 校對.公家辭典連詞 import 公家辭典連詞
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.基本元素.公用變數 import 標點符號

class 數位典藏一對一(產生一對一):
	_分析器 = 拆文分析器()
	_語料 = 讀語料()
	_公家辭典連詞 = 公家辭典連詞()
	_篩仔 = 字物件篩仔()
	_譀鏡 = 物件譀鏡()
	def 檔案合起來(self, 型檔案, 音檔案, 一對一檔名):
		閩南語字 = self._語料.讀語料檔案(型檔案)
		閩南語音 = self._語料.讀語料檔案(音檔案)
		結果 = []
		逝數 = 0
		for 型, 音 in zip(閩南語字, 閩南語音):
			print(逝數)
			型 = ' ' + 型 + ' '
			音 = ' ' + 音 + ' '
			型陣列 = self._分析器.拆章做句(型)
			音陣列 = self._分析器.拆章做句(音)
			if len(型陣列) != len(音陣列):
				型陣列 = 音陣列
			for 型, 音 in zip(型陣列, 音陣列):
				try:
					結果.append(self.合起來(型, 音))
				except:
					結果.append(self.合起來(音, 音))
			逝數 += 1
		self._語料.寫語料檔案(一對一檔名, '\n'.join(結果))
		return
	def 檔案合起來而且無愛無佇辭典的字(self, 型檔案, 音檔案, 一對一檔名):
		閩南語字 = self._語料.讀語料檔案(型檔案)
		閩南語音 = self._語料.讀語料檔案(音檔案)
		結果 = []
		逝數 = 0
# 		辭典, 連詞=self._公家辭典連詞.讀文件產生()
		辭典 = self._公家辭典連詞.產生()[0]
		for 型, 音 in zip(閩南語字, 閩南語音):
			print(逝數)
			型 = ' ' + 型 + ' '
			音 = ' ' + 音 + ' '
			型陣列 = self._分析器.拆章做句(型)
			音陣列 = self._分析器.拆章做句(音)
			if len(型陣列) != len(音陣列):
				章物件 = self.辭典對齊(辭典, 型, 音)
				結果.extend(章物件.內底句)
			for 型, 音 in zip(型陣列, 音陣列):
				章物件 = self.辭典對齊(辭典, 型, 音)
				結果.extend(章物件.內底句)
			逝數 += 1
		斷詞格式=[]
		for 句物件 in 結果: 
			斷詞格式.append(self._譀鏡.看斷詞(句物件, 物件分型音符號='｜'))
		self._語料.寫語料檔案(一對一檔名, '\n'.join(斷詞格式))
		return
	def 辭典對齊(self, 辭典, 型, 音):
		型物件 = self._分析器.建立章物件(型)
		型字陣列 = self._篩仔.篩出字物件(型物件)
		音物件 = self._分析器.建立章物件(音)
		音字陣列 = self._篩仔.篩出字物件(音物件)
		表 = []
		表.append([(0, 0)] * (1 + len(音字陣列)))
		for 型字 in 型字陣列:
			表.append([(0, 0)])
			for 音字 in 音字陣列:
# 				print(self.佇辭典內底(辭典, 型字.型, 音字.型), 型字.型, 音字.型)
				if self.佇辭典內底(辭典, 型字.型, 音字.型):
					倒爿面頂 = 表[-2][len(表[-1]) - 1]
					表[-1].append((倒爿面頂[0] + 1, 1))
				else:
					面頂 = 表[-2][len(表[-1])]
					倒爿 = 表[-1][-1]
					if 面頂[0] >= 倒爿[0]:
						表[-1].append((面頂[0], 2))
					else:
						表[-1].append((倒爿[0], 3))
		型所在 = len(表) - 1
		音所在 = len(表[-1]) - 1
		while 型所在 > 0 and 音所在 > 0:
			方向 = 表[型所在][音所在][1]
			if 方向 == 1:
				音字陣列[音所在 - 1].音 = 音字陣列[音所在 - 1].型
				音字陣列[音所在 - 1].型 = 型字陣列[型所在 - 1].型
				型所在 -= 1
				音所在 -= 1
			elif 方向 == 2:
				型所在 -= 1
			elif 方向 == 3:
				音字陣列[音所在 - 1].音 = 音字陣列[音所在 - 1].型
				音所在 -= 1
			else:
				raise RuntimeError('程式有問題')
# 		print(型, 音)
# 		print(self._譀鏡.看斷詞(音物件))
		return 音物件
	def 佇辭典內底(self, 辭典, 型, 音):
		if 型 == 音:
			return True
		if 型 in 標點符號 and 音 in 標點符號:
			return True
		try:
			字物件 = self._分析器.產生對齊字(型, 音)
			詞物件 = self._分析器.建立詞物件('')
			詞物件.內底字 = [字物件]
			結果 = 辭典.查詞(詞物件)
			if len(結果[0]) > 0:
				return True
			else:
				return False
		except:
			return False
	'''
	試驗：	
	一般
		稽 考 在 早 tsiah4 e5 博 學 e5 人 ，
		khe1-kho2 tsai7-tsa2 tsiah4-e5 phok4-hak8 e5 lang5 ,
		khe1-考｜kho2 在-早｜tsai7-tsa2 tsiah4-e5｜tsiah4-e5 博-學｜phok4-hak8 e5｜e5 人｜lang5 ，｜,
	漢羅詞
		攏 總 會 曉 tit4 寫 批 ，
		long2-tsong2 ue7-hiau2-tit4 sia2 phue1 ,
		攏-總｜long2-tsong2 會-曉-tit4｜ue7-hiau2-tit4 寫｜sia2 批｜phue1 ，｜,
	毋著字
		看 見 園 丁 企 hi2 路 邊 ，
		khuann3-kinn3 hng5-ting1 khia7 hi2 loo7-pinn1 ,
		看-見｜khuann3-kinn3 園-丁｜hng5-ting1 khia7｜khia7 hi2｜hi2 路-邊｜loo7-pinn1 ，｜,  
	型音數量無對齊
	數字 
'''
if __name__ == '__main__':
	一對一 = 數位典藏一對一()
# 	一對一.檔案合起來("../語料/臺語文數位典藏漢羅文.txt.gz",
# 				"../語料/臺語文數位典藏全羅文.txt.gz",
# 				"../語料/臺語文數位典藏一對一.txt.gz")
	一對一.檔案合起來而且無愛無佇辭典的字("../語料/臺語文數位典藏漢羅文.txt.gz",
				"../語料/臺語文數位典藏全羅文.txt.gz",
				"../語料/臺語文數位典藏一對一.txt.gz")
	
