### 服务器换源

```shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### Create

```shell
conda env list
conda create --name myenv python=3.8
conda remove --name myenv --all
conda create --prefix /path/to/myenv python=3.8
rm -rf /path/to/myenv
```
