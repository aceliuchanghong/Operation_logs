### no gui fix

1. Shadowsocks

```
sudo pip3 install https://github.com/shadowsocks/shadowsocks/archive/master.zip -U
或者
sudo pip3 install shadowsocks

此外，如果你需要使用 Shadowsocks 新的加密方式的话，比如 Chacha20-Ietf-Poly1305，你还需要装下面这个东西
Ubuntu
sudo apt install libsodium-dev

CentOS
sudo yum -y install epel-release
sudo yum -y install libsodium
配置
新建配置文件夹和配置文件

sudo mkdir /etc/shadowsocks
sudo vi /etc/shadowsocks/shadowsocks.json
配置如下，具体内容自行修改（没有梯子请联系工信部申请 12300@caict.ac.cn https://yhssglxt.miit.gov.cn/）

{
    "server": "your_server_url",
    "server_port": 23333,
    "local_address": "127.0.0.1",
    "local_port": 1080,
    "password": "your_server_password",
    "timeout": 60,
    "method": "chacha20-ietf-poly1305",
    "workers": 1,
    "fast_open": false
}
其中

server：提供商的 Shadowsocks 服务器地址
server_port：提供商的 Shadowsocks 服务器端口
local_address：本地 Sock5 代理地址
local_port：本地 Sock5 代理端口
password：提供商的 Shadowsocks 连接密码
timeout：超时等待时间（秒）
method：加密方式
workers：工作线程数
fast_open：TCP Fast Open，按需开启
配置完成，之后就可以通过 local_address 和 local_port 走 Sock5 代理了

启动脚本
创建启动脚本 /etc/systemd/system/shadowsocks.service

这里请确认你的 sslocal 的所在位置，自行修改脚本文件中的 /usr/local/bin/sslocal，位置不对启动服务时会报 203 错误

[Unit]
Description=Shadowsocks

[Service]
TimeoutStartSec=0
ExecStart=/usr/local/bin/sslocal -c /etc/shadowsocks/shadowsocks.json

[Install]
WantedBy=multi-user.target

GO! GO! GO!
启动服务或者配置开机自启动
# 开机自启动
sudo systemctl enable shadowsocks.service
# 启动服务
sudo systemctl start shadowsocks.service
# 查看状态
sudo systemctl status shadowsocks.service
# 停止服务
sudo systemctl stop shadowsocks.service
测试一下，看看你的 ip 地址是否符合预期 10808是我写的需要改对

curl --socks5 127.0.0.1:10808 https://httpbin.org/ip

安装privoxy
修改privoxy配置
文件：/etc/privoxy/config，增加一下内容
forward-socks5t / 127.0.0.1:1080 .
启动privoxy服务
systemctl enable privoxy
systemctl start privoxy
修改/etc/profile
export http_proxy=http://127.0.0.1:8118
export https_proxy=http://127.0.0.1:8118
使profile生效
source /etc/profile
验证privoxy
curl www.google.com

# 不需要
export http_proxy=http://127.0.0.1:10808
export https_proxy=http://127.0.0.1:10808
export http_proxy=socks5://127.0.0.1:10808
export https_proxy=socks5://127.0.0.1:10808
```

2. V2RayA
没试

### reference

* [教程](https://ry.huaji.store/2020/08/Linux-magic-network/)
