

# 文件创建时间相关

Android stat 获取的文件时间，有以下三种

```
#define st_atime st_atim.tv_sec
#define st_mtime st_mtim.tv_sec
#define st_ctime st_ctim.tv_sec
```

分别是访问、更改、状态更改时间

访问时间 (st_atime)：这代表了文件或目录最后一次被访问的时间。"访问" 通常指的是读取文件的内容，而不是获取文件的元数据（如文件大小等）。例如，当你打开一个文件来阅读时，系统会更新这个时间戳。

修改时间 (st_mtime)：这代表了文件内容最后一次被修改的时间。任何对文件数据的更改都会更新这个时间戳。这包括写入文件、截断文件等操作。这是开发者和系统管理员最常关注的时间戳之一，因为它反映了文件内容的最后更改时间。

状态更改时间 (st_ctime)：这代表了文件状态（元数据）最后一次被修改的时间。这不仅包括文件内容的修改，还包括对文件的元数据的修改，如更改文件的权限、所有权或链接数。注意，st_ctime 和“创建时间”不同；它不表示文件何时被创建。


## 为什么 st_atime 没有更新？

1. `noatime` 挂载选项：为了提高性能，许多 `Linux` 系统（包括 Android）在挂载文件系统时使用 noatime 选项。这意味着系统在访问文件时不会更新访问时间，因为每次更新访问时间都需要写入磁盘，这可能导致性能下降，特别是在频繁读取文件的场景中。

2. `relatime` 挂载选项：一些系统可能使用 `relatime` 选项，它会在某些条件下更新访问时间，例如仅当访问时间早于修改时间或状态更改时间时。这种方法减少了磁盘写入操作，同时仍然保持了一定程度的访问时间跟踪。


在 Android shell 内通过 mount 命令可以看到所有的挂载目录都有 noatime 的配置，这个是提高了底层的执行效率，示例 


```
/dev/fuse on /storage/emulated type fuse (rw,lazytime,nosuid,nodev,noexec,noatime,user_id=0,group_id=0,allow_other)

/data/media on /mnt/user/0/emulated/0/Android/data type sdcardfs (rw,nosuid,nodev,noexec,noatime,fsuid=1023,fsgid=1023,gid=1015,multiuser,mask=6,derive_gid,default_normal,unshared_obb)
/data/media on /mnt/androidwritable/0/emulated/0/Android/obb type sdcardfs (rw,nosuid,nodev,noexec,noatime,fsuid=1023,fsgid=1023,gid=1015,multiuser,mask=6,derive_gid,default_normal,unshared_obb)
/data/media on /storage/emulated/0/Android/obb type sdcardfs (rw,nosuid,nodev,noexec,noatime,fsuid=1023,fsgid=1023,gid=1015,multiuser,mask=6,derive_gid,default_normal,unshared_obb)
/data/media on /mnt/user/0/emulated/0/Android/obb type sdcardfs (rw,nosuid,nodev,noexec,noatime,fsuid=1023,fsgid=1023,gid=1015,multiuser,mask=6,derive_gid,default_normal,unshared_obb)
/data/media on /mnt/installer/0/emulated/0/Android/obb type sdcardfs (rw,nosuid,nodev,noexec,noatime,fsuid=1023,fsgid=1023,gid=9997,multiuser,mask=7,derive_gid,default_normal,unshared_obb)
```



rw：表示文件系统被挂载为可读写模式。这是最常见的挂载类型，允许用户和程序读取和写入文件。

lazytime：这个选项减少了元数据（比如访问时间、修改时间等）更新到磁盘的频率。启用 lazytime 时，这些更新会在内存中缓存，并且只在特定条件下（如系统关机或文件系统卸载等）写入磁盘。这有助于提高性能并减少对磁盘的写入。

nosuid：这个选项阻止 suid（set-user-ID）和 sgid（set-group-ID）权限位的生效。这是一种安全措施，可以防止某些类型的安全漏洞，特别是在共享文件系统和公共目录中。

nodev：指定在此文件系统上不允许设备文件的创建。这是一种安全措施，用于防止对特殊设备文件的滥用。

noexec：表示在这个文件系统上不允许执行任何二进制程序。这也是一种安全措施，用于防止执行可能的恶意软件或脚本。

noatime：此选项告诉系统不要更新文件的访问时间。这通常用于提高性能，因为每次文件被读取时都不需要进行额外的磁盘写操作。

user_id=0 和 group_id=0：这些选项指定了文件系统上文件的默认用户 ID 和组 ID。在这里，0 通常是 root 用户和组。这意味着文件系统上的文件默认属于 root 用户。

allow_other：这个选项允许除了挂载文件系统的用户之外的其他用户访问文件系统。这在使用某些类型的文件系统（如 FUSE）时很重要，以确保不同的用户可以访问挂载的文件系统。



