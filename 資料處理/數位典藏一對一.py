from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 翻譯研究.讀語料 import 讀語料
from 資料處理.產生一對一 import 產生一對一

class 數位典藏一對一(產生一對一):
	__分析器=拆文分析器()
	__語料=讀語料()
	def 檔案合起來(self,型檔案,音檔案,一對一檔名):
		閩南語字=self.__語料.讀語料檔案(型檔案)
		閩南語音=self.__語料.讀語料檔案(音檔案)
		結果=[]
		逝數=0
		for 型,音 in zip(閩南語字,閩南語音):
			print(逝數)
			型=' '+型+' '
			音=' '+音+' '
			型陣列=self.__分析器.拆章做句(型)
			音陣列=self.__分析器.拆章做句(音)
			if len(型陣列)!=len(音陣列):
				型陣列=音陣列
			for 型,音 in zip(型陣列,音陣列):
				try:
					結果.append(self.合起來(型, 音))
				except:
					結果.append(self.合起來(音, 音))
			逝數+=1
		self.__語料.寫語料檔案(一對一檔名, '\n'.join(結果))
		return

if __name__=='__main__':
	一對一=數位典藏一對一()
	一對一.檔案合起來("../語料/臺語文數位典藏漢羅文.txt.gz",
				"../語料/臺語文數位典藏全羅文.txt.gz",
				"../語料/臺語文數位典藏一對一.txt.gz")
	