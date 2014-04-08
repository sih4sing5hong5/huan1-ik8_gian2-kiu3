import json
import urllib.request
from 臺灣言語工具.字詞組集句章.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.標音.語句連詞 import 語句連詞
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音

class 讀語料:
	__分析器 = 拆文分析器()
	__粗胚 = 文章粗胚()
	def 產生對齊語料對應表(self, 來源詞, 目標詞, 機率表):
		來源詞檔案 = open(來源詞)
		目標詞檔案 = open(目標詞)
		機率表檔案 = open(機率表)
		來源對應表 = {}
		for 一逝 in 來源詞檔案:
			編號, 詞, 出現次數 = 一逝.split()
			來源對應表[編號] = 詞
		來源詞檔案.close()
		目標對應表 = {}
		for 一逝 in 目標詞檔案:
			編號, 詞, 出現次數 = 一逝.split()
			目標對應表[編號] = 詞
		目標詞檔案.close()
		對應表 = {}
		for 一逝 in 機率表檔案:
			來源, 目標, 機率 = 一逝.split()
			if 來源!='0':
				if 來源對應表[來源] not in 對應表:
					對應表[來源對應表[來源]] = []
				對應表[來源對應表[來源]].append((目標對應表[目標], 機率))
# 			print('對應表[來源]',來源,對應表[來源])
		機率表檔案.close()
# 		print(來源對應表)
# 		print(str(對應表)[:1000])
		return 對應表
	def 產生辭典對應表(self, 對應華語):
# 		對應華語檔案=open(對應華語)
# 		資料=('['+對應華語檔案.read().strip()+']').replace('\'','\"')
# 		對應華語檔案.close()
# 		陣列=json.loads(資料)
# 		print(陣列[:10])
		網址 = 'https://raw.github.com/g0v/moedict-data-twblg/master/x-%E8%8F%AF%E8%AA%9E%E5%B0%8D%E7%85%A7%E8%A1%A8.csv'
		資料 = urllib.request.urlopen(網址)
		對應表 = {}
		for 一逝 in 資料.read().decode("utf8").split('\n')[1:]:
			一逝 = 一逝.strip()
			if 一逝 == '':
				continue
			華語, 詞條編號, 詞條名稱 = 一逝.split(',')
			對應表[華語] = 詞條編號 + 詞條名稱
# 			print(對應表[華語],華語)
# 		print(list(對應表)[:10])
		return 對應表
	def 讀語料檔案(self, 檔名):
		檔案 = open(檔名)
		資料 = []
		for 一逝 in 檔案.read().split('\n'):
			資料.append(一逝) 
		檔案.close()
		return 資料
	
	
	def 讀語言模型檔案(self, 檔名):
		連詞 = 語句連詞(3)
		數字 = 0
		for 一逝 in self.讀語料檔案('../語料/訓.閩南語音.txt'):
			組物件 = self.__分析器.建立組物件(
					self.__粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 一逝)
					)
			連詞.看(組物件)
			數字 += 1
			print(數字)
# 			print(組物件)
		return 連詞
		
if __name__ == '__main__':
	語料 = 讀語料()
	語料.產生對齊語料對應表(
		來源詞='../語料/訓.國語字_訓.閩南語音.trn.src.vcb',
		目標詞='../語料/訓.國語字_訓.閩南語音.trn.trg.vcb',
		機率表='../語料/訓.國語字_訓.閩南語音.t3.final')
	語料.產生辭典對應表('result.txt')
	
