###翻譯研究
作者：薛丞宏

###系統需求
請安裝，愈新愈好。括號內是我實驗用的版本
giza++（1.0.7）
srilm（1.7.0）
moses（commit 40c819d285cdeb40c0b8cc428bfde2fcb531b655）
設定好path，而且確定有mosesserver有裝起來
${HOME}/mt內底愛有giza++、mkcls、snt2cooc.out

請安裝Python 3佮臺灣言語工具
裝了後，全部的設定應該是
```bash
PATH=$PATH:/usr/local/giza-pp-v1.0.7/GIZA++-v2/
PATH=$PATH:/usr/local/giza-pp-v1.0.7/mkcls-v2/
PATH=$PATH:/usr/local/mosesdecoder/bin/
PATH=$PATH:/usr/local/srilm/bin/i686-m64/
export SCRIPTS_ROOTDIR=/usr/local/mosesdecoder/scripts/
```

###語料樣式探討
##產生文本
請看`資料處理/處理`
這馬無維護

##走華臺樣式實驗
下跤的程式是佇國網中心平行處理的
一个樣式愛3~4G的記憶體
若電腦記憶體無夠，請家己提掉腳本內底的背景執行(&)

#產生文本而且訓練
這幾个會使做伙做
```bash
華臺斷字指令
華臺斷詞指令
華臺斷詞組指令
華臺上長詞對前指令       
華臺上長詞對後指令    
```
#訓練別的樣式模型
```bash
華臺練模型指令
```
#算分數
載入模型（請看電腦能力人工拍開）
```bash
華臺架服務指令
```
翻譯資料出來
```bash
華臺走結果指令
#拍分數
佇專案目錄內
```bash
華臺評分
```

##提著TGB平行語料
====================
解析TGB
分TGB語料
斷語料
對齊語料