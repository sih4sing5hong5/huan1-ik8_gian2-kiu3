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
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.斷詞.型音辭典 import 型音辭典
from 臺灣言語工具.斷詞.動態規劃斷詞 import 動態規劃斷詞

class 對摩西翻譯改斷字:
	語料 = None
	對齊語料對應表 = None
	對齊片語表 = None
	辭典對應表 = None
	字典對應表 = None
	連詞 = None
	__分析器 = 拆文分析器()
	__粗胚 = 文章粗胚()
	用戶端 = None
	def 載入(self):
		self.語料 = 讀語料()
		self.用戶端 = 摩西用戶端('localhost', '8101')
		
	def 試驗(self):
		斷詞工具 = 動態規劃斷詞()
		標音工具 = 動態規劃標音()
		譀鏡 = 物件譀鏡()
		結果檔案 = open('試驗結果斷字閣組.txt', 'w')
		for 一逝, 斷詞組國語 in zip(self.語料.讀語料檔案('../語料/試.國語字斷字.txt'),
			self.語料.讀語料檔案('../語料/試.國語字.txt')):
# 			print(一逝)
			翻譯結果 = self.用戶端.翻譯(一逝, 另外參數={'nbest':1})
			for 上好句 in 翻譯結果['nbest']:
				這馬國語字數 = 0
				這馬閩南語詞組 = 0
				上好句詞陣列 = 上好句['hyp'].strip().split('  ')
				規句陣列 = []
				for 一詞組 in 斷詞組國語.split():
					這馬國語字數 += len(一詞組)
					閩南語詞組 = []
					while 這馬閩南語詞組 < len(上好句['align']) and\
						上好句['align'][這馬閩南語詞組]['src-end'] < 這馬國語字數:
						閩南語詞組.append(上好句詞陣列[這馬閩南語詞組])
						這馬閩南語詞組 += 1
					if 閩南語詞組!=[]:
						規句陣列.append('-'.join(閩南語詞組).replace(' ', '-'))
				print(上好句['hyp'])
				print(上好句詞陣列)
				print(斷詞組國語)
				print(' '.join(規句陣列))
				print(' '.join(規句陣列), file=結果檔案)
# 				print((上好句['hyp'].split('  ')))
# 				print(len(上好句['hyp'].strip().split('  ')),len(上好句['align']))
				if(len(上好句['hyp'].strip().split('  ')) != len(上好句['align'])):
					raise
				
# 			print(譀鏡.看型(上好物件, 物件分字符號='-', 物件分詞符號=' '))
# 			結果文句=' '.join(結果)
# 			print(結果文句)
# 			print(結果文句, file=結果檔案)

		結果檔案.close()

if __name__ == '__main__':
	翻譯研究 = 對摩西翻譯改斷字()
	翻譯研究.載入()
	翻譯研究.試驗()
