import gzip
import pickle
import os
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.斷詞.中研院工具.斷詞結構化工具 import 斷詞結構化工具
from 臺灣言語工具.斷詞.連詞揀集內組 import 連詞揀集內組
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
import Pyro4
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.表單.肯語句連詞 import 肯語句連詞
# 國語需要10G記憶體，載入愛4分鐘
# 閩南語需要5G，愛1分鐘
class 語言判斷模型:
	華語連詞 = None
	閩南語辭典 = None
	閩南語連詞 = None
	__粗胚 = 文章粗胚()
	__分析器 = 拆文分析器()
	__篩仔 = 字物件篩仔()
	__家私 = 轉物件音家私()
	__斷詞剖析工具 = 官方斷詞剖析工具()
	__斷詞結構化工具 = 斷詞結構化工具()
	__標音 = 連詞揀集內組()
	__斷詞 = 拄好長度辭典揣詞()
	def 載入(self, 華語連詞檔名, 閩南語辭典連詞檔名):
		if os.path.isfile(華語連詞檔名):
			self.華語連詞 = 肯語句連詞(華語連詞檔名)
		if os.path.isfile(閩南語辭典連詞檔名):
			閩南語辭典連詞檔案 = gzip.open(閩南語辭典連詞檔名, 'rb')
			self.閩南語辭典, 閩南語連詞檔 = pickle.load(閩南語辭典連詞檔案)
			閩南語辭典連詞檔案.close()
			self.閩南語連詞 = 肯語句連詞(閩南語連詞檔)
	def 國語分數(self, 章物件):
		標好, 分數, 詞數 = self.__標音.揀(self.華語連詞, 章物件)
		return 標好, 分數, 詞數
	def 閩南語分數(self, 標準組物件):
		斷好, 分數, 詞數 = self.__斷詞.揣詞(self.閩南語辭典, 標準組物件)
		標好, 分數, 詞數 = self.__標音.揀(self.閩南語連詞, 斷好, 揀幾个=125)
		return 標好, 分數, 詞數
	def 孤詞表(self):
		國語孤詞 = []
		for 詞, 機率 in self.華語連詞.連詞表.items():
			if len(詞) == 1:
				國語孤詞.append((詞[0], 機率))
		閩南語孤詞 = []
		for 詞, 機率 in self.閩南語連詞.連詞表.items():
			if len(詞) == 1:
				閩南語孤詞.append((詞[0], 機率))
		return 國語孤詞, 閩南語孤詞,
if __name__ == '__main__':
	判斷模型 = 語言判斷模型()
	判斷模型.載入('../語料/分言語/中研院連詞.lm', '../語料/分言語/閩南語辭典連詞.pickle.gz')
	Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')
	Pyro4.Daemon.serveSimple(
	{
		判斷模型: "判斷模型",
	}, ns=False, port=9091)
