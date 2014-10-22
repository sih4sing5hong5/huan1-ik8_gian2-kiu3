import pickle
import gzip
from 校對.公家辭典連詞 import 公家辭典連詞
from 臺灣言語工具.表單.斯里語句連詞訓練 import 斯里語句連詞訓練

class 閩南語辭典連詞:
	def 產生(self):
		辭典連詞 = 公家辭典連詞()
		辭典, 連詞 = 辭典連詞.產生()
		擺 = 5
		華臺 = '../語料/華臺/{0:02}.華臺一對一斷詞.txt.gz'.format(擺)
		典藏 = '../語料/典藏/{0:02}.臺語文典藏一對一.txt.gz'.format(擺)
		辭典連詞.加一个檔案(辭典, 連詞, 華臺)
		辭典連詞.加一个檔案(辭典, 連詞, 典藏)
		暫存資料夾 = '../語料/校對暫存/算閩南語連詞'
		SRILM安裝路徑 = '/usr/local/srilm/bin/i686-m64/'
		語句連詞訓練 = 斯里語句連詞訓練()
		連詞檔 = 語句連詞訓練.訓練([華臺, 典藏, '../語料/附錄句一對一斷詞.txt.gz',
					'../語料/辭典一對一.txt.gz',
					'../語料/例句一對一.txt.gz',],
				暫存資料夾, 3, SRILM執行檔路徑=SRILM安裝路徑)
		return 辭典, 連詞檔

if __name__ == '__main__':
	辭典, 連詞 = 閩南語辭典連詞().產生()
	print((辭典, 連詞))
	閩南語辭典連詞檔案 = gzip.open('../語料/分言語/閩南語辭典連詞有例句.pickle.gz', 'wb')
	pickle.dump((辭典, 連詞), 閩南語辭典連詞檔案,
			protocol=pickle.HIGHEST_PROTOCOL)
	閩南語辭典連詞檔案.close()
