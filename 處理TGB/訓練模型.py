import json
from 處理TGB.提掉網頁標仔工具 import 提掉網頁標仔工具
from 處理TGB.提掉文章標仔工具 import 提掉文章標仔工具
import gzip
from 分言語.語言判斷 import 判斷
import os
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.斷詞.中研院工具.斷詞結構化工具 import 斷詞結構化工具
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 處理TGB.資料檔 import 資料檔
from sklearn.lda import LDA

class 訓練模型:
	__資料檔 = 資料檔()
	def 訓練(self, 分數檔名):
		問題, 答案 = self.__資料檔.讀(分數檔名)
		訓練問題 = []
		from sklearn import svm
		前幾常用 = 1000
# 		問題=問題[:-213]#+問題[-213:]
# 		答案=答案[:-213]#+答案[-213:]
		for 問 in 問題:
			訓練問題.append(問[0:14] + 問[14:14 + 前幾常用] + 問[1014:1014 + 前幾常用])
# 			print(len(問),訓練問題[-1])
		import numpy as np
		sample_weight_constant = np.ones(len(問題))
# 		sample_weight_constant[-213:] *= 10
		clf = svm.SVC(C=1)
		lda = LDA()
# 		clf = svm.NuSVC()
		lda.fit(訓練問題, 答案)
		clf.fit(lda.transform(訓練問題), 答案, sample_weight=sample_weight_constant)
		試驗函式 = lambda 問:clf.predict(lda.transform(問))
		結果 = 試驗函式(訓練問題)
		毋著 = 0
		第幾个 = 0
		for 結, 答 in zip(結果, 答案):
			if 結 != 答:
				print(結, 答, 第幾个)
				毋著 += 1
			第幾个 += 1
		print(毋著, len(答案))
		return 試驗函式
	def 試驗(self,句對應分數檔名,函式):
		句對應分數 =self.__資料檔.讀(句對應分數檔名)
		分類={0:[],1:[],2:[]}
		段資料=[]
		分數資料=[]
		for 段,分數 in 句對應分數.items():
			段資料.append(段)
			分數資料.append(分數)
		for 段,結果 in zip(段資料,函式(分數資料)):
			分類[結果].append(段)
		print(分類[0][:10])
		print(分類[1][:10])
		print(分類[2][:10])

if __name__ == '__main__':
	TGB = 訓練模型()
	試驗函式=TGB.訓練('../語料/TGB/逐句訓練分數.json.gz')
	TGB.試驗('../語料/TGB/全部句分數.json.gz', 試驗函式)
