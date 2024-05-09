


# ja3 和 ja4 网络指纹

描述：
通过抓取网络数据包内的默认协议来分析设备指纹，比如 ja3 是根据客户端默认拼接的 加密方法排序、ec_point_formay 、elliptic_curves 等数据，拼接后计算 md5 就是了。
ja4 是多段式，包含了默认协议内的字串，也有默认 cookie 选项的 hash，a_b_c 三段。ja4+ 包含 “JA4、JA4S、JA4L、JA4H、JA4X、JA4SSH” 

```
JA4 — TLS Client   请求头顺序、加密方法的 hash、拓展的 hash
JA4S — TLS Server Response   请求头顺序、加密 chosen hash、拓展的 hash 
JA4H — HTTP Client   根据 http 协议分析的 hash
JA4L — Light Distance/Location   推算距离，去得到大概的位置
JA4X — X509 TLS Certificate 
JA4SSH — SSH Traffic
```


参考：

JA3 https://medium.com/salesforce-engineering/tls-fingerprinting-with-ja3-and-ja3s-247362855967
Jarm https://medium.com/salesforce-engineering/easily-identify-malicious-servers-on-the-internet-with-jarm-e095edac525a
jarm_github https://github.com/salesforce/jarm
主要参考 https://blog.foxio.io/ja4-network-fingerprinting-9376fe9ca637
github 项目 https://github.com/FoxIO-LLC/ja4

渗透工具 [sliver](https://github.com/BishopFox/sliver) 可以自动伪造加密方法的排序


# 关于 JA4L 位置的计算

**D = jc/p**

j 是指上下报文内时间间隔，计算方法是

```
JA4L-S = {（B-A）/2}_Server TTL
JA4L-C = {（C-B）/2}_Client TTL
```
c 是指光速，在单位为 us 时，1 us 走过的距离是 0.206 km 

p 是延迟因子，是根据 ttl 来运算的，

ttl | 延迟因子
---|---
<=21 | 1.5
22 | 1.6
23 | 1.7
24 | 1.8
25 | 1.9
>=26 | 2.0

示例：
JA4L-S = 2449
TTL = 22

则最终的距离大概是 2449*0.206/1.6=315 km

所以在设置多个数据点时，就能大概估算出真实的物理位置，取交点

# jarm

通过伪造客户端的请求数据包，分析服务端响应的 tsl 信息，以 hash 算出指纹。

是客户端主动去区分服务端是否是真实的。

对应于钓鱼伪造网站可以识别。




