import Pyro4

判斷 =  Pyro4.Proxy("PYRO:判斷@localhost:9091")
if __name__ == '__main__':
# 	偌濟漢字 = 判斷.有偌濟漢字('中研院連詞.pickle.gz閩南語辭典連詞.pickle.gz')
# 	print(偌濟漢字)
# 	偌濟音標 = 判斷.有偌濟音標('chhu1 tsha hi5 gha1')
# 	print(偌濟音標)
# 	國語分數 = 判斷.國語分數('中研院連詞.pickle.gz閩南語辭典連詞.pickle.gz')
# 	print(國語分數)
# 	閩南語分數 = 判斷.閩南語分數('中研院連詞.pickle.gz閩南語辭典連詞.pickle.gz')
# 	print(閩南語分數)
	print(判斷.分數('tsiong1-hua3-kuan7 ting2-jim7 gi7-tiunn2 peh8-hong5-sim1 e5 hau7-senn1 peh8-bin2-kiat8 '))
	print(判斷.分數('彰化縣 前任 議長 白鴻森 的 兒子 白閔傑'))
	print(判斷.分數('彰化縣 前任 議長 白鴻森 的 後生 白閔傑'))
	print(判斷.分數('Piān-nā到「決戰ê關鍵」, ta̍k-ê to lóng ē顧慮「事後算siàu」(無論是內場iah外場), m̄-chiah ē jú來jú無人beh開路, 衝頭1 ê. Chit-má內場做頭ê壓力已經大kah接受採訪ê時, 講tio̍h學生安全tō目屎liàn--落-來.'))
	print(判斷.分數('Piān-nā到「決戰ê關鍵」, ta̍k-ê to lóng ē顧慮「事後算siàu」(無論是內場iah外場), m̄-chiah ē jú來jú無人beh開路, 衝頭1 ê. Chit-má內場做頭ê壓力已經大kah接受採訪ê時, 講tio̍h學生安全tō目屎liàn--落-來.'))
	print(判斷.分數('每到「決戰關頭」，大家都會顧慮「秋後算帳」（不管是場內、場外），所以越來越沒有人要當頭開第一槍。現在場內當頭的已經壓力大到受訪時，談到學生安全時都落下眼淚了。 '))
