import requests
import json


def get_text(filepath):
    url = "http://127.0.0.1:1224/argv"
    headers = {"Content-Type": "application/json"}
    data = ["--path", filepath.replace("\\", "/")]
    for i in range(5):
        F5_url()
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print("截图结果：\n", response.text)
            return response.text
        else:
            print("请求失败:", response.status_code)
            return "请求失败:" + str(response.status_code)
    except Exception as e:
        return "发生错误:" + str(e)


def get_text2(filepath):
    return filepath.replace("\\", "/")


def F5_url():
    url = 'http://127.0.0.1:1224/'
    res = requests.get(url)
    print(res)
