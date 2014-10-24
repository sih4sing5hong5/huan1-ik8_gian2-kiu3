from 翻譯研究.讀語料 import 讀語料
import os

if __name__ == '__main__':
	目錄 = '../語料/TGB/分開對齊/'
	華語檔名 = []
	閩南語檔名 = []
	for 檔名 in os.listdir(目錄):
		if 檔名.endswith('對齊句華語'):
			華語檔名.append(檔名)
		elif 檔名.endswith('對齊句閩南'):
			閩南語檔名.append(檔名)
	華語檔名.sort()
	閩南語檔名.sort()
	if len(華語檔名) != len(閩南語檔名):
		raise RuntimeError('檔案數量無仝')
	華平行資料 = []
	閩平行資料 = []
	_語料 = 讀語料()
	for 華, 閩 in zip(華語檔名, 閩南語檔名):
		華資料 = _語料.讀語料檔案(os.path.join(目錄, 華))
		閩資料 = _語料.讀語料檔案(os.path.join(目錄, 閩))
		if len(華資料) != len(閩資料):
			raise RuntimeError('檔案{}、{}數量無仝'.format(華, 閩))
		華平行資料.extend(華資料)
		閩平行資料.extend(閩資料)
	_語料.寫語料檔案(os.path.join(目錄, '..', '對齊平行華語資料'), 華平行資料)
	_語料.寫語料檔案(os.path.join(目錄, '..', '對齊平行閩南語資料'), 閩平行資料)
	print(len(華平行資料))
