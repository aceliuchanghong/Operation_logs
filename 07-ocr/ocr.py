import requests
import json

url = "http://127.0.0.1:1224/argv"
data = ["--path", "C:/Users/lawrence/PycharmProjects/Operation_logs/using_files/img/ocr/test/img.png"]

# 接口暂不支持pdf类
data2 = ["--path", "C:/Users/lawrence/Desktop/Resume.pdf"]

headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("截图结果：\n", response.text)
    else:
        print("请求失败:", response.status_code)
except Exception as e:
    print("发生错误:", e)
