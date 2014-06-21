from 分言語.語言判斷 import 判斷
from 處理TGB.資料檔 import 資料檔
from sklearn.lda import LDA
from 處理TGB.解析TGB import 解析TGB
import numpy as np
from sklearn import svm
from 翻譯研究.讀語料 import 讀語料

class 訓練模型:
	_資料檔 = 資料檔()
	_讀語料 = 讀語料()
	_解析TGB = 解析TGB()
	def 訓練(self, 分數檔名):
		問題, 答案 = self._資料檔.讀(分數檔名)
		訓練問題 = []
		前幾常用 = 1000
		for 問 in 問題:
			訓練問題.append(問[0:14] + 問[14:14 + 前幾常用] + 問[1014:1014 + 前幾常用])
		試驗函式 = self.LDA佮SVM模型(訓練問題, 答案)
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
	def LDA佮SVM模型(self, 問題, 答案):
		sample_weight_constant = np.ones(len(問題))
		clf = svm.SVC(C = 1)
		lda = LDA()
# 		clf = svm.NuSVC()
		print('訓練LDA')
		lda.fit(問題, 答案)
		print('訓練SVM')
		clf.fit(lda.transform(問題), 答案, sample_weight = sample_weight_constant)
		print('訓練了')
		return lambda 問:clf.predict(lda.transform(問))
	def 試驗(self, 函式, 國語結果 = None, 閩南語結果 = None):
		分類 = {0:[], 1:[], 2:[]}
		段資料 = []
		分數資料 = []
		for 段 in self._解析TGB.提一逝一逝資料出來():
			分數 = 判斷.分數(段)
			段資料.append(段)
			分數資料.append(分數)
			print(len(分數資料))
		for 段, 結果 in zip(段資料, 函式(分數資料)):
			分類[結果].append(段)
		if 國語結果 != None and 閩南語結果 != None:
			self._讀語料.寫語料檔案(國語結果, '\n'.join(分類[0]))
			self._讀語料.寫語料檔案(閩南語結果, '\n'.join(分類[1]))
# 		print(分類[0][:10])
# 		print(分類[1][:10])
# 		print(分類[2][:10])
		return 分類
	def 確定分類(self, 國語檔, 閩南檔):
		分數資料 = []
		答案 = []
		for 國語句 in self._讀語料.讀語料檔案(國語檔):
# 			if 國語句 in 句對應分數:
# 				分數=句對應分數[國語句]
# 			else:
			分數 = 判斷.分數(國語句)
			分數資料.append(分數)
			答案.append(0)
			print(len(答案))
		for 閩南句 in self._讀語料.讀語料檔案(閩南檔):
# 			if 閩南句 in 句對應分數:
# 				分數=句對應分數[閩南句]
# 			else:
			分數 = 判斷.分數(閩南句)
			分數資料.append(分數)
			答案.append(1)
			print(len(答案))
		return self.LDA佮SVM模型(分數資料, 答案)
	def 加校對(self, 國語檔, 閩南檔,
			新國語檔, 新閩南檔, 毋是國語, 毋是閩南):
		編號 = 1
		國 = []
		閩 = []
		for 國語句 in self._讀語料.讀語料檔案(國語檔):
			if 編號 in 毋是國語:
				閩.append(國語句)
			else:
				國.append(國語句)
		for 閩南句 in self._讀語料.讀語料檔案(閩南檔):
			if 編號 not in 毋是閩南:
				閩.append(閩南句)
			else:
				國.append(閩南句)
		self._讀語料.寫語料檔案(新國語檔, '\n'.join(國))
		self._讀語料.寫語料檔案(新閩南檔, '\n'.join(閩))
	def 重產生檔案(self, 國語檔, 閩南檔, 新國語檔, 新閩南檔):
		舊國語句 = set(self._讀語料.讀語料檔案(國語檔))
# 		舊閩南句 = set(self._讀語料.讀語料檔案(閩南檔))
		國 = []
		閩 = []
		for 段 in self._解析TGB.提一逝一逝資料出來():
			if 段 in 舊國語句:
				國.append(段)
			else:
				閩.append(段)
		self._讀語料.寫語料檔案(新國語檔, '\n'.join(國))
		self._讀語料.寫語料檔案(新閩南檔, '\n'.join(閩))
if __name__ == '__main__':
	TGB = 訓練模型()
# 	試驗函式 = TGB.訓練('../語料/TGB/逐句訓練分數.json.gz')
# 	TGB.試驗('../語料/TGB/全部句分數.json.gz', 試驗函式)
# 	TGB.加校對('0.txt', '1.txt', '2.txt', '3.txt',
# 		[27, 35, 48, 51, 68, 228, 239, 258, 317, 595, 663, 717, 804, 807, 989, 1077, 1108, 1150, 1160, 1225, 1228, 1454, 1518, 1575, 1605, 1719, 1724, 1859, 1971, 1975, 2256, 2347, 2594, 2605, 2656, 2689, 2719, 2849, 2867, 2919, 3042, 3160, 3179, 3317, 3339, 3541, 3547, 3559, 3656, 3659, 3699, 3896, 3959, 4028, 4153, 4365, 4366, 4367, 4579, 4835, 5174, 5177, 5212, 5276, 5287, 5604, 5692, 5701, 5721, 5765, 5895, 5971, 6083, 6112, 6137, 6494, 6605, 6704, 6815, 6923, 6992, 7002, 7012, 7026, 7127, 7165, 7188, 7222, 7303, 7434, 7461, 7496, 7613, 7694, 7804, 8073, 8087, 8088, 8186, 8197, 8213, 8324, 8421, 8439],
# 		[590, 636, 655, 810, 4489, 5858])
	TGB.重產生檔案('國2', '閩2', '國3', '閩3')
	試驗函式 = TGB.確定分類('國3', '閩3')
	分類 = TGB.試驗(試驗函式, '國4', '閩4')
