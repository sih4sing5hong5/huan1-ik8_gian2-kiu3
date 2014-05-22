# -*- coding: utf-8 -*-
import json
import urllib.request
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.標音.語句連詞 import 語句連詞
from 翻譯研究.讀語料 import 讀語料
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
import pickle
import os
from 臺灣言語工具.標音.動態規劃標音 import 動態規劃標音
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.基本元素.句 import 句

class 翻譯:
	語料 = None
	對齊語料對應表 = None
	對齊片語表 = None
	辭典對應表 = None
	字典對應表 = None
	連詞 = None
	__分析器 = 拆文分析器()
	__粗胚 = 文章粗胚()
	def 載入(self):
		self.語料 = 讀語料()
		self.對齊語料對應表 = self.語料.產生對齊語料對應表(
			來源詞 = '../語料/訓.國語字_訓.閩南語音.trn.src.vcb',
			目標詞 = '../語料/訓.國語字_訓.閩南語音.trn.trg.vcb',
			機率表 = '../語料/訓.國語字_訓.閩南語音.t3.final')
		對齊片語表檔名 = '對齊片語表.pickle'
		if os.path.isfile(對齊片語表檔名):
			對齊片語表檔案 = open(對齊片語表檔名, 'rb')
			self.對齊片語表 = pickle.load(對齊片語表檔案)
			對齊片語表檔案.close()
		else:
			self.對齊片語表 = self.語料.產生對齊語料片語表('../語料/phrase-table.gz')
			對齊片語表檔案 = open(對齊片語表檔名, 'wb')
			pickle.dump(self.對齊片語表, 對齊片語表檔案, protocol = pickle.HIGHEST_PROTOCOL)
			對齊片語表檔案.close()

		辭典對應表模型檔名 = '辭典對應表.pickle'
		if os.path.isfile(辭典對應表模型檔名):
			辭典對應表模型檔案 = open(辭典對應表模型檔名, 'rb')
			教育部對應表 = pickle.load(辭典對應表模型檔案)
			辭典對應表模型檔案.close()
		else:
			教育部對應表 = self.語料.產生辭典對應表('/home/Ihc/git/temp/test/test3/結果.json')
			辭典對應表模型檔案 = open(辭典對應表模型檔名, 'wb')
			pickle.dump(教育部對應表, 辭典對應表模型檔案, protocol = pickle.HIGHEST_PROTOCOL)
			辭典對應表模型檔案.close()
		self.辭典對應表, self.字典對應表 = 教育部對應表
		語言模型檔名 = '語言模型檔名.pickle'
		if os.path.isfile(語言模型檔名):
			語言模型檔案 = open(語言模型檔名, 'rb')
			self.連詞 = pickle.load(語言模型檔案)
			語言模型檔案.close()
		else:
			self.連詞 = self.語料.讀語言模型檔案('../語料/訓.閩南語音.txt')
			語言模型檔案 = open(語言模型檔名, 'wb')
			pickle.dump(self.連詞, 語言模型檔案, protocol = pickle.HIGHEST_PROTOCOL)
			語言模型檔案.close()
	def 試驗(self):
		標音工具 = 動態規劃標音()
		譀鏡 = 物件譀鏡()
		結果檔案 = open('試驗結果.txt', 'w')
		for 一逝 in self.語料.讀語料檔案('../語料/試.國語字.txt'):
			全部句 = []
			self.得著全部翻譯句(一逝.split(), 0, [], 全部句)
			上好分數 = None
			上好物件 = None
			for 句物件 in 全部句:
				結果物件, 結果分數, 詞數 = 標音工具.標音(self.連詞, 全部句[0])
				if 上好分數 == None or 上好分數 < 結果分數:
					上好分數 = 結果分數
					上好物件 = 結果物件
			print(譀鏡.看型(上好物件, 物件分字符號 = '-', 物件分詞符號 = ' '))
			print(譀鏡.看型(上好物件, 物件分字符號 = '-', 物件分詞符號 = ' '), file = 結果檔案)

		結果檔案.close()
	def 得著全部翻譯句(self, 來源詞陣列, 所在, 集陣列, 全部句):
		if 所在 == len(來源詞陣列):
			全部句.append(句(集陣列))
			return
		有到後一步 = False
		for 尾 in range(所在 + 1, len(來源詞陣列) + 1)[::-1]:
			這段 = tuple(來源詞陣列[所在:尾])
			if 這段 in self.對齊片語表:
				有到後一步 = True
				集物件 = self.__分析器.建立集物件('')
				for 目標詞組, 機率 in self.對齊片語表[這段]:
					標準音 = self.__粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 目標詞組)
					組物件 = self.__分析器.建立組物件(標準音)
					組物件.內底詞[0].屬性 = {'機率':self.連詞.對數(機率)}
					集物件.內底組.append(組物件)
				集陣列.append(集物件)
				self.得著全部翻譯句(來源詞陣列, 尾, 集陣列, 全部句)
				集陣列.pop()
		if not 有到後一步:
			國語詞 = 來源詞陣列[所在]
			集物件 = self.__分析器.建立集物件('')
			if 國語詞 in self.對齊語料對應表:
				for 閩南語詞, 機率 in self.對齊語料對應表[國語詞]:
					組物件 = self.__分析器.建立組物件(閩南語詞)
					組物件.屬性 = {'機率':self.連詞.對數(float(機率))}
					集物件.內底組.append(組物件)
# 				print('對齊語料對應表',國語詞,對齊語料對應表[國語詞])
# 				print(集物件)
			elif 國語詞 in self.辭典對應表:
				for 閩南語詞 in self.辭典對應表[國語詞]:
					組物件 = self.__分析器.建立組物件(閩南語詞)
					集物件.內底組.append(組物件)
# 				print('辭典對應表',國語詞,辭典對應表[國語詞])
# 				print(集物件)
			elif 國語詞 in self.字典對應表:
				for 閩南語詞 in self.字典對應表[國語詞]:
					組物件 = self.__分析器.建立組物件(閩南語詞)
					集物件.內底組.append(組物件)
			else:
				組物件 = self.__分析器.建立組物件('字')
				組物件.內底詞[0].內底字[0].型 = 國語詞
				集物件.內底組.append(組物件)
			集陣列.append(集物件)
			self.得著全部翻譯句(來源詞陣列, 所在 + 1, 集陣列, 全部句)
			集陣列.pop()

if __name__ == '__main__':
	翻譯研究 = 翻譯()
	翻譯研究.載入()
	翻譯研究.試驗()
