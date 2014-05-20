import json
import gzip

class 資料檔:
	def 讀(self,檔名):
		檔案 = gzip.open(檔名, 'rt')
		全部 = json.load(檔案,)
		檔案.close()
		return 全部
	def 寫(self,檔名,資料):
		檔案 = gzip.open(檔名, 'wt')
		json.dump(資料, 檔案)
		檔案.close()