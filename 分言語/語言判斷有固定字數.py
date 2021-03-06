import gzip
import pickle
import os
import unicodedata
from 臺灣言語工具.基本元素.公用變數 import 統一碼漢字佮組字式類
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音音標
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.斷詞.中研院工具.斷詞結構化工具 import 斷詞結構化工具
from 臺灣言語工具.斷詞.連詞揀集內組 import 連詞揀集內組
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
import Pyro4
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 分言語.語言判斷模型 import 語言判斷模型
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔
import itertools
from 處理TGB.資料檔 import 資料檔
from 分言語.語言判斷模型 import 遠端連接埠
import random
from 臺灣言語工具.基本元素.公用變數 import 分字符號
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡

句對應分數檔名 = '../語料/TGB/全部句分數.json.gz'

class 語言判斷有固定字數:
	國語連詞 = None
	閩南語辭典 = None
	閩南語連詞 = None
	__粗胚 = 文章粗胚()
	__分析器 = 拆文分析器()
	__篩仔 = 字物件篩仔()
	_篩仔 = 字物件篩仔()
	_譀鏡 = 物件譀鏡()
	__家私 = 轉物件音家私()
	__斷詞剖析工具 = 官方斷詞剖析工具()
	__斷詞結構化工具 = 斷詞結構化工具()
	__標音 = 連詞揀集內組()
	__斷詞 = 拄好長度辭典揣詞()
	__網仔 = 詞物件網仔()
	__資料檔 = 資料檔()
	判斷模型 = 語言判斷模型()
	詞表 = {}
	斷詞 = {}
	句對應分數 = {}
	def 分數(self, 語句, 字數):
		處理減號 = self.__粗胚.建立物件語句前處理減號(教會羅馬字音標, 語句)
		print('算閩南')
		標好閩南語, 閩南語分數, 閩南語詞數, 教羅, 通用, 句所在 = self.閩南語分數(處理減號, 字數)
		print('算國語')
		標好國語, 國語分數, 國語詞數 = self.國語分數(處理減號, 句所在)
		print('算定用詞')
		定用詞 = self.看國閩定用詞(標好國語, 標好閩南語)
		結果 = [國語分數, 國語詞數, \
				閩南語分數, 閩南語詞數, 教羅, 通用]
# 		print(結果,標好閩南語,標好國語)
		結果.extend(定用詞)
		print('好矣')
		return 結果
	def 標好國語(self, 語句):
		處理減號 = self.__粗胚.建立物件語句前處理減號(教會羅馬字音標, 語句)
		標好國語, 國語分數, 國語詞數 = self.國語分數(處理減號)
		return 標好國語
	def 有偌濟漢字(self, 語句):
		漢字 = 0
		for 字 in 語句:
			if unicodedata.category(字) in 統一碼漢字佮組字式類:
				漢字 += 1
		return 漢字 / len(語句)
	def 有偌濟音標(self, 處理減號):
		教羅 = 0
		通用 = 0
		組物件 = self.__分析器.建立組物件(處理減號)
		字陣列 = self.__篩仔.篩出字物件(組物件)
		for 字物件 in 字陣列:
			if 教會羅馬字音標(字物件.型).音標 != None:
				教羅 += 1
			if 通用拼音音標(字物件.型).音標 != None:
				通用 += 1
		return 教羅 / len(字陣列), 通用 / len(字陣列),
	def 國語分數(self, 處理減號, 句所在):
		無空白 = ''.join(處理減號.split())
		if 處理減號 in self.斷詞:
			章物件 = self.斷詞[處理減號]
# 		elif 無空白 in  self.舊斷詞 :
# 			print(處理減號,self.舊斷詞[無空白])
		else:
			斷詞結果 = self.__斷詞剖析工具.斷詞(處理減號, 等待=60, 一定愛成功=True)
			章物件 = self.__斷詞結構化工具.斷詞轉章物件(斷詞結果)
			self.斷詞[處理減號] = 章物件
			print('斷詞這馬', len(self.斷詞), '句')
		鉸過章物件 = self.提一段出來(章物件, 句所在)
		標好, 分數, 詞數 = self.判斷模型.國語分數(鉸過章物件)
		return 標好, 分數, 詞數
	def 閩南語分數(self, 處理減號, 字數):
		教羅, 通用 = self.有偌濟音標(處理減號)
		章物件 = self.__分析器.建立章物件(處理減號)
		if 教羅 >= 通用:
			標準章物件 = self.__家私.轉音(教會羅馬字音標, 章物件)
		else:
			標準章物件 = self.__家私.轉音(通用拼音音標, 章物件)
		句所在 = self.提佗位出來(標準章物件, 字數)
		鉸過 = self.提一段出來(標準章物件, 句所在)
