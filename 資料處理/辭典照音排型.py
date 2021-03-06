from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.基本元素.公用變數 import 標點符號

'''
試驗：	
一般
	稽 考 在 早 tsiah4 e5 博 學 e5 人 ，
	khe1-kho2 tsai7-tsa2 tsiah4-e5 phok4-hak8 e5 lang5 ,
	khe1-考｜kho2 在-早｜tsai7-tsa2 tsiah4-e5｜tsiah4-e5 博-學｜phok4-hak8 e5｜e5 人｜lang5 ，｜,
漢羅詞
	攏 總 會 曉 tit4 寫 批 ，
	long2-tsong2 ue7-hiau2-tit4 sia2 phue1 ,
	攏-總｜long2-tsong2 會-曉-tit4｜ue7-hiau2-tit4 寫｜sia2 批｜phue1 ，｜,
毋著字
	看 見 園 丁 企 hi2 路 邊 ，
	khuann3-kinn3 hng5-ting1 khia7 hi2 loo7-pinn1 ,
	看-見｜khuann3-kinn3 園-丁｜hng5-ting1 khia7｜khia7 hi2｜hi2 路-邊｜loo7-pinn1 ，｜,
頭前毋著字
	廈 門 e5 牧 師 ，
	e7-mng5 e5 bok8-su1 , 
	e7-門｜e7-mng5 e5｜e5 牧-師｜bok8-su1 ，｜,  
型音數量無對齊
數字 
'''
class 辭典照音排型:
	_分析器 = 拆文分析器()
	_篩仔 = 字物件篩仔()
	def 對齊(self, 辭典, 型, 音):
		型物件 = self._分析器.建立章物件(型)
		型字陣列 = self._篩仔.篩出字物件(型物件)
		音物件 = self._分析器.建立章物件(音)
		音字陣列 = self._篩仔.篩出字物件(音物件)
		表 = []
		表.append([(0, 0)] * (1 + len(音字陣列)))
		for 型字 in 型字陣列:
			表.append([(0, 0)])
			for 音字 in 音字陣列:
# 				print(self.佇辭典內底(辭典, 型字.型, 音字.型), 型字.型, 音字.型)
				if self.佇辭典內底(辭典, 型字.型, 音字.型):
					倒爿面頂 = 表[-2][len(表[-1]) - 1]
					表[-1].append((倒爿面頂[0] + 1, 1))
				else:
					面頂 = 表[-2][len(表[-1])]
					倒爿 = 表[-1][-1]
					if 面頂[0] >= 倒爿[0]:
						表[-1].append((面頂[0], 2))
					else:
						表[-1].append((倒爿[0], 3))
		型所在 = len(表) - 1
		音所在 = len(表[-1]) - 1
		while 型所在 > 0 and 音所在 > 0:
			方向 = 表[型所在][音所在][1]
			if 方向 == 1:
				音字陣列[音所在 - 1].音 = 音字陣列[音所在 - 1].型
				音字陣列[音所在 - 1].型 = 型字陣列[型所在 - 1].型
				型所在 -= 1
				音所在 -= 1
			elif 方向 == 2:
				型所在 -= 1
			elif 方向 == 3:
# 				音字陣列[音所在 - 1].音 = 無音
				音所在 -= 1
			else:
				raise RuntimeError('程式有問題')
		while 音所在 > 0:
			音字陣列[音所在 - 1].音 = 音字陣列[音所在 - 1].型
			音所在 -= 1
			
# 		from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
# 		_譀鏡 = 物件譀鏡()
# 		print(型, 音)
# 		print(_譀鏡.看分詞(音物件))
		
		return 音物件
	def 佇辭典內底(self, 辭典, 型, 音):
		if 型 == 音:
			return True
		if 型 in 標點符號 and 音 in 標點符號:
			return True
		try:
			字物件 = self._分析器.產生對齊字(型, 音)
			詞物件 = self._分析器.建立詞物件('')
			詞物件.內底字 = [字物件]
			結果 = 辭典.查詞(詞物件)
			if len(結果[0]) > 0:
				return True
			else:
				return False
		except:
			return False
