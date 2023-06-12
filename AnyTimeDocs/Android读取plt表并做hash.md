




JNI（Java Native Interface）是一种可以让 Java 代码与 C 和 C++ 代码互相调用的接口。为了实现你需要的功能，我们需要两个步骤：首先，使用 C/C++ 来实现一个读取 so 文件 plt 表并计算 hash 的功能；然后，使用 JNI 来使得你的 Android 程序可以调用这个功能。

这是一个复杂的问题，我会尽量保持代码清晰并提供必要的注释。

首先，我们需要在 C/C++ 中创建一个文件（比如 `native-lib.cpp`）来实现这个功能：

```cpp
#include <jni.h>
#include <cstdio>
#include <cstdlib>
#include <dlfcn.h>
#include <elf.h>
#include <sys/mman.h>
#include <unistd.h>
#include <fcntl.h>
#include <openssl/sha.h>

// 辅助函数: 计算哈希
void calculate_hash(unsigned char *data, size_t len, unsigned char *hash) {
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, data, len);
    SHA256_Final(hash, &sha256);
}

extern "C" JNIEXPORT jbyteArray JNICALL
Java_com_your_package_name_MainActivity_getPltHash(JNIEnv *env, jobject) {
    void *handle;
    ElfW(Ehdr) *ehdr;
    ElfW(Phdr) *phdr;
    ElfW(Dyn) *dyn;
    ElfW(Rel) *rel, *plt_rel;
    ElfW(Sym) *sym;
    int i, j, fd;
    char *strtab;
    unsigned char hash[SHA256_DIGEST_LENGTH];
    jbyteArray ret;

    handle = dlopen(NULL, RTLD_NOW);
    ehdr = (ElfW(Ehdr) *) handle;
    phdr = (ElfW(Phdr) *)((char *)handle + ehdr->e_phoff);

    for (i = 0; i < ehdr->e_phnum; i++) {
        if (phdr[i].p_type != PT_DYNAMIC) continue;
        dyn = (ElfW(Dyn) *)((char *)handle + phdr[i].p_vaddr);
        for (j = 0; dyn[j].d_tag != DT_NULL; j++) {
            switch (dyn[j].d_tag) {
                case DT_JMPREL:
                    plt_rel = (ElfW(Rel) *)((char *)handle + dyn[j].d_un.d_ptr);
                    break;
                case DT_SYMTAB:
                    sym = (ElfW(Sym) *)((char *)handle + dyn[j].d_un.d_ptr);
                    break;
                case DT_STRTAB:
                    strtab = (char *)handle + dyn[j].d_un.d_ptr;
                    break;
            }
        }
    }

    calculate_hash((unsigned char *)plt_rel, sizeof(ElfW(Rel)), hash);

    ret = env->NewByteArray(SHA256_DIGEST_LENGTH);
    env->SetByteArrayRegion(ret, 0, SHA256_DIGEST_LENGTH, (jbyte *)hash);

    return ret;
}
```

然后，你需要在你的 Java 代码中使用 JNI 来调用这个功能：

```java
public class MainActivity extends AppCompatActivity {

    static {
        System.loadLibrary("native-lib");
    }

    public native byte[] getPltHash();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
       

 byte[] pltHash = getPltHash();

        // do something with pltHash
    }
}
```

需要注意的是，这里的代码基于 ELF 格式的 so 文件，并且使用了 OpenSSL 的 SHA256 来计算哈希。在 Android NDK 中并没有提供 OpenSSL，你需要自己编译或者找一个预编译版本。还有，代码中的包名和类名需要替换成你实际的包名和类名。

另外，这个代码只是一个基础版本，它没有处理错误，也没有进行详细的测试，你可能需要根据实际情况进行调整。

最后，请注意，JNI 有一些特殊的编程需求和限制，例如，所有 JNI 函数都必须返回一个结果，即使那个结果没有被使用。而且，JNI 函数名必须遵循一定的命名规则，否则 JVM 将无法找到并调用这些函数。具体细节可以参考 Oracle 的 JNI 规范。











