import gzip
import pickle
import os
import unicodedata
from 臺灣言語工具.字詞組集句章.基本元素.公用變數 import 統一碼漢字佮組字式類
from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.字詞組集句章.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.通用拼音音標 import 通用拼音音標
from build.lib.臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from build.lib.臺灣言語工具.斷詞.中研院工具.斷詞結構化工具 import 斷詞結構化工具
from build.lib.臺灣言語工具.標音.動態規劃標音 import 動態規劃標音
from build.lib.臺灣言語工具.斷詞.動態規劃斷詞 import 動態規劃斷詞

class 語言判斷:
	國語連詞 = None
	閩南語辭典 = None
	閩南語連詞 = None
	__分析器 = 拆文分析器()
	__篩仔 = 字物件篩仔()
	__斷詞剖析工具 = 官方斷詞剖析工具()
	__斷詞結構化工具 = 斷詞結構化工具()
	__標音 = 動態規劃標音()
	__斷詞=動態規劃斷詞()
	def 載入(self, 國語連詞檔名, 閩南語辭典連詞檔名):
		if os.path.isfile(國語連詞檔名):
			辭典連詞檔案 = gzip.open(國語連詞檔名, 'rb')
			self.國語連詞 = pickle.load(辭典連詞檔案)
			辭典連詞檔案.close()
		if os.path.isfile(閩南語辭典連詞檔名):
			閩南語辭典連詞檔案 = gzip.open(閩南語辭典連詞檔名, 'rb')
			self.閩南語辭典, self.閩南語連詞 = pickle.load(閩南語辭典連詞檔案)
			閩南語辭典連詞檔案.close()
	def 分數(self, 語句):
		return (self.國語分數(語句),self.閩南語分數(語句),\
			self.有偌濟漢字(語句),)+self.有偌濟音標(語句)
	def 有偌濟漢字(self, 語句):
		漢字 = 0
		for 字 in 語句:
			if unicodedata.category(字) in 統一碼漢字佮組字式類:
				漢字 += 1
		return 漢字 / len(語句)
	def 有偌濟音標(self, 語句):
		教羅 = 0
		通用 = 0
		組物件 = self.__分析器.建立組物件(語句)
		字陣列 = self.__篩仔.篩出字物件(組物件)
		for 字物件 in 字陣列:
			if 教會羅馬字音標(字物件.型).音標 != None:
				教羅 += 1
			if 通用拼音音標(字物件.型).音標 != None:
				通用 += 1
		return 教羅 / len(字陣列), 通用 / len(字陣列),
	def 國語分數(self, 語句):
		斷詞結果 = self.__斷詞剖析工具.斷詞(語句, 一定愛成功 = True)
		組物件 = self.__斷詞結構化工具.斷詞轉組物件(斷詞結果)
		標好, 分數, 詞數 = self.__標音.標音(self.國語連詞, 組物件)
		return 分數
	def 閩南語分數(self, 語句):
		組物件 = self.__分析器.建立組物件(語句)
		斷好, 分數, 詞數 = self.__斷詞.斷詞(self.閩南語辭典, 組物件)
		標好, 分數, 詞數 = self.__標音.標音(self.閩南語連詞, 斷好)
		return 分數
if __name__ == '__main__':
	判斷 = 語言判斷()
	偌濟漢字 = 判斷.有偌濟漢字('中研院連詞.pickle.gz閩南語辭典連詞.pickle.gz')
	print(偌濟漢字)
	偌濟音標 = 判斷.有偌濟音標('chhu1 tsha hi5 gha1')
	print(偌濟音標)
# 	判斷.載入('中研院連詞.pickle.gz', '閩南語辭典連詞.pickle.gz')
