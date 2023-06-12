

# 参考

https://bbs.kanxue.com/thread-277402.htm


## 1

```
string simulator_files_check() {
    if (file_exist("/system/bin/androVM-prop")) {//检测androidVM
        return "/system/bin/androVM-prop";
    } else if (file_exist("/system/bin/microvirt-prop")) {//检测逍遥模拟器--新版本找不到特征
        return "/system/bin/microvirt-prop";
    } else if (file_exist("/system/lib/libdroid4x.so")) {//检测海马模拟器
        return "/system/lib/libdroid4x.so";
    } else if (file_exist("/system/bin/windroyed")) {//检测文卓爷模拟器
        return "/system/bin/windroyed";
    } else if (file_exist("/system/bin/nox-prop")) {//检测夜神模拟器--某些版本找不到特征
        return "/system/bin/nox-prop";
    } else if (file_exist("system/lib/libnoxspeedup.so")) {//检测夜神模拟器
        return "system/lib/libnoxspeedup.so";
    } else if (file_exist("/system/bin/ttVM-prop")) {//检测天天模拟器
        return "/system/bin/ttVM-prop";
    } else if (file_exist("/data/.bluestacks.prop")) {//检测bluestacks模拟器  51模拟器
        return "/data/.bluestacks.prop";
    } else if (file_exist("/system/bin/duosconfig")) {//检测AMIDuOS模拟器
        return "/system/bin/duosconfig";
    } else if (file_exist("/system/etc/xxzs_prop.sh")) {//检测星星模拟器
        return "/system/etc/xxzs_prop.sh";
    } else if (file_exist("/system/etc/mumu-configs/device-prop-configs/mumu.config")) {//网易MuMu模拟器
        return "/system/etc/mumu-configs/device-prop-configs/mumu.config";
    } else if (file_exist("/system/priv-app/ldAppStore")) {//雷电模拟器
        return "/system/priv-app/ldAppStore";
    } else if (file_exist("system/bin/ldinit") && file_exist("system/bin/ldmountsf")) {//雷电模拟器
        return "system/bin/ldinit";
    } else if (file_exist("/system/app/AntStore") && file_exist("/system/app/AntLauncher")) {//小蚁模拟器
        return "/system/app/AntStore";
    } else if (file_exist("vmos.prop")) {//vmos虚拟机
        return "vmos.prop";
    } else if (file_exist("fstab.titan") && file_exist("init.titan.rc")) {//光速虚拟机
        return "fstab.titan";
    } else if (file_exist("x8.prop")) {//x8沙箱和51虚拟机
        return "x8.prop";
    } else if (file_exist("/system/lib/libc_malloc_debug_qemu.so")) {//AVD QEMU
        return "/system/lib/libc_malloc_debug_qemu.so";
    }
    LOGD("simulator file check info not find  ");
    return "";
}
```

## 2


