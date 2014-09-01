from 機器學習.訓練模型 import 訓練模型
import json

if __name__ == '__main__':
	TGB = 訓練模型()
	問題, 答案 = TGB.確定分類('../語料/TGB/分國閩/訓.國語.gz',
		'../語料/TGB/分國閩/訓.閩南.gz')
	with open('訓.問題','w') as 檔案:
		json.dump(問題,檔案)
	with open('訓.答案','w') as 檔案:
		json.dump(答案,檔案)
	問題, 答案 = TGB.確定分類('../語料/TGB/分國閩/試.國語.gz',
		'../語料/TGB/分國閩/試.閩南.gz')
	with open('試.問題','w') as 檔案:
		json.dump(問題,檔案)
	with open('試.答案','w') as 檔案:
		json.dump(答案,檔案)