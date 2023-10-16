
# HarmonyOS 设备调试

参考：
https://blog.csdn.net/hanru723/article/details/117563773


## 步骤

1. 在[主页](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)选择 `用户与访问` ，然后可以看到左下角的 `设备管理` 与 `证书管理`
2. 设备管理是需要添加设备的 udid ，udid 的获取方法是 `hdc shell` 或者 `adb shell` 进入到设置终端内，然后执行命令 `bm get --udid` 获取，然后添加进去
3. 证书管理是要添加的证书是从 DevEco Studio 内生成的 esr 证书，在 Build -> `Generate Key And Csr` 内按照步骤生成，这里可以拿到 `p12` 和 `csr` 证书
4. 此时回到 证书管理 页面，在这里添加 csr 证书即可。添加完成后，可以看到下载选项，这里点击下载就拿到了 `cer` 证书文件。
5. 然后新建项目和 HarmonyOS 应用，创建成功后，切换到应用的详情页面，最左下角可以看到 `HarmonyOS应用` -> `HAP Provision Profile`，然后再这里添加并配置 Profile。里面要去选择证书和设备，证书和设备都是上面添加的
6. 当添加 Profile 成功后，可以点击下载按钮下载 p7b 文件；此时，项目内需要的证书文件就都全了
7. 最后在 DevEco Studio 内 `Proejct Structure` -> `Singing Configs` 内配置 p12 / p7b / cer 对应的文件，然后 hap 就可以正常安装了。



## 中间主要遇到的错误

Failure[MSG_ERR_INSTALL_FAILED_VERIFY_APP_PKCS7_FAIL]  是因为配置的 csr / cer / p7b 对应不上
Failure[MSG_ERR_INSTALL_FAILED_APP_SOURCE_NOT_TRUESTED]   是因为配置的 csr / cer / p7b 对应不上
Failure[MSG_ERR_INSTALL_GRANT_REQUEST_PERMISSIONS_FAILED]  是因为在 module.json5 内声明的权限太多了



