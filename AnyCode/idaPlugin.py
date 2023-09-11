

```

# 打印当前断点的函数地址

# filename: get_breakpoint_func_address.py
import idaapi
import idc

def get_breakpoint_func_address():
    ea = idc.get_screen_ea()  # 获取当前光标所在的地址
    func = idaapi.get_func(ea)  # 获取该地址对应的函数对象
    if func:
        print("Current breakpoint is inside the function at address: 0x{:X}".format(func.start_ea))
    else:
        print("No function found for current breakpoint address.")

# 执行函数
get_breakpoint_func_address()


```

# hook 断点，并打印函数的参数

import idc
import idaapi
import idautils

# 目标函数地址
target_function_addr = 0x7DF44DEEB0

# 断点处理函数
class MyDbgHook(idaapi.DBG_Hooks):
    def dbg_bpt(self, tid, ea):
        # 获取第二个参数的值
        # 在ARM64架构下，第二个参数通常在x1寄存器
        second_arg_ptr = idc.get_reg_value("X1")

        # 读取字符串内容
        str_content = idc.get_strlit_contents(second_arg_ptr)
        if str_content is not None:
            print(f"Breakpoint at {hex(ea)}, second argument is string: {str_content.decode()}")
        #else:
            #print(f"Breakpoint at {hex(ea)}, second argument pointer is: {hex(second_arg_ptr)} but could not fetch string")

        # 让程序继续执行
        return 0

# 注册断点处理函数
debugger = MyDbgHook()
debugger.hook()

# 在目标函数地址设置断点
idc.add_bpt(target_function_addr)

print(f"Set breakpoint at target function {hex(target_function_addr)}")

```

# hook 函数并打印函数的参数

import idaapi
import idc
import idautils

# 目标函数地址
target_function_addr = 0x7DF44DEEB0

# 断点处理函数
class MyDbgHook(idaapi.DBG_Hooks):
    def dbg_bpt(self, tid, ea):
        if ea == target_function_addr:
            # 获取 X1 寄存器的值，即第二个参数的地址
            second_arg_ptr = idc.get_reg_value("X1")

            # 读取内存，尝试获取一个长度为 100 的字节串
            memory_content = idaapi.dbg_read_memory(second_arg_ptr, 100)
            if memory_content:
                try:
                    # 找到字符串的结尾（null 字符）
                    null_pos = memory_content.index(b'\0')
                    # 解码字符串
                    str_content = memory_content[:null_pos].decode('utf-8')
                    print(f"Breakpoint at {hex(ea)}, second argument is string: {str_content}")
                except ValueError:
                    # 如果找不到 null 字符，直接输出原始的字节串
                    print(f"Breakpoint at {hex(ea)}, second argument is raw bytes: {memory_content}")
            else:
                print(f"Breakpoint at {hex(ea)}, but couldn't read memory at X1: {hex(second_arg_ptr)}")
                
        return 0

# 注册断点处理函数
debugger = MyDbgHook()
debugger.hook()

# 在目标函数地址设置断点
bpt1 = idaapi.bpt_t()
bpt1.ea = target_function_addr
idaapi.add_bpt(bpt1)

```

# 根据地址区间，内存 dump :

import idc

# 起始和结束地址
start_addr = 0x7D9585BBB0  # 请用你的实际地址替换
end_addr = 0x7D9585C770    # 请用你的实际地址替换

# 计算需要读取的内存大小
size = end_addr - start_addr

# 读取内存内容
memory_data = idc.get_bytes(start_addr, size)

if memory_data is not None:
    # 导出到文件
    with open('C:\\Users\\Think\\Desktop\\a.bin', 'wb') as f:
        f.write(memory_data)
    print(f"Successfully exported memory from {hex(start_addr)} to {hex(end_addr)} to exported_memory.bin")
else:
    print(f"Failed to read memory from {hex(start_addr)} to {hex(end_addr)}")


