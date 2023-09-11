import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

# 一个应用的 类 内所有方法的调用
jscode = """
Java.perform(function () {

    var ContextClass = Java.use('android.content.Context');
    var methods3 = ContextClass.class.getDeclaredMethods();
    methods3.forEach(function(method) {
        var methodName = method.getName();
        method.setAccessible(true);
        
        try {
            var overloadz = ContextClass[methodName].overloads;
        } catch (e) {
            console.error('Cannot find overloads for: ' + methodName);
            return;
        }

        overloadz.forEach(function(overload) {
            try {
                overload.implementation = function() {
                    console.log('Context Called: ' + methodName + '(' + overload.argumentTypes.join(', ') + ')');
                    return overload.apply(this, arguments);
                };
            } catch (e) {
                console.error('Failed to hook: ' + methodName);
            }
        });
    });
    
});
"""

def get_pid(package_name):
    device = frida.get_usb_device()
    processes = device.enumerate_processes()
    for process in processes:
        #print("process -> " + process.name)
        if process.name == package_name:
            return process.pid
    return None

tag = 0
pid = get_pid('浏览器')
if pid is None:
    pid = get_pid('com.android.browser')

print("pid0 -> " + str(pid))
device = frida.get_usb_device()
if pid is None:
    print("spawn innn ")
    tag = 1
    pid = device.spawn(["com.android.browser"])
print("pid1 -> " + str(pid))

process = device.attach(pid)
print("attach 1")
script = process.create_script(jscode)
print("attach 2")
script.on('message', on_message)
script.load()
if tag == 1:
    device.resume(pid)
#device.resume(pid)
sys.stdin.read()
print("attach 3")


