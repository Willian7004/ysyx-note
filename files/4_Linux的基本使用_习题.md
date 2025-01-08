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

### Shell 工具和脚本

**1**
```shell
(base) william@william-T5-Series:~/下载/GitHub/ysyx-workbench$ ls -a
.  ..  .git  .gitignore  init.sh  Makefile  npc  README.md
(base) william@william-T5-Series:~/下载/GitHub/ysyx-workbench$ ls -h
init.sh  Makefile  npc  README.md
(base) william@william-T5-Series:~/下载/GitHub/ysyx-workbench$ ls -t
Makefile  init.sh  npc  README.md
(base) william@william-T5-Series:~/下载/GitHub/ysyx-workbench$ ls --color=auto
init.sh  Makefile  npc  README.md
```
**2**

/home/william/tmp/marco.sh
```shell
marco() {
     export MARCO=$(pwd)
 }
 polo() {
     cd "$MARCO"
 }
```
```shell
(base) william@william-T5-Series:~/tmp$ source /home/william/tmp/marco.sh
(base) william@william-T5-Series:~/tmp$ marco
(base) william@william-T5-Series:~/tmp$ cd
(base) william@william-T5-Series:~$ polo

```
**3**

（题目中的脚本保存到error_test.sh）

用于运行的脚本run_error_test.sh
```shell
#!/bin/bash

# 初始化计数器
count=0

# 无限循环
while true; do
    # 增加计数器
    ((count++))
    
    # 运行 error_test.sh 并将输出追加到 error_test.log
    sudo bash ./error_test.sh >> error_test.log 2>&1
    
    # 检查上一个命令的退出状态
    if [ $? -eq 1 ]; then
        # 如果退出状态为1，打印运行次数并退出循环
        echo "脚本在运行 $count 次后出错"
        break
    fi
done
```
**4**
```bash
find . -type f -name "*.html" -print0 | xargs -0 zip html_files.zip
```
**5**
```bash
(base) william@william-T5-Series:~/tmp$ find . -type f -exec ls -ltu {} + | awk '{for(i=8; i<=NF; i++) printf "%s ", $i; print ""}'
17:24 ./html_files.zip 
17:24 ./missing/test2.html 
17:24 ./test 1.html 
16:17 ./error_test.log 
16:17 ./run_error_test.sh 
16:11 ./error_test.sh 
15:17 ./marco.sh 
12:20 ./missing/semester 
```