```

# 批量打断点，一键打断点

import idaapi
import idc

def set_breakpoints(base_address, offsets):
    for offset in offsets:
        absolute_address = base_address + offset
        idc.add_bpt(absolute_address)
        print("Breakpoint set at 0x{:X}".format(absolute_address))

base_address = 0x7DF4449000
function_offsets = [0x7F6B8, 0x16B1F4, 0x802A4, 0xAA7A0, 0x9F000, 0xA5178, 0x41A04]

set_breakpoints(base_address, function_offsets)

```

# 同时 hook 多个函数并打印参数

import idaapi
import idc
import idautils

# 目标函数地址
target_function_addr = 0x7DF45B4130
target_function_addr2 = 0x7DF44C92A4

# 断点处理函数
class MyDbgHook(idaapi.DBG_Hooks):
    def dbg_bpt(self, tid, ea):
        if ea == target_function_addr2:
            # 获取 X1 寄存器的值，即第二个参数的地址
            second_arg_ptr = idc.get_reg_value("X1")

            # 读取内存，尝试获取一个长度为 100 的字节串
            memory_content = idaapi.dbg_read_memory(second_arg_ptr, 100)
            if memory_content:
                try:
                    # 找到字符串的结尾（null 字符）
                    null_pos = memory_content.index(b'\0')
                    # 解码字符串
                    str_content = memory_content[:null_pos].decode('utf-8')
                    print(f"Breakpoint at {hex(ea)}, second argument is string: {str_content}")
                except ValueError:
                    # 如果找不到 null 字符，直接输出原始的字节串
                    print(f"Breakpoint at {hex(ea)}, second argument is raw bytes: {memory_content}")
            else:
                print(f"Breakpoint at {hex(ea)}, but couldn't read memory at X1: {hex(second_arg_ptr)}")
        if ea == target_function_addr:
            # 获取 X1 寄存器的值，即第二个参数的地址
            second_arg_ptr = idc.get_reg_value("X1")

            # 读取内存，尝试获取一个长度为 100 的字节串
            memory_content = idaapi.dbg_read_memory(second_arg_ptr, 100)
            if memory_content:
                try:
                    # 找到字符串的结尾（null 字符）
                    null_pos = memory_content.index(b'\0')
                    # 解码字符串
                    str_content = memory_content[:null_pos].decode('utf-8')
                    print(f"Breakpoint at {hex(ea)}, second argument is string: {str_content}")
                except ValueError:
                    # 如果找不到 null 字符，直接输出原始的字节串
                    print(f"Breakpoint at {hex(ea)}, second argument is raw bytes: {memory_content}")
            else:
                print(f"Breakpoint at {hex(ea)}, but couldn't read memory at X1: {hex(second_arg_ptr)}")
                
        return 0

# 注册断点处理函数
debugger = MyDbgHook()
debugger.hook()


```

# 寻找当前函数中第一个出现的RET指令的地址

from idaapi import *
from idc import *

# 获取当前的函数地址
current_func = get_func(get_screen_ea())

if current_func:
    start = current_func.start_ea
    end = current_func.end_ea
    
    # 从函数开始地址到结束地址遍历
    ea = start
    while ea < end:
        # 获取当前地址的反汇编指令
        disasm = GetDisasm(ea)
        
        # 检查是否是RET指令
        if "RET" in disasm:
            print(f"Found RET at address: {hex(ea)}")
            break
        
        # 移到下一条指令
        ea = next_head(ea, end)
else:
    print("No function found at current address.")

```

# 打印内存地址，这个还需要优化

import idautils
import idc

def get_memory_info():
    memory_segments = []
    for seg_ea in idautils.Segments():
        seg_info = {
            'start': hex(idc.get_segm_start(seg_ea)),
            'end': hex(idc.get_segm_end(seg_ea)),
            'name': idc.get_segm_name(seg_ea)
        }
        memory_segments.append(seg_info)

    return memory_segments

if __name__ == "__main__":
    memory_info = get_memory_info()
    for segment in memory_info:
        print(f"Segment name: {segment['name']}, Start: {segment['start']}, End: {segment['end']}")

