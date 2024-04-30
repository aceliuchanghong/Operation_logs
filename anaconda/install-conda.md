### 安装 anaconda

```shell
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
sh Anaconda3-2023.09-0-Linux-x86_64.sh
# 注意此处改成conda的安装路径
echo 'export PATH=/root/anaconda3/bin:$PATH'>> ~/.bashrc
source ~/.bashrc
conda env list
rm Anaconda3-2023.09-0-Linux-x86_64.sh
```

conda在linux环境
```shell
conda create -n mySummary python=3.11
source activate mySummary
```

### reference

* [常用安装命令](https://github.com/aceliuchanghong/media_work_model/blob/main/my_env.ipynb)
