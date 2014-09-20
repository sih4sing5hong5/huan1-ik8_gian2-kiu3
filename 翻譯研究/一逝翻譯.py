from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
import sys
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 翻譯研究.斷詞斷字翻譯 import 斷詞斷字翻譯
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡

class 一逝翻譯:
	編碼器 = 語句編碼器()
	_斷詞斷字翻譯 = 斷詞斷字翻譯()
	_譀鏡 = 物件譀鏡()
	def __init__(self, 斷詞埠, 斷字埠):
		self.斷詞用戶端 = 摩西用戶端('localhost', 斷詞埠)
		self.斷字用戶端 = 摩西用戶端('localhost', 斷字埠)
	def 譯(self, 一句):
		句物件 = self._斷詞斷字翻譯.譯一句(
			self.斷詞用戶端, self.斷字用戶端, self.編碼器,
				一句)[0]
		return self._譀鏡.看分詞(句物件)

if __name__ == '__main__':
	翻譯 = 一逝翻譯(sys.argv[1], sys.argv[2])
	try:
		for 一逝 in sys.stdin:
			一逝 = 一逝.strip()
			print(翻譯.譯(一逝))
	except:
		pass

