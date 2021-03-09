#網路串接公開資料
import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
    data=json.load(response)
#列出景點名稱
travelSpot=data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
    for info in travelSpot:
        file.write(info["stitle"]+","+info["longitude"]+","+info["latitude"]+","+(info["file"]).split(".jpg", 6)[0]+".jpg"+"\n")
     

#景點名稱,經度,緯度,第一張圖檔網址
#新北投溫泉區,123.5446,24.5312,http://www.travel.taipei/pic/11000848.jpg
