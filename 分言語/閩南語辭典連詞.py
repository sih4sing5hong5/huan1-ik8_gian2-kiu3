import re
from 翻譯研究.讀語料 import 讀語料
import os
from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.標音.語句連詞 import 語句連詞
import pickle
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.斷詞.中研院工具.斷詞結構化工具 import 斷詞結構化工具
from 臺灣言語工具.字詞組集句章.解析整理.物件譀鏡 import 物件譀鏡
import gzip
from 校對.公家辭典連詞 import 公家辭典連詞

class 閩南語辭典連詞:
	def 產生(self):
		辭典連詞 = 公家辭典連詞()
		辭典, 連詞 = 辭典連詞.產生()
		擺 = 5
		華臺 = '../華臺/{0:02}.訓.華臺一對一斷詞.txt.gz'.format(擺)
		典藏 = '../典藏/{0:02}.臺語文典藏典藏一對一.txt.gz'.format(擺)
		辭典連詞.加一个檔案(辭典, 連詞, 華臺)
		辭典連詞.加一个檔案(辭典, 連詞, 典藏)
		return 辭典, 連詞

if __name__ == '__main__':
	辭典, 連詞 = 閩南語辭典連詞().產生()
	閩南語辭典連詞檔案 = gzip.open('閩南語辭典連詞.pickle.gz', 'wb')
	pickle.dump((辭典, 連詞), 閩南語辭典連詞檔案,
			protocol = pickle.HIGHEST_PROTOCOL)
	閩南語辭典連詞檔案.close()