```
public static ListItemBean checkEmulator(Context context) {
        ArrayList<String> choose = new ArrayList<>();
//        try {
//            String[] strArr = {
//                    "/boot/bstmods/vboxguest.ko",
//                    "/boot/bstmods/vboxsf.ko",
//                    "/dev/mtp_usb",
//                    "/dev/qemu_pipe",
//                    "/dev/socket/baseband_genyd",
//                    "/dev/socket/genyd",
//                    "/dev/socket/qemud",
//                    "/dev/socket/windroyed-audio",
//                    "/dev/socket/windroyed-camera",
//                    "/dev/socket/windroyed-gps",
//                    "/dev/socket/windroyed-sensors",
//                    "/dev/vboxguest",
//                    "/dev/vboxpci",
//                    "/dev/vboxuser",
//                    "/fstab.goldfish",
//                    "/fstab.nox",
//                    "/fstab.ranchu-encrypt",
//                    "/fstab.ranchu-noencrypt",
//                    "/fstab.ttVM_x86",
//                    "/fstab.vbox86",
//                    "/init.goldfish.rc",
//                    "/init.magisk.rc",
//                    "/init.nox.rc",
//                    "/init.ranchu-encrypt.rc",
//                    "/init.ranchu-noencrypt.rc",
//                    "/init.ranchu.rc",
//                    "/init.ttVM_x86.rc",
//                    "/init.vbox86.rc",
//                    "/init.vbox86p.rc",
//                    "/init.windroye.rc",
//                    "/init.windroye.sh",
//                    "/init.x86.rc",
//                    "/proc/irq/20/vboxguest",
//                    "/sdcard/Android/data/com.redfinger.gamemanage",
//                    "/stab.andy",
//                    "/sys/bus/pci/drivers/vboxguest",
//                    "/sys/bus/pci/drivers/vboxpci",
//                    "/sys/bus/platform/drivers/qemu_pipe",
//                    "/sys/bus/platform/drivers/qemu_pipe/qemu_pipe",
//                    "/sys/bus/platform/drivers/qemu_trace",
//                    "/sys/bus/virtio/drivers/itolsvmlgtp",
//                    "/sys/bus/virtio/drivers/itoolsvmhft",
//                    "/sys/class/bdi/vboxsf-1",
//                    "/sys/class/bdi/vboxsf-2",
//                    "/sys/class/bdi/vboxsf-3",
//                    "/sys/class/misc/qemu_pipe",
//                    "/sys/class/misc/vboxguest",
//                    "/sys/class/misc/vboxuser",
//                    "/sys/devices/platform/qemu_pipe",
//                    "/sys/devices/virtual/bdi/vboxsf-1",
//                    "/sys/devices/virtual/bdi/vboxsf-2",
//                    "/sys/devices/virtual/bdi/vboxsf-3",
//                    "/sys/devices/virtual/misc/qemu_pipe",
//                    "/sys/devices/virtual/misc/vboxguest",
//                    "/sys/devices/virtual/misc/vboxpci",
//                    "/sys/devices/virtual/misc/vboxuser",
//                    "/sys/fs/selinux/booleans/in_qemu",
//                    "/sys/kernel/debug/bdi/vboxsf-1",
//                    "/sys/kernel/debug/bdi/vboxsf-2",
//                    "/sys/kernel/debug/x86",
//                    "/sys/module/qemu_trace_sysfs",
//                    "/sys/module/vboxguest",
//                    "/sys/module/vboxguest/drivers/pci:vboxguest",
//                    "/sys/module/vboxpcism",
//                    "/sys/module/vboxsf",
//                    "/sys/module/vboxvideo",
//                    "/sys/module/virtio_pt/drivers/virtio:itoolsvmhft",
//                    "/sys/module/virtio_pt_ie/drivers/virtio:itoolsvmlgtp",
//                    "/sys/qemu_trace",
//                    "/system/app/GenymotionLayout",
//                    "/system/bin/OpenglService",
//                    "/system/bin/androVM-vbox-sf",
//                    "/system/bin/droid4x",
//                    "/system/bin/droid4x-prop",
//                    "/system/bin/droid4x-vbox-sf",
//                    "/system/bin/droid4x_setprop",
//                    "/system/bin/enable_nox",
//                    "/system/bin/genymotion-vbox-sf",
//                    "/system/bin/microvirt-prop",
//                    "/system/bin/microvirt-vbox-sf",
//                    "/system/bin/microvirt_setprop",
//                    "/system/bin/microvirtd",
//                    "/system/bin/mount.vboxsf",
//                    "/system/bin/nox",
//                    "/system/bin/nox-prop",
//                    "/system/bin/nox-vbox-sf",
//                    "/system/bin/nox_setprop",
//                    "/system/bin/noxd",
//                    "/system/bin/noxscreen",
//                    "/system/bin/noxspeedup",
//                    "/system/bin/qemu-props",
//                    "/system/bin/qemud",
//                    "/system/bin/shellnox",
//                    "/system/bin/ttVM-prop",
//                    "/system/bin/windroyed",
//                    "/system/droid4x",
//                    "/system/etc/init.droid4x.sh",
//                    "/system/etc/init.tiantian.sh",
//                    "/system/lib/egl/libEGL_emulation.so",
//                    "/system/lib/egl/libEGL_tiantianVM.so",
//                    "/system/lib/egl/libEGL_windroye.so",
//                    "/system/lib/egl/libGLESv1_CM_emulation.so",
//                    "/system/lib/egl/libGLESv1_CM_tiantianVM.so",
//                    "/system/lib/egl/libGLESv1_CM_windroye.so",
//                    "/system/lib/egl/libGLESv2_emulation.so",
//                    "/system/lib/egl/libGLESv2_tiantianVM.so",
//                    "/system/lib/egl/libGLESv2_windroye.so",
//                    "/system/lib/hw/audio.primary.vbox86.so",
//                    "/system/lib/hw/audio.primary.windroye.so",
//                    "/system/lib/hw/audio.primary.x86.so",
//                    "/system/lib/hw/autio.primary.nox.so",
//                    "/system/lib/hw/camera.vbox86.so",
//                    "/system/lib/hw/camera.windroye.jpeg.so",
//                    "/system/lib/hw/camera.windroye.so",
//                    "/system/lib/hw/camera.x86.so",
//                    "/system/lib/hw/gps.nox.so",
//                    "/system/lib/hw/gps.vbox86.so",
//                    "/system/lib/hw/gps.windroye.so",
//                    "/system/lib/hw/gralloc.nox.so",
//                    "/system/lib/hw/gralloc.vbox86.so",
//                    "/system/lib/hw/gralloc.windroye.so",
//                    "/system/lib/hw/sensors.nox.so",
//                    "/system/lib/hw/sensors.vbox86.so",
//                    "/system/lib/hw/sensors.windroye.so",
//                    "/system/lib/init.nox.sh",
//                    "/system/lib/libGM_OpenglSystemCommon.so",
//                    "/system/lib/libc_malloc_debug_qemu.so",
//                    "/system/lib/libclcore_x86.bc",
//                    "/system/lib/libdroid4x.so",
//                    "/system/lib/libnoxd.so",
//                    "/system/lib/libnoxspeedup.so",
//                    "/system/lib/modules/3.10.30-android-x86.hd+",
//                    "/system/lib/vboxguest.ko",
//                    "/system/lib/vboxpcism.ko",
//                    "/system/lib/vboxsf.ko",
//                    "/system/lib/vboxvideo.ko",
//                    "/system/lib64/egl/libEGL_emulation.so",
//                    "/system/lib64/egl/libGLESv1_CM_emulation.so",
//                    "/system/lib64/egl/libGLESv2_emulation.so",
//                    "/vendor/lib64/egl/libEGL_emulation.so",
//                    "/vendor/lib64/egl/libGLESv1_CM_emulation.so",
//                    "/vendor/lib64/egl/libGLESv2_emulation.so",
//                    "/vendor/lib64/libandroidemu.so",
//                    "/system/lib64/hw/gralloc.ranchu.so",
//                    "/system/lib64/libc_malloc_debug_qemu.so",
//                    "/system/usr/Keylayout/droid4x_Virtual_Input.kl",
//                    "/system/usr/idc/Genymotion_Virtual_Input.idc",
//                    "/system/usr/idc/droid4x_Virtual_Input.idc",
//                    "/system/usr/idc/nox_Virtual_Input.idc",
//                    "/system/usr/idc/windroye.idc",
//                    "/system/usr/keychars/nox_gpio.kcm",
//                    "/system/usr/keychars/windroye.kcm",
//                    "/system/usr/keylayout/Genymotion_Virtual_Input.kl",
//                    "/system/usr/keylayout/nox_Virtual_Input.kl",
//                    "/system/usr/keylayout/nox_gpio.kl",
//                    "/system/usr/keylayout/windroye.kl",
//                    "system/etc/init/ndk_translation_arm64.rc",
//                    "/system/xbin/noxsu",
//                    "/ueventd.android_x86.rc",
//                    "/ueventd.andy.rc",
//                    "/ueventd.goldfish.rc",
//                    "/ueventd.nox.rc",
//                    "/ueventd.ranchu.rc",
//                    "/ueventd.ttVM_x86.rc",
//                    "/ueventd.vbox86.rc",
//                    "/vendor/lib64/libgoldfish-ril.so",
//                    "/vendor/lib64/libgoldfish_codecs_common.so",
//                    "/vendor/lib64/libstagefright_goldfish_avcdec.so",
//                    "/vendor/lib64/libstagefright_goldfish_vpxdec.so",
//                    "/x86.prop"
//            };
//            for (int i = 0; i < 7; i++) {
//                String f = strArr[i];
//                if (new File(f).exists())
//                    choose.add(f);
//            }
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
 
        try {
            String[] myArr = {
                    "generic",
                    "vbox"
            };
            for (String str : myArr) {
                if (Build.FINGERPRINT.contains(str))
                    choose.add(Build.FINGERPRINT);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
 
        try {
            String[] myArr = {
                    "google_sdk",
                    "emulator",
                    "android sdk built for",
                    "droid4x"
            };
            for (String str : myArr) {
                if (Build.MODEL.contains(str))
                    choose.add(Build.MODEL);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
 
        try {
            String[] myArr = {
                    "Genymotion"
            };
            for (String str : myArr) {
                if (Build.MANUFACTURER.contains(str))
                    choose.add(Build.MANUFACTURER);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
 
        try {
            String[] myArr = {
                    "google_sdk", "sdk_phone", "sdk_x86", "vbox86p", "nox"
            };
            for (String str : myArr) {
                if (Build.PRODUCT.toLowerCase(Locale.ROOT).contains(str))
                    choose.add(Build.PRODUCT);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
 
        try {
            String[] myArr = {
                    "nox"
            };
            for (String str : myArr) {
                if (Build.BOARD.toLowerCase(Locale.ROOT).contains(str))
                    choose.add(Build.BOARD);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
 
        try {
            String[] myArr = {
                    "nox"
            };
            for (String str : myArr) {
                if (Build.BOOTLOADER.toLowerCase(Locale.ROOT).contains(str))
                    choose.add(Build.BOOTLOADER);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
 
        try {
            String[] myArr = {
                    "ranchu", "vbox86", "goldfish"
            };
            for (String str : myArr) {
                if (Build.HARDWARE.equalsIgnoreCase(str))
                    choose.add(Build.HARDWARE);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
 
        try {
            Enumeration<NetworkInterface> networkInterfaces = NetworkInterface.getNetworkInterfaces();
            while (networkInterfaces.hasMoreElements()) {
                NetworkInterface ele = networkInterfaces.nextElement();
                if (ele != null) {
                    Enumeration<InetAddress> inetAddresses = ele.getInetAddresses();
                    while (inetAddresses.hasMoreElements()) {
                        InetAddress nextElement = inetAddresses.nextElement();
                        if (!nextElement.isLoopbackAddress() &&
                                (nextElement instanceof Inet4Address)) {
                            String ip = nextElement.getHostAddress();
                            if (ip == null) continue;
                            if (ip.equalsIgnoreCase("10.0.2.15") ||
                                    ip.equalsIgnoreCase("10.0.2.16")) {
                                choose.add(ip);
                            }
                        }
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
 
//        try {
//            String[] qemuProps = {
//                    "ro.kernel.qemu.avd_name",
//                    "ro.kernel.qemu.gles",
//                    "ro.kernel.qemu.gltransport",
//                    "ro.kernel.qemu.opengles.version",
//                    "ro.kernel.qemu.uirenderer",
//                    "ro.kernel.qemu.vsync",
//                    "ro.qemu.initrc",
//                    "init.svc.qemu-props",
//                    "qemu.adb.secure",
//                    "qemu.cmdline",
//                    "qemu.hw.mainkeys",
//                    "qemu.logcat",
//                    "ro.adb.qemud",
//                    "qemu.sf.fake_camera",
//                    "qemu.sf.lcd_density",
//                    "qemu.timezone",
//                    "init.svc.goldfish-logcat",
//                    "ro.boottime.goldfish-logcat",
//                    "ro.hardware.audio.primary",
//                    "init.svc.ranchu-net",
//                    "init.svc.ranchu-setup",
//                    "ro.boottime.ranchu-net",
//                    "ro.boottime.ranchu-setup",
//                    "init.svc.droid4x",
//                    "init.svc.noxd",
//                    "init.svc.qemud",
//                    "init.svc.goldfish-setup",
//                    "init.svc.goldfish-logcat",
//                    "init.svc.ttVM_x86-setup",
//                    "vmos.browser.home",
//                    "vmos.camera.enable",
//                    "ro.trd_yehuo_searchbox",
//                    "init.svc.microvirtd",
//                    "init.svc.vbox86-setup",
//                    "ro.ndk_translation.version",
//                    "redroid.width",
//                    "redroid.height",
//                    "redroid.fps",
//                    "ro.rf.vmname"
//            };
//
//            for (String str : qemuProps) {
//                String val = SystemPropertiesUtils.getProperty(str, null);
//                if (val != null) {
//                    choose.add(str);
//                }
//            }
//        } catch (Throwable e) {
//            e.printStackTrace();
//        }
        //判断是否存在指定硬件
        PackageManager pm = null;
        try {
            pm = context.getPackageManager();
            String[] features = {
                    //PackageManager.FEATURE_RAM_NORMAL,//这个存在问题,自己组装的手机可能导致这个痕迹找不到
                    PackageManager.FEATURE_BLUETOOTH,
                    PackageManager.FEATURE_CAMERA_FLASH,
                    PackageManager.FEATURE_TELEPHONY
            };
            for (String feature : features) {
                if (!pm.hasSystemFeature(feature)) {
                    choose.add(feature);
                }
            }
        } catch (Throwable ignored) {
    }
 
    try {
        String[] emuPkgs = {
                "com.google.android.launcher.layouts.genymotion",
                "com.bluestacks",
                "com.bignox.app"
        };
 
        for (String pkg : emuPkgs) {
            try {
                if (pm != null) {
                    pm.getPackageInfo(pkg, 0);
                }
                choose.add(pkg);
            } catch (Throwable e) {
                //e.printStackTrace();
            }
        }
    } catch (Throwable ignored) {
 
    }
 
    try {
        SensorManager sensor = (SensorManager) context.getSystemService(Context.SENSOR_SERVICE);
        int sensorSize = sensor.getSensorList(Sensor.TYPE_ALL).size();
        for (int i = 0; i < sensorSize; i++) {
            Sensor s = sensor.getDefaultSensor(i);
            if (s != null && s.getName().contains("Goldfish")) {
                choose.add(s.getName());
            }
        }
    } catch (Throwable ignored) {
 
    }
 
    try {
        if (checkSelfPermission(context, "android.permission.READ_SMS") == 0 ||
                checkSelfPermission(context, "android.permission.READ_PHONE_NUMBERS") == 0 ||
                    checkSelfPermission(context, "android.permission.READ_PHONE_STATE") == 0) {
            TelephonyManager telephonyManager = (TelephonyManager) context.getSystemService(Context.TELEPHONY_SERVICE);
            String phoneNumber = telephonyManager.getLine1Number();
 
            String[] phoneNumbers = {
                    "15555215554",
                    "15555215556",
                    "15555215558",
                    "15555215560",
                    "15555215562",
                    "15555215564",
                    "15555215566",
                    "15555215568",
                    "15555215570",
                    "15555215572",
                    "15555215574",
                    "15555215576",
                    "15555215578",
                    "15555215580",
                    "15555215582",
                    "15555215584"
            };
            if(phoneNumber!=null) {
                for (String phone : phoneNumbers) {
                    if (phoneNumber.equalsIgnoreCase(phone)) {
                        choose.add(phone);
                        break;
                    }
                }
            }
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
 
    if (choose.size() > 0) {
        ListItemBean item = new ListItemBean("检测到APK运行在虚拟机&模拟器中",
                ListItemBean.RiskLeave.Deadly,
                choose.toString()
        );
        for (String str : choose) {
            item.putData(str);
        }
        return item;
    }
    return null;
}
```


