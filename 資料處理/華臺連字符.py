from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 翻譯研究.讀語料 import 讀語料

class 華臺連字符:
	__分析器=拆文分析器()
	__譀鏡=物件譀鏡()
	def 轉連字符(self,本源,目的):
		語料=讀語料()
		閩南語=語料.讀語料檔案(本源)
		結果=[]
		for 一逝 in 閩南語:
			一逝=一逝.replace(' - ','-')
			if 一逝.endswith(' -'):
				一逝=一逝[:-2]
			if 一逝=='不但 國 美館 無視 看無 臺中市政府 的 公文 ，':
				一逝='不但 國 美館 看無 臺中市政府 的 公文 ，'
			elif 一逝 == '佇 遙遠 Solomon 群島 群島 的 一位 當地 頭目 ，':
				一逝 = '佇 遙遠 Solomon 群島 的 一位 當地 頭目 ，'
			結果.append(一逝)
		語料.寫語料檔案(目的, '\n'.join(結果))
		return

if __name__=='__main__':
	華臺=華臺連字符()
	華臺.轉連字符("../語料/華臺原本閩南語字.txt.gz", "../語料/華臺閩南語字.txt.gz")
	華臺.轉連字符("../語料/華臺原本閩南語音.txt.gz", "../語料/華臺閩南語音.txt.gz")
