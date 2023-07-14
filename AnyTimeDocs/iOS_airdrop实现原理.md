

# 总结

1. 通过 BLE 发现设备
2. 发现设备后，建立 wifi 对等网络，就是 wifi p2p 
3. 通过 bonjour 网络通信
4. bonjour 是零配置网络的一种实现，bounjour 是什么呢？可以扫描各种临近设备信息，mdns



# AirDrop实现原理

#### You:
airdrop 接收方的设备扫描可用的 Wi-Fi 网络并查看发送方的设备，这个是怎样实现的？怎样可以查看发送方的设备？

#### ChatGPT:
# I will search for information on how Airdrop receives devices scan available Wi-Fi networks and see the sender's device.

search("airdrop 接收方的设备扫描可用的 Wi-Fi 网络并查看发送方的设备 怎样实现")


#### Plugin (browser):
> [How to use AirDrop on your iPhone or iPad - Apple Support](https://support.apple.com/en-us/HT204144)
> [如何在 iPhone 或 iPad 上使用 AirDrop - Apple 支援 (台灣)](https://support.apple.com/zh-tw/HT204144)
> [AirDrop security - Apple Support](https://support.apple.com/guide/security/airdrop-security-sec2261183f4/web)
> [苹果 隔空投送 AirDrop 原理 - 知乎 - 知乎专栏](https://zhuanlan.zhihu.com/p/566055452)
> [如何在 iPhone 或 iPad 使用 AirDrop - Apple 支援 (香港)](https://support.apple.com/zh-hk/HT204144)
> [安心传，尽情传：解读 AirDrop 的隐私安全 - 少数派](https://sspai.com/post/27613)
> [AirDrop：蓝牙还是Wi-Fi？ - QA Stack](https://qastack.cn/apple/146644/airdrop-bluetooth-or-wi-fi)
> [iOS 7 的 AirDrop 是利用什么信号来传输的？ - 知乎](https://www.zhihu.com/question/21189545)
> [【教學】Windows 也能 AirDrop 無線 WiFi 與 iPhone / iPad 互傳分享照片、影片與檔案](https://app.yipee.cc/115645/%E3%80%90%E6%95%99%E5%AD%B8%E3%80%91windows-%E4%B9%9F%E8%83%BD-airdrop-%E7%84%A1%E7%B7%9A-wifi-%E8%88%87-iphone-ipad-%E4%BA%92%E5%82%B3%E5%88%86%E4%BA%AB%E7%85%A7%E7%89%87%E3%80%81%E5%BD%B1%E7%89%87/)
> [AirDrop 必须在同一个 Wi-Fi 下才可以传输吗？ - 爱范儿](https://www.ifanr.com/app/851501)
> [Search results for query: 'airdrop 接收方的设备扫描可用的 Wi-Fi 网络并查看发送方的设备 怎样实现']()


#### ChatGPT:
# I will click on the result that seems to explain the principles of how Airdrop works.

click(3)


#### Plugin (browser):


#### ChatGPT:
# Since I couldn't click on the link that seemed most relevant, I'll click on another link that might explain how Airdrop works.

click(6)


#### Plugin (browser):
> [AirDrop：蓝牙还是Wi-Fi？](https://qastack.cn/apple/146644/airdrop-bluetooth-or-wi-fi)


#### ChatGPT:
# I will store the information that explains how Airdrop works.

quote("支持AirDrop的iOS设备使用 低功耗蓝牙（BLE）和Apple创建的对等Wi-Fi技术", "组织可以限制使用 MDM解决方案 管理的设备或应用程序 使用AirDrop 。")


#### Plugin (browser):
> AirDrop：蓝牙还是Wi-Fi？


#### ChatGPT:
AirDrop 是苹果的一种无线文件共享技术，适用于 iOS 和 macOS 设备。以下是 AirDrop 的工作原理：

1. **低功耗蓝牙和对等 Wi-Fi 技术**: 当用户启用 AirDrop 时，支持 AirDrop 的 iOS 设备使用低功耗蓝牙 (Bluetooth Low Energy, BLE) 和 Apple 创建的对等 Wi-Fi 技术来发送文件和信息到附近的设备。Wi-Fi 无线电用于设备之间的直接通信，不需要互联网连接或 Wi-Fi 接入点。

2. **身份识别**: AirDrop 在设备上存储一个 2048 位的 RSA 身份，并根据与用户的 Apple ID 关联的电子邮件地址和电话号码创建一个 AirDrop 身份哈希。

3. **信号和响应**: 当用户选择 AirDrop 作为文件共享的方式时，设备通过 BLE 发出 AirDrop 信号。其他处于唤醒状态、接近并已打开 AirDrop 的设备会检测到此信号，并以其所有者的身份哈希的缩短版本进行响应。

4. **创建对等 Wi-Fi 网络**: 如果 AirDrop 设置为“仅限联系人”模式，并且找到与接收到的身份哈希匹配的联系人，发送设备将创建对等 Wi-Fi 网络，并使用 Bonjour 通告 AirDrop 连接。使用此连接，接收设备将其完整的身份哈希发送给发起方。

5. **TLS 加密连接**: 发送设备与接收设备建立加密的 TLS 连接，该连接交换 iCloud 身份证书。发送用户可以选择要与之共享的人。

6. **接收用户的确认**: 系统要求接收用户接受来自已识别的人或设备的传入传输。

7. **所有人模式**: 在“所有人”模式下，将使用与“仅限联系人”模式相同的过程，但如果未找到匹配的联系人，则接收设备将在 AirDrop 发送表中显示，附带一个带有设备名称的剪影。

这个过程使 AirDrop 能够安全、快速地在设备之间共享文件，而无需通过互联网或使用电子邮件【9†source】。


#### You:
airdrop 建立连接的具体逻辑是什么？通过 ble 发现设备？那么 bonjour 是用来做什么？

#### ChatGPT:
是的，AirDrop 使用低功耗蓝牙 (BLE) 来发现附近的设备。具体来说，当一个设备使用 AirDrop 时，它会通过 BLE 广播一个信号。其他处于唤醒状态、接近并已启用 AirDrop 的设备会检测到这个信号，并以其所有者的身份哈希的缩短版本响应。这是一个设备发现阶段。

接下来是建立连接的阶段。如果 AirDrop 设置为“仅限联系人”模式，并且找到与接收到的身份哈希匹配的联系人，发送设备将创建一个对等 Wi-Fi 网络。这是通过 Apple 创建的对等 Wi-Fi 技术实现的，它允许设备之间直接通信，而无需使用任何互联网连接或 Wi-Fi 接入点。

Bonjour 在这个过程中起着重要的作用。Bonjour 是 Apple 的零配置网络服务，它允许设备在局域网上自动发现其他设备和服务，而无需进行手动配置。在 AirDrop 中，一旦通过 BLE 发现设备并建立对等 Wi-Fi 网络，Bonjour 就用于通告 AirDrop 连接。简单地说，它是用来告诉接收设备，“嘿，我在这里，我想通过 AirDrop 与你共享文件”。通过使用 Bonjour，发送设备和接收设备能够在没有互联网连接的情况下找到彼此并建立一个安全的连接。

接下来，发送设备与接收设备建立加密的 TLS 连接，该连接交换 iCloud 身份证书，以验证双方的身份。

最后，系统要求接收用户接受来自已识别的人或设备的传入传输。一旦接收用户接受，文件传输就会开始。

总的来说，AirDrop 使用 BLE 来发现设备，使用对等 Wi-Fi 技术来建立直接的网络连接，并使用 Bonjour 来通告和协助建立连接，最后通过加密的 TLS 连接安全地传输文件【9†source】。


#### You:
零配置网络服务 是什么？

#### ChatGPT:
零配置网络服务，通常简称为零配置或 Zeroconf，是一种网络技术，允许计算机和其他设备在局域网（Local Area Network, LAN）内自动配置其网络设置，并发现其他设备和网络服务，而无需用户手动输入配置信息或使用专用的配置服务器。

零配置网络服务主要解决三个基本问题：

1. **自动分配 IP 地址**：当一个设备连接到网络时，零配置允许它自动获得一个 IP 地址，即使没有 DHCP 服务器也可以完成这个过程。

2. **自动发现网络服务和设备**：零配置允许设备在网络上广播其存在和提供的服务，并允许其他设备发现并与其交互。

3. **自动解析主机名**：零配置使设备能够将本地网络上的主机名解析为 IP 地址，而无需使用 DNS 服务器。

Apple 的 Bonjour 是零配置网络服务的一种实现，广泛应用于 Apple 的产品和服务。它是基于多播 DNS（mDNS）的，允许设备在没有传统 DNS 服务器的局域网上发布和发现服务。这对于家庭网络和小型办公网络非常有用，因为用户通常没有网络管理经验，也没有配置复杂网络服务的需求。

通过使用零配置网络服务，设备可以轻松地在网络上找到彼此，并自动配置必要的网络设置，使用户能够无缝地共享文件、打印机、流媒体服务等，而无需复杂的设置过程。


#### You:
对等 wifi 网络是什么
？

#### ChatGPT:
对等 Wi-Fi 网络，也称为 Wi-Fi Direct 或 Wi-Fi P2P（Peer-to-Peer），是一种允许 Wi-Fi 设备直接彼此通信的网络标准。在传统的 Wi-Fi 网络中，通常需要一个中央的接入点（如无线路由器）来管理设备之间的通信。然而，在对等 Wi-Fi 网络中，设备可以直接彼此连接，无需通过中央接入点。

以下是对等 Wi-Fi 网络的一些关键特点：

1. **直接连接**：对等 Wi-Fi 网络允许两个或更多的 Wi-Fi 设备直接相互连接。这对于无需互联网连接的场景，如文件共享、打印或流式传输媒体内容非常有用。

2. **设备发现和服务发现**：通过使用 Wi-Fi Direct，设备可以自动发现彼此的存在，以及它们提供的服务。这类似于零配置网络服务，但是特定于 Wi-Fi 设备。

3. **高速数据传输**：由于对等 Wi-Fi 网络允许设备直接通信，通常可以实现比通过传统 Wi-Fi 网络更快的数据传输速率。

4. **简单配置**：Wi-Fi Direct 设计为简单易用，通常不需要复杂的配置过程。设备可以通过按下按钮、输入 PIN 或使用近场通信（NFC）快速配对。

5. **安全性**：对等 Wi-Fi 网络通常使用 WPA2 或 WPA3 加密来保护数据的安全。

Wi-Fi Direct 在各种应用场景中很受欢迎，包括文件共享、无线打印、屏幕投影和多人游戏。例如，AirDrop 使用对等 Wi-Fi 技术来在 Apple 设备之间快速共享文件。同样，Android 设备也可以使用 Wi-Fi Direct 来进行文件传输和其他任务。


#### You:
那在 airdrop 的时候，bonjour 和 wifi p2p 冲突吗？都代表什么样的角色？

#### ChatGPT:
在 AirDrop 中，Bonjour 和 Wi-Fi P2P（对等 Wi-Fi 网络）是协同工作的，而不是冲突的。它们在 AirDrop 的工作过程中扮演不同的角色：

1. **Wi-Fi P2P（对等 Wi-Fi 网络）**:
   - *作用*: Wi-Fi P2P 负责在设备之间建立一个直接的网络连接。这使得两个 AirDrop 设备能够直接通信，而不需要通过 Wi-Fi 接入点或互联网。
   - *在 AirDrop 中的角色*: 当你使用 AirDrop 分享文件时，你的设备会使用 Wi-Fi P2P 创建一个对等网络，允许它直接与接收设备通信。这种直接的连接允许高速、安全的文件传输。

2. **Bonjour**:
   - *作用*: Bonjour 是一种零配置网络技术，允许设备在局域网上自动发现其他设备和服务。它使用多播 DNS（mDNS）来发现局域网内的服务和设备。
   - *在 AirDrop 中的角色*: 一旦通过 Wi-Fi P2P 建立了对等网络，Bonjour 就会用于通告 AirDrop 连接。它告诉接收设备，“嘿，我在这里，我想通过 AirDrop 与你共享文件”。Bonjour 使发送设备和接收设备能够在没有互联网连接的情况下找到彼此，并协助建立一个安全的连接。

总的来说，Wi-Fi P2P 负责建立 AirDrop 设备之间的物理网络连接，而 Bonjour 则负责在这个网络上发现服务和设备。这两个技术在 AirDrop 中协同工作，使文件共享变得简单和高效。在这个过程中，它们并不冲突，而是各自发挥着不同的作用。


