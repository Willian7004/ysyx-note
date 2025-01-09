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
(base) william@william-T5-Series:~$ 
(base) william@william-T5-Series:~$ sudo find /sys/ -name capacity -exec cat {} \;
[sudo] william 的密码：          
68
cat: /sys/module/zfs/properties.vdev/capacity: 是一个目录
cat: /sys/module/zfs/properties.pool/capacity: 是一个目录
(base) william@william-T5-Series:~$ 
```
本次习题通过搜索完成了部分内容，写入刚开始按习惯用了vim（主要是命令行用vim，大部分时候都用图形界面），后面根据提示换成用>>追加。文档中部分内容没有明确是指令中的语句也导致需要进行额外的搜索。

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
这部分内容比上一部分复杂，要搜索的内容也多一些。不过大部分功能可以在桌面环境实现，因此之前不怎么了解这类指令，按文档操作时有时候会用上。

### 编辑器 (Vim)

**1**

vimtutor的内容与文档类似，主要提供了一些操作案例。我此前主要用wq、q、i指令，移动光标用方向键，可以完成所有操作。在有桌面环境的情况下，vim主要用于修改在一些文档中提供了完整路径的文件。文档中提到了不少新的快捷键，可以提高效率。实际操作发现，如果不是极为熟悉快捷键，在有桌面环境时都难以达到鼠标操作的效率，在没有桌面环境且没有安装jupyter notebook等可以鼠标操作的远程控制工具的设备中vim才会对一般用户来说有优势。

另外提几个槽点。括号配对用%跳转的确是比较方便的设计，但增加类似于不少IDE中用到的对配对的括号高亮显示的功能会更方便。替换命令中s键的功能跟我目前的版本不同，我的版本中s是删除当前字符并进入插入模式。使用vim -v得到的版本为
```
VIM - Vi IMproved                                
版本 9.1.697                                  
维护人 Bram Moolenaar 等                            
修改者 team+vim@tracker.debian.org 
```
用man vim指令也没有查找到关于当前版本的替换命令的内容。后文中使用R的替换指令能正常使用。

**2**

文档提供的vimrc提到了vim的一些自定义选项并进行了自定义。放到指定目录后会使操作方式与前文的不一致，最终决定不使用。

### 数据整理

**2**

count_words.sh
```bash
# 定义输入文件
input_file="words"

# 查找包含至少三个 'a' 且不以 's 结尾的单词
filtered_words=$(grep -E '^(.*a.*){3,}$' "$input_file" | grep -v "'s$")

# 统计符合条件的单词个数
word_count=$(echo "$filtered_words" | wc -l)

# 提取这些单词的末尾两个字母
last_two_chars=$(echo "$filtered_words" | sed 's/.*\(..\)$/\1/')

# 统计末尾两个字母的频率并找出前三
top_three=$(echo "$last_two_chars" | sort | uniq -c | sort -nr | head -n 3)

# 输出结果
echo "符合条件的单词个数: $word_count"
echo "出现频率前三的末尾两个字母及其频率:"
echo "$top_three"
```
运行结果
```bash
(base) william@william-T5-Series:~/tmp$ bash count_words.sh
符合条件的单词个数: 768
出现频率前三的末尾两个字母及其频率:
     85 an
     57 ns
     52 as
```

**3**

替换文件时出错会导致文件损坏。

**4、5**

先吐槽一下，journalctl是systemmd的功能，虽然大部分Linux发行版有systemmd，但装了没有systemmd的Linux发行版的人就需要安装其它发行版或使用虚拟机来完成这项任务了。我由于是项目开始才安装的系统，启动次数较少，也跳过这两步。

### 命令行环境

**任务控制**

**1**

```bash
base) william@william-T5-Series:~/tmp$ sleep 10000
^Z
[1]+  已停止               sleep 10000
(base) william@william-T5-Series:~/tmp$ bg
[1]+ sleep 10000 &
(base) william@william-T5-Series:~/tmp$ pgrep sleep
293603
293833
293930
(base) william@william-T5-Series:~/tmp$ pkill  -af sleep
```

**2**

```bash
(base) william@william-T5-Series:~/tmp$ sleep 60 &
pgrep sleep | wait; ls
[1] 294596
 count_words.sh   error_test.sh    marco.sh   run_error_test.sh   warn.txt
 error_test.log   html_files.zip   missing   'test 1.html'        words
