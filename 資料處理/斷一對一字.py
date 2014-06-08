from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
import sys
from 臺灣言語工具.基本元素.公用變數 import 分詞符號

class 斷一對一字:
	__分析器 = 拆文分析器()
	__譀鏡 = 物件譀鏡()
	__篩仔 = 字物件篩仔()
	def 斷字(self, 一對一):
		組物件 = self.__分析器.建立組物件('')
		for 詞 in 一對一.split(分詞符號):
			try:
				組物件.內底詞.append(self.__分析器.轉做詞物件(詞))
			except:
				詞='-'.join(詞)
				組物件.內底詞.append(self.__分析器.產生對齊詞(詞, 詞))
		字陣列 = self.__篩仔.篩出字物件(組物件)
		斷字句 = []
		for 字物件 in 字陣列:
			斷字句.append(self.__譀鏡.看斷詞(字物件, 物件分型音符號 = '｜'))
		return ' '.join(斷字句)

if __name__ == '__main__':
	斷 = 斷一對一字()
	try:
		for 一逝 in sys.stdin:
			一逝 = 一逝.strip()
			print(斷.斷字(一逝))
	except:
		pass
