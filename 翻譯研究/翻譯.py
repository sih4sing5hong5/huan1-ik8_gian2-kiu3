import json
import urllib.request
from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.標音.語句連詞 import 語句連詞
from 翻譯研究.讀語料 import 讀語料
from 臺灣言語工具.字詞組集句章.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
import pickle
import os

class 翻譯:
	pass
		
if __name__ == '__main__':
	語料 = 讀語料()
	對齊語料對應表=語料.產生對齊語料對應表(
		來源詞='../語料/訓.國語字_訓.閩南語音.trn.src.vcb',
		目標詞='../語料/訓.國語字_訓.閩南語音.trn.trg.vcb',
		機率表='../語料/訓.國語字_訓.閩南語音.t3.final')
	辭典對應表=語料.產生辭典對應表('result.txt')
	分析器=拆文分析器()
	粗胚=文章粗胚()
	語言模型檔名='語言模型檔名.pickle'
	if os.path.isfile(語言模型檔名):
		語言模型檔案=open(語言模型檔名,'rb')
		連詞 = pickle.load(語言模型檔案)
		語言模型檔案.close()
	else:
		連詞=語料.讀語言模型檔案('../語料/訓.閩南語音.txt')
		語言模型檔案=open(語言模型檔名,'wb')
		pickle.dump(連詞, 語言模型檔案, protocol=pickle.HIGHEST_PROTOCOL)
		語言模型檔案.close()
	for 一逝 in 語料.讀語料檔案('../語料/試.國語字.txt'):
		句物件=分析器.建立句物件('')
		for 國語詞 in 一逝.split():
			集物件=分析器.建立集物件('')
			if 國語詞 in 對齊語料對應表:
				print('對齊語料對應表',國語詞,對齊語料對應表[國語詞])
			elif 國語詞 in 辭典對應表:
				print('辭典對應表',國語詞,辭典對應表[國語詞])
