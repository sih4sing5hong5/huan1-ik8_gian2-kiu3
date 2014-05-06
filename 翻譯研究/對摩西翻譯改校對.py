# -*- coding: utf-8 -*-
from 翻譯研究.對摩西翻譯改 import 對摩西翻譯改
import sys

class 對摩西翻譯改通用(對摩西翻譯改):
	埠 = None
	斷字埠 = None
	試驗檔名 = None
	結果檔名 = None
	愛斷字 = False
	結果檔名樣版 = '{0}/結.{1:02}.閩南語試驗結果.txt'
	試驗檔名樣版 = '{0}/試.{1:02}.斷詞.試驗文本.txt'
	def __init__(self, 所在, 號):
		self.埠 = 8100 + 號
		self.斷字埠 = 8200 + 號
		self.試驗檔名 = self.試驗檔名樣版.format(所在, 號)
		self.結果檔名 = self.結果檔名樣版.format(所在, 號)
	
# mosesserver -f 閩南語斷詞/model/moses.ini --server-port 8201
# mosesserver -f 國語斷詞組/model/moses.ini --server-port 8202
# mosesserver -f 閩南語斷詞組/model/moses.ini --server-port 8203
# mosesserver -f 國語斷詞組閩南語斷詞/model/moses.ini --server-port 8204
# mosesserver -f 國語斷詞閩南語斷詞組/model/moses.ini --server-port 8205
if __name__ == '__main__':
	if len(sys.argv) == 1:
		for 擺 in range(1, 21):
			翻譯研究 = 對摩西翻譯改通用(擺)
			翻譯研究.載入()
			翻譯研究.試驗()
	else:
		翻譯研究 = 對摩西翻譯改通用(sys.argv[1], int(sys.argv[2]))
		翻譯研究.載入()
		翻譯研究.試驗()
