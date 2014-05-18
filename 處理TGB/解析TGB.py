import json
from 處理TGB.提掉網頁標仔工具 import 提掉網頁標仔工具
from 處理TGB.提掉文章標仔工具 import 提掉文章標仔工具
import gzip
from 分言語.語言判斷用戶端 import 判斷

class 解析TGB:
	def 讀(self, json檔名, 分數檔名):
		json檔案 = gzip.open(json檔名, 'rt')
		全部 = json.loads(json檔案.read())
		json檔案.close()
		分數狀況 = []
		for 資料 in 全部:
			標題工具 = 提掉網頁標仔工具()
			標題工具.feed(資料['title'][0])
# 			 print(標題工具.結果())
			時間工具 = 提掉網頁標仔工具()
			時間工具.feed(資料['date'][0])
# 			 print(時間工具.結果())
			文章工具 = 提掉文章標仔工具()
			文章工具.feed(資料['context'][0])
			文章 = 文章工具.結果().replace('³', '3').split('<hr>')
			第幾段 = 0
			for 段 in 文章:
				分數 = (判斷.有偌濟漢字(段),) + 判斷.有偌濟音標(段)
				分數狀況.append({
					'網址':資料['url'],
					'標題':標題工具.結果(),
					'發表日':時間工具.結果(),
					'第幾段':第幾段,
					'攏總幾段':len(文章),
					'內容':段.strip(),
					'分數': 分數
					})
				第幾段 += 1
# 			print(分數狀況[-1])
		分數檔案 = gzip.open(分數檔名, 'wt')
		json.dump(分數狀況, 分數檔案)
		分數檔案.close()
		print(len(全部))

if __name__ == '__main__':
	TGB = 解析TGB()
	TGB.讀('../原來TGB.json.gz', '../分數.json.gz')