```

# 打印出所有的注释


import idc
import idautils
import idaapi

def list_all_comments():
    comments = {}
    for seg_ea in idautils.Segments():
        seg_end = idc.get_segm_end(seg_ea)  # 使用 get_segm_end 替代 SegEnd
        for head in idautils.Heads(seg_ea, seg_end):
            cmt = idc.GetCommentEx(head, 0)  # 获取行注释
            rpt_cmt = idc.GetCommentEx(head, 1)  # 获取重复行注释
            if cmt:
                comments[head] = {'normal': cmt}
            if rpt_cmt:
                if head not in comments:
                    comments[head] = {}
                comments[head]['repeat'] = rpt_cmt
                
    return comments

if __name__ == '__main__':
    comments = list_all_comments()
    for ea, cmts in comments.items():
        print(f"Address: {hex(ea)}")
        if 'normal' in cmts:
            print(f"  Normal Comment: {cmts['normal']}")
        if 'repeat' in cmts:
            print(f"  Repeat Comment: {cmts['repeat']}")


```

# 查找内存中是否已经出现固定的字符串，这个需要优化

import idaapi
import idc
import idautils

def immediate_search():
    idaapi.msg("Immediate String Search Started\n")
    
    code = "aaaaa"

    # 将16进制字符串转换为ASCII码字符串
    search_string = ' '.join(["%02X" % b for b in bytes.fromhex(code)])

    for seg_ea in idautils.Segments():
        seg_start = idc.get_segm_start(seg_ea)
        seg_end = idc.get_segm_end(seg_ea)
        idaapi.msg("Scanning %s - %s...\n" % (hex(seg_start), hex(seg_end)))

        ea = seg_start
        while ea < seg_end:
            found_ea = idc.find_binary(ea, seg_end, search_string, 16, idc.SEARCH_DOWN)
            if found_ea == idaapi.BADADDR:
                break
            idaapi.msg("String found at: %s\n" % hex(found_ea))
            ea = found_ea + len(bytes.fromhex(code))

immediate_search()

```

# 根据地址区间，查找字符串；内存字符串的查找；
# 查找目标字符串是否已经出现；
# 需要先将目标字符串转为 hex 码

try:
    import idaapi
    import ida_search

    def immediate_search():
        idaapi.msg("Immediate Address-Specific String Search Started\n")
        
        # 将16进制字符串转换为以空格分隔的形式
        search_string = "66 37 30 35 39 65 32 38 36 38 35 36 37 37 33"
        
        # 指定起始和结束地址
        start_address = 0xEB000000
        end_address = 0xEFF00000


        idaapi.msg("Scanning from {} to {}\n".format(hex(start_address), hex(end_address)))

        ea = start_address
        while ea < end_address:
            # 使用 ida_search.find_binary 替代 idc.find_binary
            found_ea = ida_search.find_binary(ea, end_address, search_string, 0, idaapi.SEARCH_DOWN)
            if found_ea == idaapi.BADADDR:
                break
            idaapi.msg("String found at: {}\n".format(hex(found_ea)))
            ea = found_ea + len(search_string.split(" ")) # 更新偏移地址

    immediate_search()

except Exception as e:
    idaapi.msg("An error occurred: {}\n".format(str(e)))


```

# 一个确定的起始结束地址内找打最早出现二进制数据的地址

import idaapi
import ida_search

def find_first_occurrence(start_address, end_address):
    search_string = "FF 03 16 D1"
    
    idaapi.msg("Searching for bytes {} between {} and {}\n".format(
        search_string,
        hex(start_address),
        hex(end_address))
    )

    # 使用 ida_search.find_binary 函数查找字节码
    found_ea = ida_search.find_binary(start_address, end_address, search_string, 0, idaapi.SEARCH_DOWN)
    
    if found_ea != idaapi.BADADDR:
        idaapi.msg("Bytes found at address: {}\n".format(hex(found_ea)))
    else:
        idaapi.msg("Bytes not found in the specified range.\n")

# 示例用法
start_address = 0x1000  # 请替换为实际的起始地址
end_address = 0x2000  # 请替换为实际的结束地址

find_first_occurrence(start_address, end_address)


```
