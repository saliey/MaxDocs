

# ollvm 14.x windows 端

参考：

https://github.com/heroims/obfuscator
https://github.com/buffcow/ollvm-project/tree/14.x
https://blog.csdn.net/qq_41923691/article/details/123258565
https://www.erlo.vip/share/9/98883.html
https://github.com/llvm/llvm-project
https://github.com/0x3f97/ollvm-12.x


## 1 步骤

1. 将 [ollvm](https://github.com/buffcow/ollvm-project/tree/14.x) 拉下来。 14.x 版本适用 [bdk-build-r25](https://github.com/android/ndk/wiki/Unsupported-Downloads) 版本。
2. 然后在 windows 端使用 visurl studio 打开项目的 `ollvm-project-14.x\llvm` 路径
3. 然后构建 CMakeSettings.json 配置文件，原命令为 `cmake -S llvm -B build -G Ninja -DLLVM_ENABLE_PROJECTS="clang" -DCMAKE_BUILD_TYPE=Release -DLLVM_INCLUDE_TESTS=OFF -DLLVM_ENABLE_NEW_PASS_MANAGER=OFF` ，所以 json 配置文件为 

```
{
  "configurations": [
    {
      "name": "x64-Debug",
      "generator": "Ninja",
      "configurationType": "Release",
      "inheritEnvironments": [ "msvc_x64_x64" ],
      "buildRoot": "${projectDir}\\out\\build\\${name}",
      "installRoot": "${projectDir}\\out\\install\\${name}",
      "cmakeCommandArgs": "",
      "buildCommandArgs": "",
      "ctestCommandArgs": "",
      "variables": [
        {
          "name": "LLVM_ENABLE_PROJECTS",
          "value": "clang",
          "type": "STRING"
        },
        {
          "name": "LLVM_INCLUDE_TESTS",
          "value": "OFF",
          "type": "STRING"
        },
        {
          "name": "LLVM_ENABLE_NEW_PASS_MANAGER",
          "value": "OFF",
          "type": "STRING"
        }
      ]
    }
  ]
}
```

4. 然后选择 生成->全部生成，等待编译完成就是最终的结果

## 2 选项说明

参数|说明
---|---
-mllbm|-sub|激活指令替换
-mllvm|-sub_loop=3|如果激活了传递，则在函数上应用3次。默认值：1
-mllvm|-bcf|激活虚假控制流程
-mllvm|-bcf_loop=3|如果激活了传递，则在函数上应用3次。默认值：1
-mllvm|-bcf_prob=40|如果激活了传递，基本块将以40％的概率进行模糊处理。默认值：30
-mllvm|-fla|激活控制流扁平化
-mllvm|-split|激活基本块分割。在一起使用时改善展平
-mllvm|-split_num=3|如果激活了传递，则在每个基本块上应用3次。默认值：1


heroims在移植 OLLVM 时，集成了Armariris的字符串混淆功能。

参数|说明
---|---
-mllvm|-sobf|编译时候添加选项开启字符串加密
-mllvm|-seed=|指定随机数生成器种子

经过测试：

1. `-mllvm -bcf	` 不能用，直接 crash 
所以不能用  `-mllvm -bcf_loop=3`

2. `-mllvm -split` 可以用，但 split_num 不能多，v7a 会编译失败
`-mllvm -split_num=2`

3. `-mllvm -seed=3` 也不能用，编译失败；

## 3 关于 ndk 的选项控制

因为不希望所有的 cpp 文件都被混淆，仅混淆关键函数，但这个并不能具体控制。还需要研究；

## 4 总结

1. windows 下如果配置 cmake/clang 进行编译，会出现下面的错误，改为 visurl studio 进行编译就好了。对应的 MSVC 环境。
   vsProject 仅支持有 CmakeLists.txt ，所以要选择到 llvm 的具体路径。

```
CMake Error at cmake/modules/CheckAtomic.cmake:59 (message):
  Host compiler appears to require libatomic, but cannot find it.
Call Stack (most recent call first):
  cmake/config-ix.cmake:377 (include)
  CMakeLists.txt:732 (include)
```

2. 编译完成后生成的 clang.exe clang++.exe clang-cl.exe 是同一个东西，要替换 `D:\sdk\ndk-bundle\toolchains\llvm\prebuilt\windows-x86_64\bin` 下对应 clnag.exe 。
同时要吧 `D:\sdk\ndk-bundle\toolchains\llvm\prebuilt\windows-x86_64\lib64\clang` 下的 14.x 文件夹拷贝到 `D:\sdk\ndk-bundle\toolchains\llvm\prebuilt\windows-x86_64\lib\clang` 下，同时 将 14.x 文件夹名字改为 `14.0.0`

3. Android.mk 文件

```
LOCAL_CFLAGS += -mllvm -fla \
        -mllvm -sub \
        -mllvm -sub_loop=3 \
        -mllvm -bcf_loop=3 \
        -mllvm -split_num=3 \
        -mllvm -sobf \
```

4. 后续还需要为更精细化的控制 ollvm cpp 文件更新，该怎样兼容呢？设置特定标识，然后编译混淆处进行识别，有选择的处理。

