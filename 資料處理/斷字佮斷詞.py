# -*- coding: utf-8 -*-
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.斷詞.中研院工具.斷詞結構化工具 import 斷詞結構化工具
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 翻譯研究.讀語料 import 讀語料
class 斷字佮斷詞:
	__語料=讀語料()
	def 處理漢字(self, 檔案名):
		原本檔案 = self.__語料.讀語料檔案(檔案名)
		斷詞剖析工具 = 官方斷詞剖析工具()
		結構化工具 = 斷詞結構化工具()
		譀鏡 = 物件譀鏡()
		斷字=[]
		斷詞=[]
		for 一逝 in 原本檔案:
			while True:
				try:
					詞組 = 一逝.split()
					無斷 = ''.join(詞組)
					斷詞結果 = 斷詞剖析工具.斷詞(無斷, 等待=10)
					斷詞章物件 = 結構化工具.斷詞轉章物件(斷詞結果)
				except:
					pass
				else:
					斷字.append(譀鏡.看型(斷詞章物件, 物件分字符號='-', 物件分詞符號=' '))
					斷詞.append(譀鏡.看型(斷詞章物件, 物件分詞符號=' '))
					break
		self.__語料.寫語料檔案(檔案名.replace('.txt', '斷字.txt'),
				'\n'.join(斷字))
		self.__語料.寫語料檔案(檔案名.replace('.txt', '斷詞.txt'),
				'\n'.join(斷詞))
	def 處理漢字斷字(self, 檔案名):
		原本檔案 = open(檔案名)
		斷字檔案 = open(檔案名.replace('.txt', '斷字.txt'), 'w')
		for 一逝 in 原本檔案:
			詞組 = 一逝.split()
			無斷 = ''.join(詞組)
			斷字 = ' '.join(無斷)
			print(斷字, file=斷字檔案)
		原本檔案.close()
		斷字檔案.close()
	def 處理音標斷字(self, 檔案名):
		原本檔案 = self.__語料.讀語料檔案(檔案名)
		斷字資料=[]
		for 一逝 in 原本檔案:
			詞組 = 一逝.replace('-', ' ').split()
			斷字 = ' '.join(詞組)
			斷字資料.append(斷字)
		self.__語料.寫語料檔案(檔案名.replace('.txt', '斷字.txt'),
				'\n'.join(斷字資料))
	
if __name__ == '__main__':
	斷字詞 = 斷字佮斷詞()
	斷字詞.處理漢字('../語料/訓.國語字.txt')
	斷字詞.處理漢字('../語料/試.國語字.txt')
	斷字詞.處理漢字斷字('../語料/訓.國語字.txt')
	斷字詞.處理漢字斷字('../語料/試.國語字.txt')
	斷字詞.處理漢字('../語料/訓.例句國語字.txt.gz')
	斷字詞.處理漢字('../語料/試.例句國語字.txt.gz')
	
	斷字詞.處理音標斷字('../語料/訓.華臺閩南語音.txt.gz')
	斷字詞.處理音標斷字('../語料/試.華臺閩南語音.txt.gz')
	
	斷字詞.處理音標斷字('../語料/訓.例句閩南語音.txt.gz')
	斷字詞.處理音標斷字('../語料/試.例句閩南語音.txt.gz')
	斷字詞.處理音標斷字('../語料/附錄句閩南語音.txt.gz')
