# -*- coding: utf-8 -*-
import json
import urllib.request
from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.標音.語句連詞 import 語句連詞
from 翻譯研究.讀語料 import 讀語料
from 臺灣言語工具.字詞組集句章.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
import pickle
import os
from 臺灣言語工具.標音.動態規劃標音 import 動態規劃標音
from 臺灣言語工具.字詞組集句章.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.字詞組集句章.基本元素.句 import 句
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.斷詞.型音辭典 import 型音辭典
from 臺灣言語工具.斷詞.動態規劃斷詞 import 動態規劃斷詞
from 翻譯研究.對摩西翻譯改 import 對摩西翻譯改
from 翻譯研究.對摩西翻譯改國語斷詞 import 對摩西翻譯改國語斷詞

class 對摩西翻譯改斷詞(對摩西翻譯改國語斷詞):
	埠='8103'
	檔名='試驗結果斷詞.txt'

if __name__ == '__main__':
	翻譯研究 = 對摩西翻譯改斷詞()
	翻譯研究.載入()
	翻譯研究.試驗()
