import re
from 翻譯研究.讀語料 import 讀語料
import os
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.斷詞.中研院工具.斷詞結構化工具 import 斷詞結構化工具
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.表單.斯里語句連詞訓練 import 斯里語句連詞訓練
import shutil

class 中研院千萬句揀出連詞:
	揣標題 = re.compile('<title>(.*?)</title>')
	分句 = re.compile('<sentence>(.*?)</sentence>')
	莫詞性 = re.compile('(\(.*?\))|(\[.*?\])')
	__語料 = 讀語料()
	__分析器 = 拆文分析器()
	__斷詞剖析工具 = 官方斷詞剖析工具()
	__斷詞結構化工具 = 斷詞結構化工具()
	__譀鏡 = 物件譀鏡()
	def 處理全部檔案(self, 目錄, 上尾檔案所在):
		連詞資料 = []
		for (所在, 資料夾, 檔案) in os.walk(目錄):
			for 檔名 in 檔案:
				if 檔名.endswith('.xml'):
					檔案 = open(所在 + '/' + 檔名)
					逐逝 = self.揀(檔案.read())
					檔案.close()
					self.加(連詞資料, 逐逝)
		暫存資料夾 = '../語料/校對暫存/算華語連詞'
		SRILM安裝路徑 = '/usr/local/srilm/bin/i686-m64/'
		os.makedirs(暫存資料夾, exist_ok=True)
		資料檔 = os.path.join(暫存資料夾, '資料.txt')
		self.__語料.寫語料檔案(資料檔, '\n'.join(連詞資料))
		語句連詞訓練 = 斯里語句連詞訓練()
		模型檔 = 語句連詞訓練.訓練([資料檔], 暫存資料夾, 連紲詞長度=3, SRILM執行檔路徑=SRILM安裝路徑)
		shutil.copy(模型檔, 上尾檔案所在)
	def 揀(self, 文章):
		逐逝 = []
# 		for 一逝 in self.揣標題.split(文章)[1::2]:
# 			while True:
# 				try:
# 					斷詞結果 = self.__斷詞剖析工具.揣詞(一逝)
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
	def 加(self, 連詞資料, 逐逝):
		for 一句 in 逐逝:
			連詞資料.append(' '.join(一句.replace('-', ' - ').split('\u3000')))

if __name__ == '__main__':
	連詞 = 中研院千萬句揀出連詞().處理全部檔案(
		'/dev/shm/1000萬(XML)/', '../語料/分言語/中研院連詞.lm')
