from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
import sys
from 分言語.語言判斷模型 import 無例句訓練的語料
from 臺灣言語工具.斷詞.連詞揀集內組 import 連詞揀集內組
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
import os
import gzip
import pickle
from 分言語.語言判斷模型 import 閩南語辭典連詞
from 臺灣言語工具.表單.肯語句連詞 import 肯語句連詞

class 斷一對一詞:
	__分析器 = 拆文分析器()
	__譀鏡 = 物件譀鏡()
	__篩仔 = 字物件篩仔()
	def __init__(self):
		if os.path.isfile(閩南語辭典連詞):
			閩南語辭典連詞檔案 = gzip.open(閩南語辭典連詞, 'rb')
			self.辭典, 閩南語連詞檔 = pickle.load(閩南語辭典連詞檔案)
			閩南語辭典連詞檔案.close()
			self.連詞 = 肯語句連詞(閩南語連詞檔)
		self.動態斷詞 = 拄好長度辭典揣詞()
		self.動態標音 = 連詞揀集內組()
	def 斷詞(self, 一對一):
		標準句物件 = self.__分析器.轉做組物件(一對一)
		斷詞句物件, 分數, 詞數 = self.動態斷詞.揣詞(self.辭典, 標準句物件)
		標音句物件, 分數, 詞數 = self.動態標音.揀(self.連詞, 斷詞句物件)
		return self.__譀鏡.看分詞(標音句物件)

if __name__ == '__main__':
	if not 無例句訓練的語料:
		raise RuntimeError('資料袂使有例句!!')
	斷 = 斷一對一詞()
	try:
		for 一逝 in sys.stdin:
			一逝 = 一逝.strip()
			print(斷.斷詞(一逝))
	except:
		pass