## 3

```
public PropArea(String area) throws IOException {
        area = "/dev/__properties__/u:object_r:" + area + ":s0";
        File file = new File(area);
        if (!file.isFile()) throw new FileNotFoundException("Not a file: " + area);
        long size = file.length();
        if (size <= 0 || size >= 0x7fffffffL) throw new IllegalArgumentException("invalid file size " + size);
 
        try (FileChannel channel = new FileInputStream(area).getChannel()) {
            data = channel.map(FileChannel.MapMode.READ_ONLY, 0, size).order(ByteOrder.nativeOrder());
        }
 
        byteUsed = data.getInt();
        data.getInt(); // serial
        int magic = data.getInt();
        if (magic != PROP_AREA_MAGIC) throw new IllegalArgumentException("Bad file magic: " + magic);
        int version = data.getInt();
        if (version != PROP_AREA_VERSION) throw new IllegalArgumentException("Bad area versin: " + version);
        data.position(data.position() + 28); // reserved
    }
 
public List<String> findPossibleValues(String name) {
    List<String> values ;
    try {
        //  atomic_uint_least32_t serial;
        //  union {
        //    char value[PROP_VALUE_MAX];
        //    struct {
        //      char error_message[kLongLegacyErrorBufferSize];
        //      uint32_t offset;
        //    } long_property;
        //  };
        final int LONG_PROP_FLAG = 1 << 16;
        final int PROP_VALUE_MAX = 92;
        final int VALUE_OFFSET = 4;
        final int NAME_OFFSET = VALUE_OFFSET + 92;
        values = new ArrayList<>(2);
        findFromBuffer(data.slice(), name.getBytes(StandardCharsets.UTF_8), (buffer, offset) -> {
            if (offset < NAME_OFFSET) return;
            int base = offset - NAME_OFFSET;
            int serial = buffer.getInt(base);
            if ((serial & LONG_PROP_FLAG) != 0) return; // Long properties are not supported
            values.add(toString(buffer, base + VALUE_OFFSET, PROP_VALUE_MAX));
        });
        CLog.i("Found " + name + "=" + values);
        return values;
    } catch (Throwable e) {
        CLog.e("findPossibleValues get error "+ name+" "+e);
        return null;
    }
}
```










