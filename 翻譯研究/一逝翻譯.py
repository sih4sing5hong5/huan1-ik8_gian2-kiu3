from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
import sys
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.翻譯.斷詞斷字翻譯 import 斷詞斷字翻譯
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器

class 一逝翻譯:
	編碼器 = 語句編碼器()
	_斷詞斷字翻譯 = 斷詞斷字翻譯()
	_譀鏡 = 物件譀鏡()
	_分析器 = 拆文分析器()
	def __init__(self, 斷詞埠, 斷字埠):
		self.斷詞用戶端 = 摩西用戶端('localhost', 斷詞埠, 編碼器=self.編碼器)
		self.斷字用戶端 = 摩西用戶端('localhost', 斷字埠, 編碼器=self.編碼器)
	def 譯(self, 一句):
		原本句物件 = self._分析器.轉做句物件(一句)
		句物件 = self._斷詞斷字翻譯.譯(
			self.斷詞用戶端, self.斷字用戶端, 原本句物件)
		return self._譀鏡.看分詞(句物件)

if __name__ == '__main__':
	翻譯 = 一逝翻譯(sys.argv[1], sys.argv[2])
	try:
		for 一逝 in sys.stdin:
			一逝 = 一逝.strip()
			print(翻譯.譯(一逝))
	except:
		pass

