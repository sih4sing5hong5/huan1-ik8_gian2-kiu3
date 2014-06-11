# -*- coding: utf-8 -*-
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.斷詞.中研院工具.斷詞結構化工具 import 斷詞結構化工具
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.斷詞.辭典揣詞 import 辭典揣詞
from 臺灣言語工具.斷詞.連詞揀集內組 import 連詞揀集內組
from 臺灣言語工具.表單.語句連詞 import 語句連詞
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.基本元素.公用變數 import 無音
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
	def 讀文件產生(self):
		辭典 = 型音辭典(4)
		self.__語料.產生辭典(辭典, '../語料/辭典一對一.txt.gz')
		self.__語料.產生辭典(辭典, '../語料/附錄句一對一斷詞.txt.gz')
		self.__語料.產生辭典(辭典, '../語料/訓.例句一對一斷詞.txt.gz')
# 		self.__語料.產生辭典(辭典, '../語料/訓.華臺一對一斷詞.txt.gz')
		連詞 = 語句連詞(3)
		self.__語料.產生連詞(連詞, '../語料/訓.例句一對一斷詞.txt.gz')
		self.__語料.產生連詞(連詞, '../語料/附錄句一對一斷詞.txt.gz')
		return 辭典, 連詞
	def 產生而且加一个檔案(self, 檔案):
		辭典, 連詞 = self.產生()
		self.加一个檔案(辭典, 連詞, 檔案)
		return 辭典, 連詞
	def 加一个檔案(self, 辭典, 連詞, 檔案):
		self.__語料.產生辭典(辭典, 檔案)
		self.__語料.產生連詞(連詞, 檔案)
		return 辭典, 連詞

