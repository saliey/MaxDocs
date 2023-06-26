


# 总

1. 在使用 clash 访问 vpn 的时候，默认情况下只有浏览器能够访问 vpn 网络，而其他的应用比如 Terminal 就不能访问，这是因为默认打开的 clash 仅仅是设置为系统的代理，其他的程序默认不走系统的代理设置，所以无法建立网络。

2. 这时需要设置 tun 虚拟网络，这个是创建了一个虚拟网络接口，将所有的流量都引导到这个虚拟网络接口，然后通过 clash 进行网络通讯。

3. 正常情况下下 clash 打开代理后，它会在 'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ProxyServer' 中配置本地代理的 ip:port。
类似还有：
    HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ProxyEnable
    HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ProxyOverride

4. tun 是指网络层的代理，tap 是更底层，指链路层的代理
    TUN（网络隧道）和TAP（网络分接头）都是虚拟网络设备
    ppp 网络连接是 拨号网络和DSL连接。

5. clash tun 的使用方法：'General' -> 'Service Mode' -> 'install' -> TUN MODE
    变成小篮球就表示成功了；
    简单设置就是打开了全局代理。

6. tun0 虚拟网卡，它与物理网卡的区别是，物理网卡外接的直接是交换机或路由器，虚拟网卡外接的是代理应用，是将数据转到代理应用，然后代理应用再将数据转发到代理服务器以完成通讯。


# 1.

这是一份关于如何使用Clash for Windows的详细教程：

1. 首先，你需要下载并安装Clash for Windows。一旦下载完成，双击以安装。安装后，你可以在桌面上找到它，或者在windows搜索栏中搜索"Clash"【38†source】。

2. 然后，添加服务器。首先登录到你的仪表板，选择"Clash for Windows"，然后点击"复制API"。打开Clash，转到"Profile"，然后将API粘贴到"Download from a URL"框中，然后点击"Download"。确保你选择了新下载的服务器配置文件，而不是默认的。我们强烈建议将API设置为每天至少自动更新一次服务器列表（最好每12小时一次）【39†source】。

3. 选择一个服务器和模式，然后连接。转到"Proxies"，从顶部选择Rule模式。从"WannaFlix"列表下选择一个服务器作为你的主服务器。你也可以为Netflix和Youtube等服务选择不同的服务器。然后，转到"General"标签，切换"System Proxy"开关。你现在已经连接上了。如果你想断开连接，再次切换"System Proxy"开关。在退出应用程序之前，确保将"System Proxy"开关关闭，否则你将无法上网【40†source】。

4. 如果你想使用Clash玩游戏或让所有应用程序通过Clash，你需要安装TUN引擎。转到"General"标签，点击"Manage"，然后点击"Install"。如果正确安装，地球图标将变为绿色。现在禁用System Proxy，并启用TUN模式【41†source】。

5. Windows Store应用程序默认不会通过VPN，即使启用了TUN/TAP。你需要使用UWP Loopback Helper强制它们。转到"General"标签，点击"Launch Helper"，然后选择所有你想强制通过VPN的应用程序，然后点击"Save Changes"【42†source】。

6. 如果你希望Clash在你启动计算机时自动启动，你需要启用这个选项。转到"General"标签，切换"Start with Windows"开关【43†source】。

7. 默认情况下，当更改服务器时，旧的连接将不会被重定向到新的服务器，而会继续到旧的服务器，直到它们超时。这在你切换服务器以观看Netflix或需要特定IP地址时会造成问题，因为你刚刚访问的网站仍然会通过旧的服务器。为了终止所有连接（因此强制通过新的服务器重新连接），你需要进行以下操作：转到"Settings"，向下滚动到"Connections"，然后选择"All"，并切换"Break when Profile change"和"Break when Mode change"【44†source】。

8. 如果Clash for Windows是一个用于Windows操作系统的代理工具。它可以帮助你通过代理服务器来访问网络，包括游戏和应用程序【37†source】【29†source】。

