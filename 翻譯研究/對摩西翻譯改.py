# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 翻譯研究.讀語料 import 讀語料
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
import pickle
import os
from 臺灣言語工具.斷詞.連詞揀集內組 import 連詞揀集內組
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.翻譯.斷詞斷字翻譯 import 斷詞斷字翻譯

class 對摩西翻譯改:
	埠 = None
	結果檔名 = None
	試驗檔名 = None
	
	斷字埠 = None
	摩西揀幾个 = 0
	愛斷字 = False
	語料 = None
	對齊語料對應表 = None
	對齊片語表 = None
	辭典對應表 = None
	字典對應表 = None
	連詞 = None
	_分析器 = 拆文分析器()
	編碼器 = 語句編碼器()
	_斷詞斷字翻譯 = 斷詞斷字翻譯()
	def 載入(self):
		self.語料 = 讀語料()
# 		self.對齊語料對應表 = self.語料.產生對齊語料對應表(
# 			來源詞='../語料/訓.國語字_訓.閩南語音.trn.src.vcb',
# 			目標詞='../語料/訓.國語字_訓.閩南語音.trn.trg.vcb',
# 			機率表='../語料/訓.國語字_訓.閩南語音.t3.final')

# 		辭典對應表模型檔名 = '辭典對應表.pickle'
# 		if os.path.isfile(辭典對應表模型檔名):
# 			辭典對應表模型檔案 = open(辭典對應表模型檔名, 'rb')
# 			教育部對應表 = pickle.load(辭典對應表模型檔案)
# 			辭典對應表模型檔案.close()
# 		else:
# 			教育部對應表 = self.語料.產生辭典對應表(
# '../語料/教育部辭典對應詞結果.json')
# 			辭典對應表模型檔案 = open(辭典對應表模型檔名, 'wb')
# 			pickle.dump(教育部對應表, 辭典對應表模型檔案,
#  protocol=pickle.HIGHEST_PROTOCOL)
# 			辭典對應表模型檔案.close()
# 		self.辭典對應表, self.字典對應表 = 教育部對應表
		
		if self.摩西揀幾个 > 1:
			語言模型檔名 = '語言模型.pickle'
			if os.path.isfile(語言模型檔名):
				語言模型檔案 = open(語言模型檔名, 'rb')
				self.連詞 = pickle.load(語言模型檔案)
				語言模型檔案.close()
			else:
				self.連詞 = self.語料.讀語言模型檔案(
						'../語料/訓.閩南語音.txt')
				語言模型檔案 = open(語言模型檔名, 'wb')
				pickle.dump(self.連詞, 語言模型檔案,
						protocol=pickle.HIGHEST_PROTOCOL)
				語言模型檔案.close()
			
		self.斷詞用戶端 = 摩西用戶端('localhost', self.埠,編碼器=self.編碼器)
		self.斷字用戶端 = 摩西用戶端('localhost', self.斷字埠,編碼器=self.編碼器)
		
# 		self.辭典 = 型音辭典(4)
# 		for 型, 音陣列 in self.字典對應表.items():
# 			for 音 in 音陣列:
# 				組物件 = self._分析器.產生對齊組(型, 音)
# 				for 詞物件 in 組物件.內底詞:
# 					for 字物件 in 詞物件.內底字:
# 						暫 = 字物件.型
# 						字物件.型 = 字物件.音
# 						字物件.音 = 暫
# 					self.辭典.加詞(詞物件)
	def 試驗(self):
		譀鏡 = 物件譀鏡()
		篩仔 = 字物件篩仔()
		結果檔案 = open(self.結果檔名, 'w')
		for 一逝 in self.語料.讀語料檔案(self.試驗檔名)[:]:
# 			print(一逝)
			句物件=self._分析器.轉做句物件(一逝)
			上好物件 = self._斷詞斷字翻譯.譯句(
					self.斷詞用戶端, self.斷字用戶端,
					句物件, self.摩西揀幾个)
			if self.愛斷字:
				結果字陣列 = 篩仔.篩出字物件(上好物件)
				結果組物件 = self._分析器.建立組物件('')
				for 字物件 in 結果字陣列:
					結果詞物件 = self._分析器.建立詞物件('')
					結果詞物件.內底字 = [字物件]
					結果組物件.內底詞.append(結果詞物件)
				print(譀鏡.看分詞(結果組物件,
					物件分型音符號='｜', 物件分字符號='-', 物件分詞符號=' '))
				print(譀鏡.看分詞(結果組物件,
					物件分型音符號='｜', 物件分字符號='-', 物件分詞符號=' '),
				file=結果檔案)
			else:
				print(譀鏡.看分詞(上好物件,
					物件分型音符號='｜', 物件分字符號='-', 物件分詞符號=' '))
				print(譀鏡.看分詞(上好物件,
					物件分型音符號='｜', 物件分字符號='-', 物件分詞符號=' '),
				file=結果檔案)