```

**终端多路复用**

由于Linux Mint的终端带有标签页功能，考虑到目前使用的缩放比例较高以及外观一致性问题，暂不使用终端模拟器。

**配置文件**

目前已改用GitHub Desktop管理项目，不再使用文档中的流程。

### 版本控制(Git)

由于GitHub Desktop没有给出文档中部分功能，以下使用GitHub CLI进行操作

**2**
```bash
(base) william@william-T5-Series:~/tmp/missing-semester-cn.github.io$  git log --all --graph --decorate
*   commit e9ec93e59b060865dcb2fbb9da05f0e0d6245b58 (HEAD -> master, origin/master, origin/HEAD)
|\  Merge: 89f3b60 8f0e3f3
| | Author: Lingfeng_Ai <hanxiaomax@gmail.com>
| | Date:   Sat Dec 7 18:14:46 2024 +0800
| | 
| |     Merge pull request #187 from attackedrookie/master
| |     
| |     修改404.html文件
| | 
| * commit 8f0e3f36f168ff89a1a6d787c28bae9f10bc46ff
|/  Author: Lin <2106639605@qq.com>
|   Date:   Fri Dec 6 16:39:28 2024 +0800
|   
|       修改404.html文件
|       
|       提升可读性、样式以及用户体验、添加导航链接提供返回首页的途径或者搜索功能能够帮助用户轻松回到正轨。我添加了一些基础的
|       CSS 样式，使 404
|       页面在视觉上更具辨识度。例如，为错误代码使用了更大的字号，采用了更醒目的颜色，并且确保链接能够突出显示且便于操作。
|   
*   commit 89f3b6094784a6b64baa5d01daf92f200543f47f
(base) william@william-T5-Series:~/tmp/missing-semester-cn.github.io$ git log -1 README.md
commit fc93d7c0660cee7ac2dfeb23fd85f9ec741ff3a8
Author: Zhenger233 <2042712521@qq.com>
Date:   Fri Nov 15 00:01:20 2024 +0800

    修改为中文README
(base) william@william-T5-Series:~/tmp/missing-semester-cn.github.io$  git blame _config.yml | grep collections
a88b4eac (Anish Athalye  2020-01-17 15:26:30 -0500 18) collections:

```

补充：目前用的Linux Mint在默认配置下不能正常使用git，需要在sshconfig中把22端口改为443端口。github disktop和github cli都没有这一问题。

**3**

```bash
(base) william@william-T5-Series:~/tmp/missing-semester-cn.github.io$  git filter-branch --force --index-filter\
 'git rm --cached --ignore-unmatch ./my_password' \
 --prune-empty --tag-name-filter cat -- --all
WARNING: git-filter-branch has a glut of gotchas generating mangled history
	 rewrites.  Hit Ctrl-C before proceeding to abort, then use an
	 alternative filtering tool such as 'git filter-repo'
	 (https://github.com/newren/git-filter-repo/) instead.  See the
	 filter-branch manual page for more details; to squelch this warning,
	 set FILTER_BRANCH_SQUELCH_WARNING=1.
Proceeding with filter-branch...

# 省略列表

Ref 'refs/heads/master' was rewritten
Ref 'refs/remotes/origin/master' was rewritten
Ref 'refs/remotes/origin/dependabot/bundler/activesupport-6.0.6.1' was rewritten
Ref 'refs/remotes/origin/dependabot/bundler/addressable-2.8.1' was rewritten
Ref 'refs/remotes/origin/dependabot/bundler/nokogiri-1.14.3' was rewritten
Ref 'refs/remotes/origin/dependabot/bundler/tzinfo-1.2.10' was rewritten
WARNING: Ref 'refs/remotes/origin/master' is unchanged
Ref 'refs/remotes/origin/review' was rewritten
```

**4**

git stash会把所有未提交的修改（包括暂存的和非暂存的）都保存起来，用于后续恢复当前工作目录。

git stash pop用于恢复上一次暂存的工作区内容。

