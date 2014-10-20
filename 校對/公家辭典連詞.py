# -*- coding: utf-8 -*-
from 臺灣言語工具.表單.實際語句連詞 import 實際語句連詞
from 臺灣言語工具.表單.型音辭典 import 型音辭典
from 翻譯研究.讀語料 import 讀語料
import os
import pickle
class 公家辭典連詞:
	__語料 = 讀語料()
	def 產生(self):
		辭典連詞檔名 = '辭典連詞.pickle'
		if os.path.isfile(辭典連詞檔名):
			辭典連詞檔案 = open(辭典連詞檔名, 'rb')
			辭典, 連詞 = pickle.load(辭典連詞檔案)
			辭典連詞檔案.close()
		else:
			辭典, 連詞 = self.讀文件產生()
			辭典連詞檔案 = open(辭典連詞檔名, 'wb')
			pickle.dump((辭典, 連詞), 辭典連詞檔案,
					protocol = pickle.HIGHEST_PROTOCOL)
			辭典連詞檔案.close()
		return 辭典, 連詞
	def 讀文件產生(self, 辭典=型音辭典(4), 連詞=實際語句連詞(3)):
		self.__語料.產生辭典(辭典, '../語料/辭典一對一.txt.gz')
		self.__語料.產生辭典(辭典, '../語料/附錄句一對一斷詞.txt.gz')
# 		self.__語料.產生辭典(辭典, '../語料/訓.例句一對一斷詞.txt.gz')
# 		self.__語料.產生辭典(辭典, '../語料/訓.華臺一對一斷詞.txt.gz')

# 		self.__語料.產生連詞(連詞, '../語料/訓.例句一對一斷詞.txt.gz')
# 		self.__語料.產生連詞(連詞, '../語料/附錄句一對一斷詞.txt.gz')
		return 辭典, 連詞
	def 產生而且加一个檔案(self, 檔案):
		辭典, 連詞 = self.產生()
		self.加一个檔案(辭典, 連詞, 檔案)
		return 辭典, 連詞
	def 加一个檔案(self, 辭典, 連詞, 檔案):
		self.__語料.產生辭典(辭典, 檔案)
# 		self.__語料.產生連詞(連詞, 檔案)
		return 辭典, 連詞

