


发现不同的运营商下拿到的 基站 CI 值是一样的，对应的频点和 mnc 都是不一样的，所以需要进一步去了解基站 CI 的构成和区别，以及怎样能确认是具有唯一性的 CI 。



# 全局唯一的基站 ID

## LTE:

eNB (evolved Node B)

ECGI = MCC + MNC + ECI
ECI = eNB ID(20Bit) + Cell ID  (8Bit)

示例： 128953226 % 256 = 503723 + 138

ECI (E-UTRAN Cell Identifier) ，是指 "Evolved UMTS Terrestrial Radio Access Network"，即演进的UMTS陆地无线接入网络

ECI 总共是 28 位；

eNB 代表 "evolved Node B"，"evolved" 表示这是从3G UMTS网络演进而来的，"Node B" 是 3G UMTS 网络中基站的术语；
标识LTE网络中的基站设备，在一个 PLMN（Public Land Mobile Network）内唯一标识一个 eNB。



## NR:

NCGI（NR Cell Global Identifier）

NCGI = PLMN Identity + NCI (NR Cell Identity)

PLMN Identity = MCC（Mobile Country Code） + MNC（Mobile Network Code）

NCI = gNB ID(24bit) + Cell ID (12Bit)

示例：5781295126 % 4096 = 1411449 + 22 

NCI 总共是 36 位；

gNB 代表 "next generation Node B"，"next generation" 表明这是为5G设计的新一代基站；
标识 5G NR 网络中的基站设备，在一个 PLMN 内唯一标识一个 gNB。


# 参考


## 1.

1. eNB ID (LTE网络):

- 名称解释：
  eNB 代表 "evolved Node B"
  "evolved" 表示这是从3G UMTS网络演进而来的
  "Node B" 是3G UMTS网络中基站的术语

- 意义：
  标识LTE网络中的基站设备
  在一个PLMN（Public Land Mobile Network）内唯一标识一个eNB

- 构成：
  通常为20位比特串
  可以支持宏基站（Macro eNB）、家庭基站（Home eNB）等不同类型

- 用途：
  网络规划和管理
  邻区关系建立
  切换（Handover）管理

2. gNB ID (5G NR网络):

- 名称解释：
  gNB 代表 "next generation Node B"
  "next generation" 表明这是为5G设计的新一代基站

- 意义：
  标识5G NR网络中的基站设备
  在一个PLMN内唯一标识一个gNB

- 构成：
  可变长度，范围是22-32位比特串
  中国移动选择使用24位

- 用途：
  5G网络规划和管理
  支持更复杂的网络拓扑
  便于大规模MIMO和波束赋形等5G特性的实现

3. 命名逻辑：

- eNB（evolved Node B）反映了从3G到4G的演进过程，强调了与之前技术的连续性。
- gNB（next generation Node B）强调了5G作为新一代技术的革新性，表明这是一个全新的设计。

4. 区别和联系：

- eNB专用于LTE网络，而gNB专用于5G NR网络。
- 两者都是各自网络中的关键节点，负责无线信号的发送和接收。
- gNB通常具有更高的容量和更低的延迟，以支持5G的高级特性。

5. 在中国移动网络中的应用：

- LTE网络：使用20位eNB ID + 8位Cell ID构成28位ECI。
- 5G NR网络：使用24位gNB ID + 12位Cell ID构成36位NCI。

6. 意义：

- 这种ID系统允许精确定位和管理网络中的每个基站和小区。
- 支持网络自动化和优化，如自动邻区关系（ANR）。
- 便于网络故障排查和性能分析。
- 为未来网络扩展和技术演进提供了足够的寻址空间。

总之，eNB ID和gNB ID的设计反映了移动通信技术的演进过程，同时为网络管理和优化提供了强大的工具。这种标识系统的设计考虑了技术连续性、网络复杂性和未来扩展性，是现代移动通信网络不可或缺的组成部分。

## 2. 

您提出了一个很好的问题。让我详细解释一下5G NR（New Radio）网络中的标识系统：

1. 5G NR 的小区标识：

在5G中，不再使用ECGI（E-UTRAN Cell Global Identifier）这个术语。而是改用NCGI（NR Cell Global Identifier）。

