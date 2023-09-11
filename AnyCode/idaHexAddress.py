
import binascii

def reverse_hex(hex_str: str) -> str:
    # 移除输入字符串中的所有空格
    cleaned_hex_str = hex_str.replace(" ", "")
    # 判断是否为偶数长度，否则在最前面加0补齐
    if len(cleaned_hex_str) % 2 != 0:
        cleaned_hex_str = '0' + cleaned_hex_str
    # 分割成两个字符一组的列表
    hex_pairs = [cleaned_hex_str[i:i + 2] for i in range(0, len(cleaned_hex_str), 2)]
    # 反转列表并拼接成新的字符串
    reversed_hex_str = ''.join(reversed(hex_pairs))
    # 添加 "0x" 前缀并返回
    return '0x' + reversed_hex_str.upper()

def subtract_hex_addresses(hex1: str, hex2: str) -> str:
    # 移除输入字符串中的所有空格和 "0x" 前缀
    cleaned_hex1 = hex1.replace(" ", "").replace("0x", "")
    cleaned_hex2 = hex2.replace(" ", "").replace("0x", "")
    # 将 hex 字符串转换为整数
    int1 = int(cleaned_hex1, 16)
    int2 = int(cleaned_hex2, 16)
    # 相减得到差值
    diff = int1 - int2
    # 将差值转回 hex 字符串，并添加 "0x" 前缀
    result_hex = "0x" + hex(diff)[2:].upper()
    return result_hex


def add_hex_addresses(hex1: str, hex2: str) -> str:
    # 移除输入字符串中的所有空格和 "0x" 前缀
    cleaned_hex1 = hex1.replace(" ", "").replace("0x", "")
    cleaned_hex2 = hex2.replace(" ", "").replace("0x", "")
    # 将 hex 字符串转换为整数
    int1 = int(cleaned_hex1, 16)
    int2 = int(cleaned_hex2, 16)
    # 相加得到和值
    sum_value = int1 + int2
    # 将和值转回 hex 字符串，并添加 "0x" 前缀
    result_hex = "0x" + hex(sum_value)[2:].upper()
    return result_hex

def remove_newlines(input_text: str) -> str:
    # 使用 replace 方法去除所有的回车和换行符
    cleaned_text = input_text.replace("\n", "").replace("\r", "")
    return cleaned_text


def string_to_ascii(input_str: str) -> str:
    # 使用 ord() 函数获取每个字符的 ASCII 码，并用 \t 分隔
    ascii_values = ' '.join(str(ord(char)) for char in input_str)
    return ascii_values


def string_to_hex_with_space(s):
    hex_string = binascii.hexlify(s.encode()).decode()
    hex_string_with_space = ' '.join([hex_string[i:i+2] for i in range(0, len(hex_string), 2)])
    return hex_string_with_space


# 高位地址转换
ida_hex = "69 00 E7 EE"
reversed_hex = reverse_hex(ida_hex)
print(f"[+] \"{ida_hex}\"反转后(高位转换)的地址 hex ->  {reversed_hex}")


# 基础地址，每次加载，都需要设置
baseaddr = "D540C000"

# 由 base 地址和内存函数得到静态函数地址   0830 -> 0000007DF446F000
funaddr = "D545B98A "
result = subtract_hex_addresses(funaddr, baseaddr)
print(f"[+] so 内函数的静态地址(相减)是 ->  {result}")

# 由偏移和 base 地址得到内存函数地址
static_fun = "706B0"
result = add_hex_addresses(static_fun, baseaddr)
print(f"[+] 内存内动态地址(相加)的结果为  ->  {result}")

# 换行符删除
multi_line_text = """
W...redf.mathine
code....F...ro.d
roid4x.host.mac.
]...nemud.player
"""
single_line_text = remove_newlines(multi_line_text)
print(f"[+] 数据整合为一行  -> {single_line_text}")

# 字符串转为 ascii 码
asciisrtr = "tzyTyqz34Wlyo}zto:nzy"
ascii_output = string_to_ascii(asciisrtr)
print(f"[+] 字符串对应的 ASCII 码是  -> {ascii_output}")

# 字符串转为 hex 十六进制码
input_string = "reason"
hex_string_with_space = string_to_hex_with_space(input_string)
print(f"[+] 原始字符串 -> {input_string}")
print(f"[+] 转换后并添加空格的十六进制字符串 -> {hex_string_with_space}")