以下是设置Clash for Windows的步骤：

1. 下载和安装Clash for Windows。你可以在GitHub或其他下载站点找到它【38†source】【29†source】。

2. 下载并安装好后，你需要导入Clash配置文件。你可以通过拖拽方式来导入，或者如果你有自己的节点并希望将其转换为Clash订阅链接，你可以访问订阅转换器来完成这个操作【29†source】【39†source】。

3. 连接到你的服务器。你需要打开Clash应用，然后在"Proxies"菜单中选择你的服务器。你也可以为如Netflix、YouTube等服务选择不同的服务器【40†source】。

4. 打开"General"标签，然后切换"System Proxy"开关。这样你就连接上了。如果你想断开连接，只需再次切换"System Proxy"开关【40†source】。

以下是一些额外的步骤，这些步骤可以帮助你更好地使用Clash for Windows：

1. 安装TUN引擎：如果你想要玩游戏或让所有应用程序都通过Clash，你需要安装TUN引擎。你可以在"General"标签下找到"Manage"选项，点击后选择"Install"【41†source】。

2. 使用UWP Loopback Helper强制Windows Store应用程序通过VPN：默认情况下，即使启用了TUN/TAP，Windows Store应用程序也不会通过VPN。你需要使用UWP Loopback Helper来强制它们通过VPN。你可以在"General"标签下找到"Launch Helper"选项，点击后选择你想要强制通过VPN的应用程序，然后点击"Save Changes"【42†source】。

3. 开机启动Clash：如果你希望在启动计算机时自动启动Clash，你需要开启这个选项。你可以在"General"标签下找到"Start with Windows"开关，切换开关即可【43†source】。

4. 在更换服务器时终止所有连接：默认情况下，旧的连接不会被重定向到新的服务器，而是会继续连接到旧的服务器，直到超时。为了解决这个问题，你需要在"Settings"标签下找到"Connections"选项，然后在"Break when proxy change"旁边选择"All"，同时也切换"Break when Profile change"和"Break when Mode change"的开关【44†source】。


# 2.

TUN（网络隧道）和TAP（网络分接头）都是虚拟网络设备。它们在网络层（TUN）和数据链路层（TAP）上工作，可以用来实现VPN或其他网络相关的应用。

TUN设备工作在第3层，即网络层，主要处理IP包。当应用程序向TUN设备写入数据时，系统会认为这些数据来自网络层，然后进行相应的路由。同样，当网络层的数据发给TUN设备时，应用程序可以读取到这些数据。这样，我们就可以在用户空间程序和内核网络协议栈之间建立起一个隧道。

TAP设备工作在第2层，即数据链路层，处理的是以太网帧。它的工作原理和TUN设备类似，不过TAP设备可以更好地模拟真实的网络设备，因为它可以接收和发送的是完整的以太网帧，包括MAC地址等信息。这使得TAP设备能够用于构建桥接网络或者软件交换机等网络设备。

TUN和TAP通常被放在一起讨论，因为它们都是虚拟网络设备，功能上有一定的相似性，但工作的网络层级不同，因此在实际使用中，会根据具体的需求选择使用TUN设备还是TAP设备。

在Clash等软件中，一般使用TUN模式，是因为TUN模式工作在网络层，对于大部分网络应用（比如浏览器，邮件客户端等）已经足够。TUN模式可以捕获和处理这些应用产生的IP包，将它们转发到正确的网络接口（比如VPN隧道），实现网络代理的功能。


# 3.
在 Windows 上，Clash for Windows 使用 Windows 提供的 API 来修改系统的代理设置。具体来说，它会修改以下的注册表键值来改变系统代理设置：

- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ProxyEnable`：这个键值控制是否启用代理。Clash for Windows 会把它设置为1，以启用代理。
- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ProxyServer`：这个键值定义了代理服务器的地址和端口。Clash for Windows 会把它设置为自己的本地代理服务器地址和端口。
- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ProxyOverride`：这个键值定义了一些不走代理的地址。Clash for Windows 一般会把它设置为空，以使所有的流量都走代理。

以上的操作都需要 Windows 管理员权限，Clash for Windows 会在需要的时候弹出 UAC 提示框请求这个权限。

在这些设置被修改之后，大部分遵循系统代理设置的应用（包括大部分浏览器）就会开始通过 Clash 的本地代理服务器来发送和接收数据。然而，一些应用可能不遵循系统代理设置，或者只在启动时读取一次系统代理设置。这种情况下，这些应用就需要使用额外的工具（如 Proxifier、UWP Loopback Helper 或 TUN/TAP）来强制它们走代理【17†source】【42†source】。

另外，Clash for Windows 还支持启用 "System Proxy" 和 "TUN Mode"。当 "System Proxy" 开启时，Clash for Windows 将自动设置系统代理，让大多数应用通过 Clash 连接网络。当 "TUN Mode" 开启时，Clash 通过更改系统 DNS 服务器，重定向所有网络请求，包括那些不遵循系统代理设置的应用的网络请求【41†source】。

总的来说，当 Clash 代理开启后，系统的网络配置将会改变，让网络流量通过 Clash 的本地代理服务器发送和接收，从而实现网络流量的管理和控制。

# 4.

TUN和TAP都是虚拟网络内核接口的名称，它们是操作系统中的内核级别网络设备。这两个名字的由来和它们的功能有关。

- TUN：TUN代表“网络隧道”，它操作第3层的网络协议（例如IP）。TUN设备允许用户空间程序接收到或者发送去往网络层的数据包。这意味着，通过TUN设备，你可以处理IP数据包，例如在用户空间的VPN程序中。

- TAP：TAP代表“网络分接头”，它操作第2层的数据链路层协议（例如Ethernet）。TAP设备可以使用户空间程序接收或发送链路层的数据帧。使用TAP设备，你可以创建一个在用户空间程序和内核网络栈之间的虚拟网络桥接。

这两种接口都可以用于例如VPN等网络应用，选择使用哪种接口取决于你想在哪个网络层次操作数据。

# 5.

TUN（网络隧道）和TAP（网络分接头）都是虚拟网络设备。它们在网络层（TUN）和数据链路层（TAP）上工作，可以用来实现VPN或其他网络相关的应用。

TUN设备工作在第3层，即网络层，主要处理IP包。当应用程序向TUN设备写入数据时，系统会认为这些数据来自网络层，然后进行相应的路由。同样，当网络层的数据发给TUN设备时，应用程序可以读取到这些数据。这样，我们就可以在用户空间程序和内核网络协议栈之间建立起一个隧道。

TAP设备工作在第2层，即数据链路层，处理的是以太网帧。它的工作原理和TUN设备类似，不过TAP设备可以更好地模拟真实的网络设备，因为它可以接收和发送的是完整的以太网帧，包括MAC地址等信息。这使得TAP设备能够用于构建桥接网络或者软件交换机等网络设备。

TUN和TAP通常被放在一起讨论，因为它们都是虚拟网络设备，功能上有一定的相似性，但工作的网络层级不同，因此在实际使用中，会根据具体的需求选择使用TUN设备还是TAP设备。

在Clash等软件中，一般使用TUN模式，是因为TUN模式工作在网络层，对于大部分网络应用（比如浏览器，邮件客户端等）已经足够。TUN模式可以捕获和处理这些应用产生的IP包，将它们转发到正确的网络接口（比如VPN隧道），实现网络代理的功能。

# 6.

TUN0 是一个虚拟网卡设备，可以看到它与物理网卡相同的地方在于它们的一端都连接内核协议栈，不同的地方在于物理网卡另一端连接的是外面的交换机或者路由器等硬件设备，TUN0 连接的是处于用户层的应用程序，协议栈发送给虚拟网卡的数据都被发送到了应用程序中，通过加密，转换，校验等方式后通过物理网卡发送出去。