2. NCGI 的构成：

NCGI = PLMN Identity + NCI (NR Cell Identity)

- PLMN Identity: 与4G相同，由MCC（Mobile Country Code）和MNC（Mobile Network Code）组成。
- NCI: NR Cell Identity，是5G小区的唯一标识符。

3. NCI 的结构：

NCI是36位的比特串（BIT STRING），比4G的ECI（28位）长。它包含两部分：

- gNB ID（gNodeB Identifier）：可变长度，范围是22-32位。
- Cell ID：剩余的位数，范围是4-14位。

4. 中国移动的5G NCI选择：

根据您之前提供的信息，中国移动选择的NCI结构为：
NCI（36bit）= gNB ID（24Bit）+ Cell ID（12Bit）

5. gNB（gNodeB）：

这是5G网络中的基站设备，相当于4G中的eNB。

6. Global gNB ID：

全球唯一标识一个gNB，由PLMN Identity和gNB ID组成。

7. 5G小区标识CELL-ID：

- 12比特长度
- 高两位预留作为小区类型标识（初始值为00）
- 剩余10位由各省分配，可支持1024个小区

8. 小区标识（CI）规则：

采用三位数XYZ规则：
- X：表示站点类型和BBU内不同物理站点
- Y：表示扇区内载波序号
- Z：表示本物理站点内扇区序号

9. 与4G ECI的对比：

- 5G NCI（36位）比4G ECI（28位）长
- 5G提供了更大的寻址空间，支持更多的小区
- 5G的Cell ID部分（12位）比4G（8位）更长，允许更细致的小区划分

10. 标准描述：

在3GPP标准中，这些标识符通常用BIT STRING描述，例如：
- NCI: BIT STRING (SIZE(36))
- gNB ID: BIT STRING (SIZE(22..32))
- Cell ID: BIT STRING (SIZE(4..14))

总结：
5G NR网络采用了新的小区标识系统（NCGI），虽然基本原理与4G类似，但提供了更大的灵活性和寻址空间。这种设计支持更复杂的网络拓扑和更多的小区，以满足5G网络的高密度部署需求。同时，保留了分层结构（国家、网络、基站、小区），便于网络管理和优化。

## 3.

我来详细解释一下ECI的组成部分和相关专业术语：

1. eNB (evolved Node B):
   - 这是4G LTE网络中的基站设备
   - 负责无线信号的发送和接收，连接移动设备和核心网络
   - 一个eNB通常包含多个小区（cell）

2. eNB ID (20 Bit):
   - 用于唯一标识一个eNB基站
   - 在运营商网络内是唯一的
   - 可以有不同长度版本（如Macro、Home、Short Macro、Long Macro），但中国移动选择使用20位

3. Cell ID (8 Bit):
   - 标识eNB内的特定小区
   - 范围是0-255（2^8 = 256个可能值）
   - 用于区分同一eNB下的不同扇区或载波

4. ECI (E-UTRAN Cell Identifier):
   - 总长度28位
   - 组合了eNB ID和Cell ID
   - E-UTRAN指"Evolved UMTS Terrestrial Radio Access Network"，即演进的UMTS陆地无线接入网络

5. 专业数据描述：
   - 在3GPP技术规范中，这些标识符通常用BIT STRING来描述
   - 例如，eNB ID可能被描述为：BIT STRING (SIZE(20))
   - Cell ID可能被描述为：BIT STRING (SIZE(8))
   - 完整的ECI：BIT STRING (SIZE(28))

6. PLMN Identity:
   - 由MCC（Mobile Country Code，3位数字）和MNC（Mobile Network Code，2或3位数字）组成
   - 用于全球唯一标识一个移动网络运营商

7. 完整的ECGI (E-UTRAN Cell Global Identifier):
   - 包含PLMN Identity和ECI
   - 格式：MCC + MNC + ECI
   - 用于全球范围内唯一标识一个LTE小区

在实际应用中，这种标识系统允许网络设备和管理系统精确定位和管理网络中的每个小区。它在网络规划、优化、故障排除和自动化操作（如自动邻区关系ANR）中起着关键作用。


