### 命令行调用OCR记录

有点类似ffmpeg

1. 下载好安装包解压到本地 进入 powerShell 就执行了,首先检查一下可以使用不

```shell
.\Umi-OCR.exe --help
```

![img.png](..%2Fusing_files%2Fimg%2Focr%2Fimg.png)

2. 在高级选项里面开启http服务,重启即可

```text
访问 http://127.0.0.1:1224/ 看是否成功
```

3. 手动测试一下,结果很不错

![img_1.png](..%2Fusing_files%2Fimg%2Focr%2Fimg_1.png)

4. 测试命令行
```text
指定路径示例：
.\Umi-OCR.exe --path "C:\Users\lawrence\PycharmProjects\Operation_logs\using_files\img\ocr\test\img.png"

指定多个路径示例：
.\Umi-OCR.exe --path "C:\Users\lawrence\PycharmProjects\Operation_logs\using_files\img\ocr\test\img.png" "C:\Users\lawrence\PycharmProjects\Operation_logs\using_files\img\ocr\img.png"

传入文件夹的路径:
.\Umi-OCR.exe --path "C:\Users\lawrence\PycharmProjects\Operation_logs\using_files\img\ocr\test\"

结果输出
复制到剪贴板  --clip
输出到文件（覆盖）  --output "文件路径.txt"
输出到文件（追加）  --output_append "文件路径.txt"

.\Umi-OCR.exe --path "C:\Users\lawrence\PycharmProjects\Operation_logs\using_files\img\ocr\test\img.png" --output "C:\Users\lawrence\PycharmProjects\Operation_logs\using_files\img\ocr\test\img.txt"
.\Umi-OCR.exe --path "C:\Users\lawrence\PycharmProjects\Operation_logs\using_files\img\ocr\test\img.png" --output_append "C:\Users\lawrence\PycharmProjects\Operation_logs\using_files\img\ocr\test\img.txt"
```

```python
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

```
### 吐槽

```text
这个webui时慢时快,搞不懂
```

### Reference

* [官方github库](https://github.com/hiroi-sora/Umi-OCR)
