import gzip
import pickle
import os

class 語言判斷:
	def 載入(self,國語連詞檔名,閩南語辭典連詞檔名):
		if os.path.isfile(國語連詞檔名):
			辭典連詞檔案 = gzip.open(國語連詞檔名, 'rb')
			self.國語連詞 = pickle.load(辭典連詞檔案)
			辭典連詞檔案.close()
		if os.path.isfile(閩南語辭典連詞檔名):
			閩南語辭典連詞檔案 = gzip.open(閩南語辭典連詞檔名, 'rb')
			self.閩南語辭典, self.閩南語連詞 = pickle.load(閩南語辭典連詞檔案)
			閩南語辭典連詞檔案.close()
if __name__ == '__main__':
	判斷 = 語言判斷()
	判斷.載入('中研院連詞.pickle.gz', '閩南語辭典連詞.pickle.gz')