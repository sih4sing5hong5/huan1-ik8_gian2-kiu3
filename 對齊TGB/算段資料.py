from 分言語.語言判斷 import 判斷
from 處理TGB.資料檔 import 資料檔
from sklearn.lda import LDA
from 處理TGB.解析TGB import 解析TGB
import numpy as np
from sklearn import svm
from 翻譯研究.讀語料 import 讀語料
from sklearn.decomposition.pca import PCA
import time
from 分言語.語言判斷模型 import 無例句訓練的語料
import os
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔

class 算段資料:
	_讀語料 = 讀語料()
	_分析器 = 拆文分析器()
	_篩仔 = 字物件篩仔()
	_網仔 = 詞物件網仔()
	def 算(self, 資料):
		字數 = 0
		詞數 = 0
		句數 = 0
		for 分詞 in 資料:
			句物件 = self._分析器.轉做句物件(分詞)
			字數 += len(self._篩仔.篩出字物件(句物件))
			詞數 += len(self._網仔.網出詞物件(句物件))
			句數 += 1
		print('句數', 句數)
		print('平均字數', 字數 / 句數)
		print('平均詞數', 詞數 / 句數)
if __name__ == '__main__':
	
	華語檔名 = '../語料/TGB/分開對齊/{0:04}.華'
	閩南語檔名 = '../語料/TGB/分開對齊/{0:04}.閩'
	_讀語料 = 讀語料()
	華 = []
	閩 = []
	for 編 in range(1179):
		print(編)
		if os.path.isfile(華語檔名.format(編)):
			華.extend(_讀語料.讀語料檔案(華語檔名.format(編)))
		if os.path.isfile(閩南語檔名.format(編)):
			閩.extend(_讀語料.讀語料檔案(閩南語檔名.format(編)))
	_算段資料 = 算段資料()
	_算段資料.算(華)
	_算段資料.算(閩)
