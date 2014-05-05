from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.字詞組集句章.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.字詞組集句章.解析整理.字物件篩仔 import 字物件篩仔
import sys

class 斷一對一字:
	__分析器 = 拆文分析器()
	__譀鏡 = 物件譀鏡()
	__篩仔 = 字物件篩仔()
	def 斷字(self, 一對一):
		句物件 = self.__分析器.轉做句物件(一對一)
		字陣列 = self.__篩仔.篩出字物件(句物件)
		斷字句 = []
		for 字物件 in 字陣列:
			斷字句.append(self.__譀鏡.看斷詞(字物件, 物件分型音符號='｜'))
		return ' '.join(斷字句)

if __name__ == '__main__':
	斷 = 斷一對一字()
	try:
		for 一逝 in sys.stdin:
			一逝 = 一逝.strip()
			print(斷.斷字(一逝))
	except:
		pass
