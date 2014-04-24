from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
import sys

if __name__ == '__main__':
	編碼器 = 語句編碼器()
	for 一逝 in sys.stdin:
		一逝 = 一逝.strip()
		print(編碼器.編碼(一逝))

