# -*- coding: utf-8 -*-
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.斷詞.中研院工具.斷詞結構化工具 import 斷詞結構化工具
from 臺灣言語工具.字詞組集句章.解析整理.物件譀鏡 import 物件譀鏡
class 斷字佮斷詞:
	def 處理漢字(self,檔案名):
		原本檔案=open(檔案名)
		斷字檔案=open(檔案名.replace('.txt','斷字.txt'),'w')
		斷詞檔案=open(檔案名.replace('.txt','斷詞.txt'),'w')
		斷詞剖析工具=官方斷詞剖析工具()
		結構化工具=斷詞結構化工具()
		譀鏡=物件譀鏡()
		for 一逝 in 原本檔案:
			詞組=一逝.split()
			無斷=''.join(詞組)
			斷詞結果=斷詞剖析工具.斷詞(無斷,等待=10)
			斷詞章物件=結構化工具.斷詞轉章物件(斷詞結果)
			print(譀鏡.看型(斷詞章物件,物件分字符號=' ',物件分詞符號=' '),file=斷字檔案)
			print(譀鏡.看型(斷詞章物件,物件分詞符號=' '),file=斷詞檔案)
		原本檔案.close()
		斷字檔案.close()
		斷詞檔案.close()
	def 處理漢字斷詞就好(self,檔案名):
		原本檔案=open(檔案名)
		斷字檔案=open(檔案名.replace('.txt','斷字.txt'),'w')
		for 一逝 in 原本檔案:
			詞組=一逝.split()
			無斷=''.join(詞組)
			斷字=' '.join(無斷)
			print(斷字,file=斷字檔案)
		原本檔案.close()
		斷字檔案.close()
	def 處理音標(self,檔案名):
		原本檔案=open(檔案名)
		斷字檔案=open(檔案名.replace('.txt','斷字.txt'),'w')
# 		斷詞檔案=open(檔案名.replace('.txt','斷詞.txt'),'w')
# 		斷詞剖析工具=官方斷詞剖析工具()
# 		結構化工具=斷詞結構化工具()
# 		譀鏡=物件譀鏡()
		for 一逝 in 原本檔案:
			詞組=一逝.replace('-',' ').split()
			斷字=' '.join(詞組)
			print(斷字,file=斷字檔案)
# 			print(斷字)
		原本檔案.close()
		斷字檔案.close()

if __name__=='__main__':
	斷字詞=斷字佮斷詞()
# 	斷字詞.處理漢字('../語料/訓.國語字.txt')
# 	斷字詞.處理漢字('../語料/試.國語字.txt')
	斷字詞.處理漢字斷詞就好('../語料/訓.國語字.txt')
	斷字詞.處理漢字斷詞就好('../語料/試.國語字.txt')
	斷字詞.處理音標('../語料/訓.閩南語音.txt')
	斷字詞.處理音標('../語料/試.閩南語音.txt')
# 	閩南語字檔案 = open('閩南語字.txt','w')
# 	閩南語音檔案 = open('閩南語音.txt','w')
	