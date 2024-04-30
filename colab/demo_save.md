### 模型转存到google drive云盘

```shell
# 克隆模型
git lfs install
git clone https://huggingface.co/mistralai/Mistral-7B-v0.1 /content/sample_data/00

# 确保文件存在,搭载云盘
import os
my_files = '/content/drive/MyDrive/fine_tune_log'
for dirname, _, filenames in os.walk(my_files):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
# 复制保存文件        
cp -r /content/sample_data/00 /content/drive/MyDrive/fine_tune_log/files
```
