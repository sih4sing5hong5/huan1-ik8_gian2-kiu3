# -*- coding: utf-8 -*-
import json
import urllib.request
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.表單.實際語句連詞 import 實際語句連詞
from 翻譯研究.讀語料 import 讀語料
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
import pickle
import os
from 臺灣言語工具.斷詞.連詞揀集內組 import 連詞揀集內組
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.表單.型音辭典 import 型音辭典
from 臺灣言語工具.斷詞.辭典揣詞 import 辭典揣詞

class 揣出翻毋好的句:
	def 比較(self,來源檔名,標準答案檔名,試驗檔名,摩西檔名,門檻=0.5):
		語料=讀語料()
		來源陣列=語料.讀語料檔案(來源檔名)
		標準答案陣列=語料.讀語料檔案(標準答案檔名)
		試驗陣列=語料.讀語料檔案(試驗檔名)
		摩西陣列=語料.讀語料檔案(摩西檔名)
		for 來源,標準,試驗,摩西 in zip(來源陣列,標準答案陣列,試驗陣列,摩西陣列):
			試驗=試驗.replace('-',' ')
			答案=self.二元連接(標準.split())
			試驗連接=self.二元連接(試驗.split())
			if len(答案)==0:
				continue
			有著=0
			for 試 in 試驗連接:
				if 試 in 答案:
					有著+=1
			if 有著/len(答案)<門檻:
				print(有著/len(答案))
				print(來源)
				print(標準)
				print(試驗)
				print(摩西)
	def 二元連接(self,詞組陣列):
		答案=[]
		頂一个=None
		for 詞組 in 詞組陣列:
			答案.append((頂一个,詞組))
			頂一个=詞組
		return 答案

if __name__ == '__main__':
	翻毋好的句 = 揣出翻毋好的句()
	翻毋好的句.比較('../語料/試.國語字.txt','../語料/試.閩南語音斷字.txt',
		'試驗結果.txt','../基準/moses試驗結果.txt')
# 	翻毋好的句.比較('../語料/試.國語字斷字.txt','../語料/試.閩南語音斷字.txt',
# 		'../基準/moses試驗結果斷字.txt','../基準/moses試驗結果斷字.txt')
# 	翻毋好的句.比較('../語料/試.國語字.txt','../語料/試.閩南語音斷字.txt',
# 		'試驗結果斷詞.txt','試驗結果.txt',)#'../基準/moses試驗結果斷詞.txt')
