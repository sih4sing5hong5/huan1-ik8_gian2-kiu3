import re
from 翻譯研究.讀語料 import 讀語料
import os
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.標音.語句連詞 import 語句連詞
import pickle
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.斷詞.中研院工具.斷詞結構化工具 import 斷詞結構化工具
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
import gzip

class 中研院千萬句揀出連詞:
	揣標題 = re.compile('<title>(.*?)</title>')
	分句 = re.compile('<sentence>(.*?)</sentence>')
	莫詞性 = re.compile('(\(.*?\))|(\[.*?\])')
	__語料 = 讀語料()
	__分析器 = 拆文分析器()
	__斷詞剖析工具 = 官方斷詞剖析工具()
	__斷詞結構化工具 = 斷詞結構化工具()
	__譀鏡 = 物件譀鏡()
	def 處理全部檔案(self, 連詞, 目錄):
		for (所在, 資料夾, 檔案) in os.walk(目錄):
			for 檔名 in 檔案:
				if 檔名.endswith('.xml'):
					檔案 = open(所在 + '/' + 檔名)
					逐逝 = self.揀(檔案.read())
					檔案.close()
					self.加(連詞, 逐逝)
	def 揀(self, 文章):
		逐逝 = []
# 		for 一逝 in self.揣標題.split(文章)[1::2]:
# 			while True:
# 				try:
# 					斷詞結果 = self.__斷詞剖析工具.斷詞(一逝)
# 				except:
# 					pass
# 				else:
# 					break
# 			組物件 = self.__斷詞結構化工具.斷詞轉組物件(斷詞結果)
# 			一逝型 = self.__譀鏡.看型(組物件, 物件分詞符號 = '\u3000')
# 			print(一逝型)
# 			逐逝.append(self.莫詞性.sub('', 一逝型))
		for 一逝 in self.分句.split(文章)[1::2]:
			逐逝.append(self.莫詞性.sub('', 一逝))
		return 逐逝
	def 加(self, 連詞, 逐逝):
		for 一句 in 逐逝:
			組物件 = self.__分析器.建立組物件('')
			for 詞 in 一句.replace('-',' - ').split('\u3000'):
				詞物件 = self.__分析器.建立詞物件(詞)
				組物件.內底詞.append(詞物件)
# 			print(組物件)
			連詞.看(組物件)

if __name__ == '__main__':
	連詞 = 語句連詞(3)
	中研院千萬句揀出連詞().處理全部檔案(連詞, '/dev/shm/1000萬(XML)/')
	中研院連詞檔案 = gzip.open('../語料/分言語/中研院連詞.pickle.gz', 'wb')
	pickle.dump(連詞, 中研院連詞檔案,
			protocol = pickle.HIGHEST_PROTOCOL)
	中研院連詞檔案.close()
