import gzip
import pickle
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
import itertools
from 翻譯研究.讀語料 import 讀語料
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器

class 語言判斷詞表:
	__物件譀鏡 = 物件譀鏡()
	定用詞數量 = 7000
	特徵詞數量 = 3000
	def 產生(self):
		華語孤詞, 閩南語孤詞 = '../語料/分言語/中研院連詞.lm', '../語料/校對暫存/算閩南語連詞/語言模型.lm'
		華語孤詞 = self.揣頭前一萬筆(華語孤詞)
		閩南語孤詞 = self.揣頭前一萬筆(閩南語孤詞)
		print(華語孤詞[:100])
		print(閩南語孤詞[:100])
		華字串種類 = set()
		閩字串種類 = set()
		for 編鄙, 資料 in enumerate(華語孤詞):
			詞物件 = 資料[0]
			型 = self.__物件譀鏡.看型(詞物件)
			華字串種類.add(型)
		for 編鄙, 資料 in enumerate(閩南語孤詞):
			詞物件 = 資料[0]
			型 = self.__物件譀鏡.看型(詞物件)
			閩字串種類.add(型)
# 			if 型 .startswith('伊') or  型 .startswith('佇'):
# 				print(編鄙, 資料)

		華語選著詞 = []
		for 資料 in 華語孤詞:
			詞物件 = 資料[0]
			型 = self.__物件譀鏡.看型(詞物件)
			if len(華語選著詞) < self.特徵詞數量 and 型 not in 閩字串種類:
				華語選著詞.append(資料)
# 				print(型)
		閩南語選著詞 = []
		for 資料 in 閩南語孤詞:
			詞物件 = 資料[0]
			型 = self.__物件譀鏡.看型(詞物件)
			if len(閩南語選著詞) < self.特徵詞數量 and 型 not in 華字串種類:
				閩南語選著詞.append(資料)
# 				print(型)
			
# 		print(華語孤詞[:10])
# 		print(閩南語孤詞[:10])
# 		print(華語孤詞[5000:5000+10])
# 		print(閩南語孤詞[5000:5000+10])
# 		print(華語孤詞[10000:10000+10])
# 		print(閩南語孤詞[10000:10000+10])
		print((華語選著詞)[:100])
		print((閩南語選著詞)[:100])
		print(len(華語選著詞))
		print(len(閩南語選著詞))
		對應編號 = {}
		編號 = 0
		for 資料 in itertools.chain(華語選著詞, 閩南語選著詞):
			詞物件 = 資料[0]
			對應編號[詞物件] = 編號
			編號 += 1
		return 對應編號
	def 揣頭前一萬筆(self, 孤詞表):
		_語料 = 讀語料()
		_分析器 = 拆文分析器()
		開始 = False
		孤詞資料 = []
		for 一逝 in _語料.讀語料檔案(孤詞表):
# 			print('一逝',一逝)
			if 開始:
				if 一逝 == '':
					continue
				if 一逝 == '\\2-grams:':
					break
				機率, 分詞, *退回 = 一逝.split('\t')
# 				print((機率),float(機率),孤詞表)
				孤詞資料.append(['詞物件', float(機率), 分詞])
			if 一逝 == '\\1-grams:':
				開始 = True
		排法 = lambda x:(-x[1], x[2])
		孤詞資料.sort(key=排法)
		for 資料 in 孤詞資料[:self.定用詞數量]:
# 			print(資料[1], 資料[2])
			詞物件 = _分析器.轉做詞物件(資料[2])
			資料[0]=詞物件
		return 孤詞資料[:self.定用詞數量]

if __name__ == '__main__':
	對應編號 = 語言判斷詞表().產生()
	語言判斷詞表檔案 = gzip.open('../語料/分言語/語言判斷詞表.pickle.gz', 'wb')
	pickle.dump(對應編號, 語言判斷詞表檔案,
			protocol=pickle.HIGHEST_PROTOCOL)
	語言判斷詞表檔案.close()
