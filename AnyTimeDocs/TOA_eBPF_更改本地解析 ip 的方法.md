


# 说明

参考：
https://machbbs.com/v2ex/760285
https://twitter.com/CFC4N/status/1658881215695290386/photo/1
https://github.com/BeichenDream/FakeToa/

源站IP ACL绕过的风险  https://fangpsh.github.io/posts/2023/2023-10-02.html


这是一个通过 ebpf 实现的本地更改服务端解析 ip 的方法；
原理是在 tcp 协议内增加一个附加信息，信息的类型如下

```
Transmission Control Protocol, Src Port: 60952, Dst Port: 80, Seq: 1, Ack: 1, Len: 109
  Options: (8 bytes), Experimental
   TCP Option - Experimental: Unknown
    Kind: RFC3692-style Experiment 2 (254)
    Experiment Identifier: Unknown (0x0050)
    Data: 01020304
```

解析
```
TCP Option - Experimental：

Kind: RFC3692-style Experiment 2 (254)：这表示 TCP 选项字段中使用了一个实验性的选项，它的类型为 RFC3692 风格的实验选项2，编号为 254。RFC 3692 定义了一种用于试验和测试目的的 TCP 选项格式。
Experiment Identifier：实验标识符，用于标识特定的实验或测试。在您的例子中，它的值是未知的 (0x0050)。
Data (数据)：这是实验性选项具体的数据内容。在您的例子中是 01020304。
```

具体实现的技术可以通过 ebpf 来添加 tcp 的数据, FakeToa 可以在 ubuntu 22.04 系统内跑起来。


还有几个知识点

1. linux ebpf 的实现原理
2. tcp 协议解析，对于这个辅助码还有哪些区分
3. 对于服务端 ip 地址的解析方法，怎样解析，怎样绕过

# bpf 的实现 

# tcp 协议解析

# 服务端解析 ipv4 的方法




# 测试数据

1. 百度获取 ip 的： https://qifu-api.baidubce.com/ip/local/geo/v1/district

2. 验证在 nginx 端拿到的是已经更改的 ip ，"cat /var/log/nginx/access.log.1"



# 环境搭建

##  ubuntu 22.04 安装 bpftool

sudo yum install gcc make bison flex git
git clone https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git   //这里要选择对应的版本
cd linux/tools/bpf/bpftool
make
sudo cp bpftool /usr/local/bin/

## 脚本工具

关键词 FakeToa
"python3 toa.py attach --toa_ip 8.8.8.8"