# 		print(標準章物件,句所在,鉸過)
		標好, 分數, 詞數 = self.判斷模型.閩南語分數(鉸過)
		return 標好, 分數, 詞數, 教羅, 通用, 句所在
	def 看國閩定用詞(self, 國語物件, 閩南語物件):
		國語長度統計 = [0] * 4
		閩南語長度統計 = [0] * 4
		目前幾擺 = [0] * len(self.詞表)
		self.看定用詞(國語物件, 國語長度統計, 目前幾擺)
		self.看定用詞(閩南語物件, 閩南語長度統計, 目前幾擺)
		return itertools.chain(國語長度統計, 閩南語長度統計, 目前幾擺)
	def 看定用詞(self, 物件, 長度統計, 目前幾擺):
		for 詞物件 in self.__網仔.網出詞物件(物件):
			if len(詞物件.內底字) <= 4:
				長度統計[len(詞物件.內底字) - 1] += 1
			else:
				長度統計[4 - 1] += 1
			if 詞物件 in self.詞表:
				目前幾擺[self.詞表[詞物件]] += 1
	def 提佗位出來(self, 章物件, 字數):
		所在 = random.randrange(len(章物件.內底句))
		這馬字數 = 0
		句所在 = []
		while 這馬字數 < 字數:
			這馬字數 += len(self._篩仔.篩出字物件(章物件.內底句[所在]))
			句所在.append(所在)
			所在 = (所在 + 1) % len(章物件.內底句)
# 		print(語句)
# 		print(' '.join(句陣列))
		return 句所在
	def 提一段出來(self, 章物件, 句所在):
		鉸過章物件 = self.__分析器.建立章物件('')
		句陣列 = 鉸過章物件.內底句
		for 所在 in 句所在:
			if 所在 < len(章物件.內底句):
				句陣列.append(章物件.內底句[所在])
		return 鉸過章物件

判斷 = 語言判斷有固定字數()
Pyro4.config.SERIALIZER = 'pickle'
判斷.判斷模型 = Pyro4.Proxy("PYRO:判斷模型@localhost:" + str(遠端連接埠))

if os.path.isfile('../語料/分言語/語言判斷詞表.pickle.gz'):
	語言判斷詞表檔案 = gzip.open('../語料/分言語/語言判斷詞表.pickle.gz', 'rb')
	判斷.詞表 = pickle.load(語言判斷詞表檔案)
	語言判斷詞表檔案.close()
# else:
# 	判斷.詞表 = 語言判斷詞表().產生()
if os.path.isfile('../語料/TGB/斷詞物件.pickle.gz'):
	斷詞物件檔案 = gzip.open('../語料/TGB/斷詞物件.pickle.gz', 'rb')
	判斷.斷詞 = pickle.load(斷詞物件檔案)
	斷詞物件檔案.close()

def __試驗():
	print(判斷.分數('tsiong1-hua3-kuan7 ting2-jim7 gi7-tiunn2 peh8-hong5-sim1 e5 hau7-senn1 peh8-bin2-kiat8 '))
	print(判斷.分數('彰化縣 前任 議長 白鴻森 的 兒子 白閔傑'))
	print(判斷.分數('彰化縣 前任 議長 白鴻森 的 後生 白閔傑'))
	print(判斷.分數('Piān-nā到「決戰ê關鍵」, ta̍k-ê to lóng ē顧慮「事後算siàu」(無論是內場iah外場), m̄-chiah ē jú來jú無人beh開路, 衝頭1 ê. Chit-má內場做頭ê壓力已經大kah接受採訪ê時, 講tio̍h學生安全tō目屎liàn--落-來.'))
	print(判斷.分數('每到「決戰關頭」，大家都會顧慮「秋後算帳」（不管是場內、場外），所以越來越沒有人要當頭開第一槍。現在場內當頭的已經壓力大到受訪時，談到學生安全時都落下眼淚了。 '))

if __name__ == '__main__':
	import cProfile
	cProfile.run('__試驗()')

