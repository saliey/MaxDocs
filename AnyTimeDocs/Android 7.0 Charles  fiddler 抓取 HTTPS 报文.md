


# first longlong ago

1. 下载 charles 工具  https://www.charlesproxy.com/ 并安装
2. 打开 charles 后，网页打开 'chls.pro/ssl' 下载证书
3. 命令 'openssl x509 -subject_hash_old -in <Certificate_File>' 得到更改后的名字，示例 `75b835b6.0`
3.1 如果是 fiddler 的 FiddlerRoot.cer 证书，则可以先 'openssl x509 -inform der -in certificate.cer -out certificate.pem' 转成 pem，然后再转成 旧散列值
4. 将 75b835b6.0 文件挂载到 Android '/system/etc/security/cacerts/' 目录下并赋予权限

```
adb push 75b835b6.0 /sdcard/
adb shell 
su
mount -o rw,remount /system
cd /system/etc/security/cacerts/
cp /sdcard/75b835b6.0 ./
chmod 644 75b835b6.0
reboot
```
重启手机后，可在设置 -> 安全 -> 信任的凭据 找到 Charles 的证书

5. 手机和 PC 连接到同一网络，在 PC Charles 内 'Help -> Local IP Address' 查看 PC 的 IP 地址
6. PC Charles 内 'Proxy -> Proxy Settings' 查看端口
7. PC Charles 内 'Help -> SSL Proxying -> Install Charles Root Certificate' 安装证书
8. PC Charles 内  'Proxy -> SSL Proxying Settings -> SSL Proxying -> Add' 填写 port 443 ，点 OK
9. 抓包


参考连接：
https://mp.weixin.qq.com/s/kqMUbHl59V75w8xBxHbXkA
https://juejin.im/post/6844903775086313480
https://stackoverflow.com/questions/25477424/adb-shell-su-works-but-adb-root-does-not
https://www.cnblogs.com/jeason1997/p/12410537.html

# 20230920 
更新：
1. 对于高 android 系统版本，不允许 mount /system 为 rw 权限，可以使用 (ro2rw){https://sourceforge.net/projects/multi-function-patch/files/RO2RW/} 工具进行处理，这个需要转到 recovery 模式下刷进去，还需要通过 + - 操控选择
2. 然后 'mount -o rw,remount /' 就可以写入
3. 不同系统 recovery 不同，需要去找

20240806:
1. 使用 magisk RO2RW 刷进去
2. 然后 adb shell su -> ro2rw
3. 然后参考 https://xdaforums.com/t/set-your-system-folder-to-r-w-mode-with-ro2rw-android-13-magisk-2024-method.4648921
4. 最后：
5. 1）将你的 super-rw-sparse-fastboot-active-_???.img 重命名为 super.img
   2）打开ADB并将手机连接到PC
   3) fastboot flash super super.img
   4) fastboot reboot
6. 

# 20240807:

使用 magisk 软件过掉抓包，参考 http://testingpai.com/article/1688797810298
下载： https://github.com/mobile46/TrustMeAlready/releases/tag/v1.0
    https://github.com/ViRb3/TrustMeAlready/releases/tag/v1.11

1. 安装 magisk 
2. magisk 内安装 lsposed https://github.com/LSPosed/LSPosed
3. 安装 lsposed-manager  https://play.google.com/store/apps/details?id=org.lsposed.manager&hl=en_US
4. 安装 TrustMeAlready.apk 文件 
5. 在 lsposed 内选择 TrustMeAlready 并选择对应的 app 
6. 然后 wlan 设置代理，使用 charles / fiddler 去抓包



# 其他 

1. Fiddler 去掉 windows 的代理
 打开 Fiddler
点击菜单栏中的 "Tools" > "Options"
在弹出的选项窗口中，选择 "Connections" 标签页
找到 "Act as system proxy on startup" 选项
取消勾选这个选项
点击 "OK" 保存设置
重启 Fiddler
2. 还有这个验证失败， 逻辑比较像，https://juejin.cn/post/7187426974883643452
3. 

