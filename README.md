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


###實驗
======================
下跤的程式是佇國網中心平行處理的
一个樣式愛3~4G的記憶體
若電腦記憶體無夠，請家己提掉腳本內底的背景執行(&)
實驗請照先後走，後壁的實驗可能需要頭前實驗的物件

##產生文本
請看`資料處理/處理`
這馬無維護
毋過檔案應該都有存佇git面頂

####斷詞方法比較
```bash
cd 教育部斷詞/ #先入來資料夾
PYTHONPATH=.. python3 產生教育部例句語料.py
```
```bash
PYTHONPATH=.. python3 語料斷詞.py #產生長詞優先、拄好長度斷詞的結果
```
```bash
PYTHONPATH=.. bash 斷詞看分數指令
```

####互相校對
```bash
cd 校對/ #先入來資料夾
PYTHONPATH=.. python3 互相訓練.py #產生訓練的語料
```
訓練翻譯模型
```bash
bash 走全部指令
```
```bash
bash 架服務指令 #試驗做了會當`killall -15 mosesserver`關掉
```
```bash
bash 做試驗指令
```
```bash
bash 看分數指令
```


####提著TGB平行語料
====================
解析TGB
分TGB語料
斷語料
對齊語料


###斷詞斷字比較
####訓練模型
```bash
訓練摩西斷詞佮斷字模型.py
```
####架摩西服務
```bash
bash 比較走結果指令
```
####走實驗
```bash
bash 比較架服務指令
```
####看實驗分數
```bash
bash 比較看分數指令
```

##走華臺樣式實驗（無維護）
產生文本而且訓練
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
