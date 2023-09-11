



# 1. 获取目标进程的 pid 


def get_pid(package_name):
    device = frida.get_usb_device()
    processes = device.enumerate_processes()
    for process in processes:
        print("process -> " + process.name)
        if process.name == package_name:
            return process.pid
    return None


pid = get_pid('com.cc')
if pid is None:
    pid = get_pid('nnnn')


print("pid1 -> " + str(pid))
device = frida.get_usb_device()
print("pid -> " + str(pid))
process = device.attach(pid)
script = process.create_script(jscode)
script.on('message', on_message)
script.load()
sys.stdin.read()

# 2. 最早时机进行注入

device = frida.get_usb_device()
pid = device.spawn(["com.qqq"])
print("pid -> " + str(pid))
process = device.attach(pid)
script = process.create_script(jscode)
script.on('message', on_message)
script.load()
device.resume(pid)
sys.stdin.read()


# 3. hook 多参数方法

Java.perform(function () {
    var oClass = Java.use('com.c');
    var resultClass = Java.use('com.n');

    oClass.a.overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'boolean', 'boolean', 'boolean').implementation = function (str1, str2, str3, str4, z1, z2, z3) {
        
        send("Hook ooo in ");
        // 输出原始参数
        console.log('Original Args: ', str1, str2, str3, str4, z1, z2, z3);
        
        // 调用原函数逻辑
        var original_result = this.a(str1, str2, str3, str4, z1, z2, z3);
        
        // 输出原始函数返回结果
        console.log('Original result: ', original_result);
        
        // 返回原结果，确保不影响原代码逻辑
        return original_result;
    };
});

.
    var urlutil = Java.use('com.URLUtil');
    urlutil.ahp.overload('java.lang.String').implementation = function (args) {
        send("Hook ahp");
        //showStacks();
        send(args[0]);
        
        var ret = urlutil.ahp.overload('java.lang.String').call(this, args);
        send("Hook ahp: " + ret);
        return ret;
    }
.

# 4. 





