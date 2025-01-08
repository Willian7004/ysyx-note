### 课程概览与 shell
```shell
(base) william@william-T5-Series:~$ echo $SHELL
/bin/bash
(base) william@william-T5-Series:~$ mkdir tmp
(base) william@william-T5-Series:~$ ls
公共  模板  视频  图片  文档  下载  音乐  桌面  miniconda3  tmp
(base) william@william-T5-Series:~$ cd tmp
(base) william@william-T5-Series:~/tmp$ mkdir missing
(base) william@william-T5-Series:~/tmp$ man touch
(base) william@william-T5-Series:~/tmp$ cd missing
(base) william@william-T5-Series:~/tmp/missing$ touch semester
(base) william@william-T5-Series:~/tmp/missing$ vim semester
(base) william@william-T5-Series:~/tmp/missing$ bash ./semester
HTTP/1.1 200 Connection established

HTTP/2 200 
server: GitHub.com
content-type: text/html; charset=utf-8
last-modified: Sat, 21 Dec 2024 16:53:01 GMT
access-control-allow-origin: *
etag: "6766f26d-205d"
expires: Sun, 05 Jan 2025 03:23:33 GMT
cache-control: max-age=600
x-proxy-cache: MISS
x-github-request-id: 27F2:1392F1:6F7C45F:731BBB3:6779F8DC
accept-ranges: bytes
age: 0
date: Wed, 08 Jan 2025 04:20:35 GMT
via: 1.1 varnish
x-served-by: cache-lax-kwhp1940030-LAX
x-cache: HIT
x-cache-hits: 0
x-timer: S1736310035.933911,VS0,VE114
vary: Accept-Encoding
x-fastly-request-id: 025db0f128b946f7fb6f4b97f6197af5347061d6
content-length: 8285

(base) william@william-T5-Series:~/tmp/missing$ cd
(base) william@william-T5-Series:~$ touch last-modified.txt
(base) william@william-T5-Series:~$ echo “Sat, 21 Dec 2024 16:53:01 GMT” >>last-modified.txt
(base) william@william-T5-Series:~$ sudo find /sys/ -name capacity -exec cat {} \;
[sudo] william 的密码：          
68
cat: /sys/module/zfs/properties.vdev/capacity: 是一个目录
cat: /sys/module/zfs/properties.pool/capacity: 是一个目录
(base) william@william-T5-Series:~$ 
```
本次习题通过搜索完成了部分内容，写入刚开始按习惯用了vim（主要是命令行用vim，大部分时候都用图形界面），后面根据提示换成用>>追加。

