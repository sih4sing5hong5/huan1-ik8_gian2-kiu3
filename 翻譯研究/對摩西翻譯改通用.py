# -*- coding: utf-8 -*-
from 翻譯研究.對摩西翻譯改 import 對摩西翻譯改

class 對摩西翻譯改通用(對摩西翻譯改):
	埠 = None
	結果檔名 = None
	試驗檔名 = None
	
# mosesserver -f 閩南語斷詞/model/moses.ini --server-port 8201
# mosesserver -f 國語斷詞組/model/moses.ini --server-port 8202
# mosesserver -f 閩南語斷詞組/model/moses.ini --server-port 8203
# mosesserver -f 國語斷詞組閩南語斷詞/model/moses.ini --server-port 8204
# mosesserver -f 國語斷詞閩南語斷詞組/model/moses.ini --server-port 8205
if __name__ == '__main__':
	翻譯研究 = 對摩西翻譯改通用()
	翻譯研究.埠 = 8201
	翻譯研究.結果檔名 = '試驗結果-閩南語斷詞.txt'
	翻譯研究.試驗檔名 = '../語料/試.國語字斷字.txt'
# 	翻譯研究.埠 = 8202
# 	翻譯研究.結果檔名 = '試驗結果-國語斷詞組.txt'
# 	翻譯研究.試驗檔名 = '../語料/試.國語字.txt'
# 	翻譯研究.埠 = 8203
# 	翻譯研究.結果檔名 = '試驗結果-閩南語斷詞組.txt'
# 	翻譯研究.試驗檔名 = '../語料/試.國語字斷字.txt'
# 	翻譯研究.埠 = 8204
# 	翻譯研究.結果檔名 = '試驗結果-國語斷詞組閩南語斷詞.txt'
# 	翻譯研究.試驗檔名 = '../語料/試.國語字.txt'
# 	翻譯研究.埠 = 8205
# 	翻譯研究.結果檔名 = '試驗結果-國語斷詞閩南語斷詞組.txt'
# 	翻譯研究.試驗檔名 = '../語料/試.國語字斷詞.txt'
	翻譯研究.載入()
	翻譯研究.試驗()
