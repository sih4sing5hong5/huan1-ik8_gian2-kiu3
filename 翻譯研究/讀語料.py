# -*- coding: utf-8 -*-
import gzip
import json
import urllib.request
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.表單.實際語句連詞 import 實際語句連詞
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.表單.型音辭典 import 型音辭典

class 讀語料:
	__分析器 = 拆文分析器()
	__粗胚 = 文章粗胚()
	__家私 = 轉物件音家私()
	__譀鏡 = 物件譀鏡()
	def 產生對齊語料對應表(self, 來源詞, 目標詞, 機率表):
		來源詞檔案 = open(來源詞, encoding='utf-8')
		目標詞檔案 = open(目標詞, encoding='utf-8')
		機率表檔案 = open(機率表, encoding='utf-8')
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
			if 來源 != '0':
				if 來源對應表[來源] not in 對應表:
					對應表[來源對應表[來源]] = []
				對應表[來源對應表[來源]].append((目標對應表[目標], 機率))
# 			print('對應表[來源]',來源,對應表[來源])
		機率表檔案.close()
# 		print(來源對應表)
# 		print(str(對應表)[:1000])
		return 對應表
	def 產生對齊語料片語表(self, 對齊片語檔名):
		對齊片語檔案 = gzip.open(對齊片語檔名, mode='rt', encoding='utf-8')
		對應表 = {}
		for 一逝 in 對齊片語檔案:
			資料 = 一逝.strip().split('|||')
			國語 = tuple(資料[0].split())
# 			標準音 = self.__粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 資料[1].strip())
# 			閩南語 = self.__分析器.建立組物件(標準音)
# 			if 國語 not in 對應表:
# 				對應表[國語] = self.__分析器.建立集物件('')
# 			對應表[國語].內底組.append(閩南語)
			閩南語 = 資料[1].strip()
			機率 = float(資料[2].split()[2])
			if 國語 not in 對應表:
				對應表[國語] = []
			對應表[國語].append((閩南語, 機率))
			print('產生對齊語料片語表', len(對應表))
		對齊片語檔案.close()
# 		print(str(對應表)[:100])
		return 對應表
	def 產生辭典對應表(self, 對應華語):
		對應華語檔案 = open(對應華語, encoding='utf-8')
		陣列 = json.loads(對應華語檔案.read())
		對應華語檔案.close()
		辭典對應表 = {}
		字典對應表 = {}
		for 國語, 流水號, 閩南語字, 閩南語音 in 陣列:
			音 = self.__粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 閩南語音.split('/')[0])
			try:
				組物件 = self.__分析器.產生對齊組(閩南語字, 音)
				標準組 = self.__家私.轉音(臺灣閩南語羅馬字拼音, 組物件)
			except:
				pass
			else:
				if 國語 not in 辭典對應表:
					辭典對應表[國語] = []
				辭典對應表[國語].append(self.__譀鏡.看音(標準組))
				型 = self.__譀鏡.看型(標準組)
				if 型 not in 字典對應表:
					字典對應表[型] = []
				字典對應表[型].append(self.__譀鏡.看音(標準組))
				print('產生辭典對應表', len(辭典對應表))
		return (辭典對應表, 字典對應表)
	def 產生萌典辭典對應表(self):
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
		if 檔名.endswith('gz'):
			檔案 = gzip.open(檔名, 'rt', encoding='utf-8')
		else:
			檔案 = open(檔名, encoding='utf-8')
		資料 = []
		for 一逝 in 檔案.read().split('\n'):
			if 一逝.strip() == '':
				continue
			資料.append(一逝.strip())
		檔案.close()
		return 資料
	def 寫語料檔案(self, 檔名, 資料):
		if 檔名.endswith('gz'):
			檔案 = gzip.open(檔名, 'wt', encoding='utf-8')
		else:
			檔案 = open(檔名, 'w', encoding='utf-8')
		print(資料, file=檔案)
		檔案.close()
		return
	
	def 產生辭典(self,辭典, 一對一檔名):
		for 閩南語一對一 in self.讀語料檔案(一對一檔名):
			try:
				組物件 = self.__分析器.轉做組物件(閩南語一對一)
# 				標準組 = self.__家私.轉音(臺灣閩南語羅馬字拼音, 組物件)
				標準組 = 組物件
			except Exception as 問題:
				print(閩南語一對一,問題)
				pass
			else:
				for 詞物件 in 標準組.內底詞:
					辭典.加詞(詞物件)
		return
	
	def 產生連詞(self,連詞, 一對一檔名):
		for 閩南語一對一 in self.讀語料檔案(一對一檔名):
			try:
				組物件 = self.__分析器.轉做組物件(閩南語一對一)
				標準組 = self.__家私.轉音(臺灣閩南語羅馬字拼音, 組物件)
			except:
				pass
			else:
				連詞.看(組物件)
		return

if __name__ == '__main__':
	語料 = 讀語料()
	語料.產生對齊語料對應表(
		來源詞='../語料/訓.國語字_訓.閩南語音.trn.src.vcb',
		目標詞='../語料/訓.國語字_訓.閩南語音.trn.trg.vcb',
		機率表='../語料/訓.國語字_訓.閩南語音.t3.final')
# 	語料.產生辭典對應表('result.txt')
	語料.產生對齊語料片語表('../語料/phrase-table.gz')


