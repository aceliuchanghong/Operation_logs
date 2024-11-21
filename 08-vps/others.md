linux环境安装代理VPN的步骤：

一、准备工作
将以下两个文件复制到/etc/shadowsocks/
1、shadowsocks.json
2、shadowsocks-master.zip
将一下文件复制到/etc/systemd/system/
2、shadowsocks.service

二、安装shadowsocks
1、安装shadowsocks
yum -y install epel-release
yum -y install python-pip
pip install shadowsocks-master.zip -U

2、启动shadowsocks服务
systemctl enable shadowsocks.service
systemctl start shadowsocks.service

3、验证shadowsocks
curl --socks5 127.0.0.1:1080 http://httpbin.org/ip
返回
{
“origin”: “x.x.x.x” #你的服务器IP
}

二、安装privoxy
1、privoxy
yum -y install privoxy

2、修改privoxy配置
文件：/etc/privoxy/config，增加一下内容
forward-socks5t / 127.0.0.1:1080 .	

3、启动privoxy服务
systemctl enable privoxy
systemctl start privoxy

4、修改/etc/profile
	export http_proxy=http://127.0.0.1:8118
	export https_proxy=http://127.0.0.1:8118

5、使profile生效
source /etc/profile

6、验证privoxy
curl www.google.com