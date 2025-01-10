### 关于PA0的补充

1.前几天看PA0漏掉后面克隆和编译仓库的部分了。之前是用github desktop克隆仓库的，但文档中包含子仓库和其它一些指令，无法用github desktop操作，换了git但又遇到连接超时问题，在sshconfig中吧github的22端口改用443端口能解决。会出现这种情况感觉windows上用git bash反而比较少坑。

2.make nenuconfig报错

```bash
$ make menuconfig
/home/william/下载/GitHub/ics2024/nemu/scripts/config.mk:20: Warning: .config does not exist!
/home/william/下载/GitHub/ics2024/nemu/scripts/config.mk:21: To build the project, first run 'make menuconfig'.
+ CC confdata.c
+ CC expr.c
+ CC preprocess.c
+ CC symbol.c
+ CC util.c
+ YACC build/parser.tab.h
make[1]: bison: 没有那个文件或目录
make[1]: *** [Makefile:32：build/parser.tab.h] 错误 127
make: *** [/home/william/下载/GitHub/ics2024/nemu/scripts/config.mk:39：/home/william/下载/GitHub/ics2024/nemu/tools/kconfig/build/mconf] 错误 2
```

经查询需要安装bison和flex

安装后再次编译报错

```bash
$ make menuconfig
/home/william/下载/GitHub/ics2024/nemu/scripts/config.mk:20: Warning: .config does not exist!
/home/william/下载/GitHub/ics2024/nemu/scripts/config.mk:21: To build the project, first run 'make menuconfig'.
+ YACC build/parser.tab.h
+ LEX build/lexer.lex.c
+ CC build/lexer.lex.c
+ CC build/parser.tab.c
+ CC mconf.c
In file included from mconf.c:23:
lxdialog/dialog.h:19:10: fatal error: ncurses.h: 没有那个文件或目录
   19 | #include <ncurses.h>
      |          ^~~~~~~~~~~
compilation terminated.
make[1]: *** [/home/william/下载/GitHub/ics2024/nemu/scripts/build.mk:34：/home/william/下载/GitHub/ics2024/nemu/tools/kconfig/build/obj-mconf/mconf.o] 错误 1
make: *** [/home/william/下载/GitHub/ics2024/nemu/scripts/config.mk:39：/home/william/下载/GitHub/ics2024/nemu/tools/kconfig/build/mconf] 错误 2
```

对于其它项目，如果根据文档操作还有两次以上需要通过搜索解决的错误，基本就是“你不干有得是人干”了。不过这个项目是课程中的，就继续搜索，从一个不完全匹配的搜索结果得到要安装libncurses5-dev，安装后make menuconfig通过，执行下一步make报错

```bash
$ make
+ CC src/nemu-main.c
+ CC src/device/io/map.c
+ CC src/device/io/mmio.c
+ CC src/device/io/port-io.c
+ CC src/engine/interpreter/hostcall.c
+ CC src/engine/interpreter/init.c
+ CC src/cpu/cpu-exec.c
+ CC src/cpu/difftest/dut.c
+ CC src/cpu/difftest/ref.c
+ CC src/monitor/monitor.c
+ CC src/monitor/sdb/expr.c
+ CC src/monitor/sdb/sdb.c
src/monitor/sdb/sdb.c:18:10: fatal error: readline/readline.h: 没有那个文件或目录
   18 | #include <readline/readline.h>
      |          ^~~~~~~~~~~~~~~~~~~~~
compilation terminated.
make: *** [/home/william/下载/GitHub/ics2024/nemu/scripts/build.mk:34：/home/william/下载/GitHub/ics2024/nemu/build/obj-riscv32-nemu-interpreter/src/monitor/sdb/sdb.o] 错误 1
```

搜索得出需要安装libreadline-dev，安装后编译通过。

后面的步骤与文档一致，这里不另做说明。

### 搭建verilator仿真环境

文档中说apt源中的verilator的版本较旧，实际版本为5.020，比文档中的5.008版本新。我在群里提到这一情况，群友说文档讲的应该是Ubuntu20.04的版本情况，而我目前用的Linux Mint22是Ubuntu24.04的下游版本。

文档中没有说明verilator的使用方法。用man verilator得到的是指令说明，官网的操作说明相对详细。

