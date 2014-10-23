
from bleualign.align import Aligner

class 翻譯評分對齊介面:
	公家參數 = {}
	def __init__(self):
		self.公家參數 = {}
		self.公家參數['factored'] = False
		self.公家參數['filter'] = None
		self.公家參數['filterthreshold'] = 90
		self.公家參數['filterlang'] = None
		self.公家參數['eval'] = None
		self.公家參數['galechurch'] = None
		self.公家參數['verbosity'] = 1
		self.公家參數['printempty'] = False
		self.公家參數['output'] = None
	def 對齊(self, 原來, 目標, 原來翻目標, 目標翻原來, 原來對齊=None, 目標對齊=None):
		參數 = self.公家參數.copy()
		參數['srcfile'] = 原來
		參數['targetfile'] = 目標
		參數['srctotarget'] = 原來翻目標
		參數['targettosrc'] = 目標翻原來
		參數['output-src'] = 原來對齊
		參數['output-target'] = 目標對齊

		a = Aligner(參數)
		a.mainloop()
		return a.results()