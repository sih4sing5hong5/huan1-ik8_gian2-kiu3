# -*- coding: utf-8 -*-

from 資料處理.斷字佮斷詞 import 斷字佮斷詞
if __name__ == '__main__':
	斷字詞 = 斷字佮斷詞()
	斷字詞.處理漢字('../語料/例句華語字.txt.gz')
	