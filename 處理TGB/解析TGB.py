import json
from 處理TGB.提掉網頁標仔工具 import 提掉網頁標仔工具

class 解析TGB:
    def 讀(self,json檔名):
        json檔案=open(json檔名)
        全部=json.loads(json檔案.read())
        json檔案.close()
        for 資料 in 全部:
            標題工具=提掉網頁標仔工具()
            標題工具.feed(資料['title'][0])
            print(標題工具.結果())
            時間工具=提掉網頁標仔工具()
            時間工具.feed(資料['date'][0])
            print(時間工具.結果())

if __name__=='__main__':
    TGB=解析TGB()
    TGB.讀('../原來TGB.json')
    