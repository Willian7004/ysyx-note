### 关于PA0的补充

1.开始时看PA0漏掉后面克隆和编译仓库的部分了。以前是用github desktop克隆仓库的，但文档中包含子仓库和其它一些指令，无法用github desktop操作，换了git但又遇到连接超时问题，在sshconfig中吧github的22端口改用443端口能解决。会出现这种情况感觉windows上用git bash反而比较少坑。

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

文档中没有说明verilator的使用方法。用man verilator得到的是指令说明，官方文档的操作说明相对详细。

**1.示例: 双控开关**

测试过程很复杂，原本做了完整记录但还是决定删掉了，得到的结论有两点：

（1）.v文件使用top.v会导致找不到头文件，使用verilator文档中our.v的名称并修改代码中的module名称能编译通过。后面发现是与头文件名称对应，our.v编译为Vour.h。

（2）verilator头文件和c++头文件之间要空行，之前认为不能添加c++头文件，偶然看到一篇文章才发现这个问题。由于相关文章没有提到报错内容，从报错内容并不能搜索到这一问题。

修改后的文件如下：

vsrc/our.v

```verilog
  module our(
     input a,
     input b,
     output f
   );
  assign f = a ^ b;
  endmodule
```

csrc/sim_main.cpp

```cpp
  #include <stdio.h>
  #include <stdlib.h>
  #include <assert.h>

  #include "Vour.h"
  #include "verilated.h"
  int main(int argc, char** argv) {
      VerilatedContext* contextp = new VerilatedContext;
      contextp->commandArgs(argc, argv);
      Vour* top = new Vour{contextp};
      while (!contextp->gotFinish()) 
    { int a = rand() & 1;
      int b = rand() & 1;
      top->a = a;
      top->b = b;
      top->eval();
      printf("a = %d, b = %d, f = %d\n", a, b, top->f);
      assert(top->f == (a ^ b)); }
      delete top;
      delete contextp;
      return 0;
  }
```

编译和运行过程

```bash
ysyx-workbench/npc$ verilator --cc --exe --build -j 0 -Wall csrc/sim_main.cpp vsrc/our.v
make: 进入目录“/home/william/下载/GitHub/ysyx-workbench/npc/obj_dir”
g++  -I.  -MMD -I/usr/share/verilator/include -I/usr/share/verilator/include/vltstd -DVM_COVERAGE=0 -DVM_SC=0 -DVM_TRACE=0 -DVM_TRACE_FST=0 -DVM_TRACE_VCD=0 -faligned-new -fcf-protection=none -Wno-bool-operation -Wno-overloaded-virtual -Wno-shadow -Wno-sign-compare -Wno-uninitialized -Wno-unused-but-set-parameter -Wno-unused-but-set-variable -Wno-unused-parameter -Wno-unused-variable       -Os -c -o sim_main.o ../csrc/sim_main.cpp
g++ -Os  -I.  -MMD -I/usr/share/verilator/include -I/usr/share/verilator/include/vltstd -DVM_COVERAGE=0 -DVM_SC=0 -DVM_TRACE=0 -DVM_TRACE_FST=0 -DVM_TRACE_VCD=0 -faligned-new -fcf-protection=none -Wno-bool-operation -Wno-overloaded-virtual -Wno-shadow -Wno-sign-compare -Wno-uninitialized -Wno-unused-but-set-parameter -Wno-unused-but-set-variable -Wno-unused-parameter -Wno-unused-variable       -c -o verilated.o /usr/share/verilator/include/verilated.cpp
g++ -Os  -I.  -MMD -I/usr/share/verilator/include -I/usr/share/verilator/include/vltstd -DVM_COVERAGE=0 -DVM_SC=0 -DVM_TRACE=0 -DVM_TRACE_FST=0 -DVM_TRACE_VCD=0 -faligned-new -fcf-protection=none -Wno-bool-operation -Wno-overloaded-virtual -Wno-shadow -Wno-sign-compare -Wno-uninitialized -Wno-unused-but-set-parameter -Wno-unused-but-set-variable -Wno-unused-parameter -Wno-unused-variable       -c -o verilated_threads.o /usr/share/verilator/include/verilated_threads.cpp
/usr/bin/python3 /usr/share/verilator/bin/verilator_includer -DVL_INCLUDE_OPT=include Vour.cpp Vour___024root__DepSet_hf7027e39__0.cpp Vour___024root__DepSet_h637983f1__0.cpp Vour___024root__Slow.cpp Vour___024root__DepSet_hf7027e39__0__Slow.cpp Vour___024root__DepSet_h637983f1__0__Slow.cpp Vour__Syms.cpp > Vour__ALL.cpp
echo "" > Vour__ALL.verilator_deplist.tmp
g++ -Os  -I.  -MMD -I/usr/share/verilator/include -I/usr/share/verilator/include/vltstd -DVM_COVERAGE=0 -DVM_SC=0 -DVM_TRACE=0 -DVM_TRACE_FST=0 -DVM_TRACE_VCD=0 -faligned-new -fcf-protection=none -Wno-bool-operation -Wno-overloaded-virtual -Wno-shadow -Wno-sign-compare -Wno-uninitialized -Wno-unused-but-set-parameter -Wno-unused-but-set-variable -Wno-unused-parameter -Wno-unused-variable       -c -o Vour__ALL.o Vour__ALL.cpp
Archive ar -rcs Vour__ALL.a Vour__ALL.o
g++     sim_main.o verilated.o verilated_threads.o Vour__ALL.a    -pthread -lpthread -latomic   -o Vour
rm Vour__ALL.verilator_deplist.tmp
make: 离开目录“/home/william/下载/GitHub/ysyx-workbench/npc/obj_dir”
(base) william@william-T5-Series:~/下载/GitHub/ysyx-workbench/npc$ obj_dir/Vour
a = 1, b = 0, f = 1
a = 1, b = 1, f = 0
a = 1, b = 1, f = 0
a = 0, b = 0, f = 0
a = 1, b = 1, f = 0
a = 0, b = 1, f = 1
a = 0, b = 1, f = 1
a = 1, b = 0, f = 1
a = 0, b = 0, f = 0
a = 0, b = 0, f = 0
a = 1, b = 0, f = 1
a = 1, b = 1, f = 0
a = 0, b = 0, f = 0
a = 0, b = 1, f = 1
a = 1, b = 1, f = 0
a = 1, b = 0, f = 1
```

**2.打印并查看波形**

修改后的sim_main.cpp

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "Vour.h"
#include "verilated.h"

#include "verilated_vcd_c.h" //可选，如果要导出vcd则需要加上

int main(int argc, char** argv) {
    VerilatedContext* contextp = new VerilatedContext;
    contextp->commandArgs(argc, argv);
    Vour* top = new Vour{contextp};

    VerilatedVcdC* tfp = new VerilatedVcdC; //初始化VCD对象指针
    contextp->traceEverOn(true); //打开追踪功能
    top->trace(tfp, 0); //
    tfp->open("wave.vcd"); //设置输出的文件wave.vcd
    
    int i=0;
    while (!contextp->gotFinish()&& i<64) {
        int a = rand() & 1;
        int b = rand() & 1;
        top->a = a;
        top->b = b;
        top->eval();
        printf("a = %d, b = %d, f = %d\n", a, b, top->f);
        assert(top->f == (a ^ b)); 

        tfp->dump(contextp->time()); //dump wave
        contextp->timeInc(1); //推动仿真时间

        i++;
        }
    delete top;
    tfp->close();
    delete contextp;
    return 0;
}
```

运行过程

```bash
(base) william@william-T5-Series:~/下载/GitHub/ysyx-workbench/npc$ verilator -Wall vsrc/our.v csrc/sim_main.cpp --cc --trace --exe --build
make: 进入目录“/home/william/下载/GitHub/ysyx-workbench/npc/obj_dir”
g++  -I.  -MMD -I/usr/share/verilator/include -I/usr/share/verilator/include/vltstd -DVM_COVERAGE=0 -DVM_SC=0 -DVM_TRACE=1 -DVM_TRACE_FST=0 -DVM_TRACE_VCD=1 -faligned-new -fcf-protection=none -Wno-bool-operation -Wno-overloaded-virtual -Wno-shadow -Wno-sign-compare -Wno-uninitialized -Wno-unused-but-set-parameter -Wno-unused-but-set-variable -Wno-unused-parameter -Wno-unused-variable       -Os -c -o sim_main.o ../csrc/sim_main.cpp
g++     sim_main.o verilated.o verilated_vcd_c.o verilated_threads.o Vour__ALL.a    -pthread -lpthread -latomic   -o Vour
make: 离开目录“/home/william/下载/GitHub/ysyx-workbench/npc/obj_dir”
(base) william@william-T5-Series:~/下载/GitHub/ysyx-workbench/npc$ obj_dir/Vour
a = 1, b = 0, f = 1
a = 1, b = 1, f = 0
a = 1, b = 1, f = 0
a = 0, b = 0, f = 0
a = 1, b = 1, f = 0
a = 0, b = 1, f = 1
a = 0, b = 1, f = 1
a = 1, b = 0, f = 1
a = 0, b = 0, f = 0
a = 0, b = 0, f = 0
a = 1, b = 0, f = 1
a = 1, b = 1, f = 0
a = 0, b = 0, f = 0
a = 0, b = 1, f = 1
a = 1, b = 1, f = 0
a = 1, b = 0, f = 1
a = 0, b = 0, f = 0
a = 1, b = 1, f = 0
a = 1, b = 0, f = 1
a = 1, b = 0, f = 1
a = 1, b = 1, f = 0
a = 1, b = 1, f = 0
a = 0, b = 1, f = 1
a = 0, b = 0, f = 0
a = 1, b = 0, f = 1
a = 1, b = 0, f = 1
a = 1, b = 0, f = 1
a = 0, b = 1, f = 1
a = 0, b = 0, f = 0
a = 0, b = 1, f = 1
a = 1, b = 1, f = 0
a = 0, b = 1, f = 1
a = 0, b = 1, f = 1
a = 0, b = 1, f = 1
a = 1, b = 1, f = 0
a = 0, b = 1, f = 1
a = 0, b = 1, f = 1
a = 0, b = 1, f = 1
a = 0, b = 0, f = 0
a = 1, b = 0, f = 1
a = 1, b = 0, f = 1
a = 0, b = 0, f = 0
a = 0, b = 0, f = 0
a = 1, b = 1, f = 0
a = 0, b = 1, f = 1
a = 0, b = 0, f = 0
a = 0, b = 0, f = 0
a = 1, b = 0, f = 1
a = 0, b = 0, f = 0
a = 0, b = 1, f = 1
a = 1, b = 0, f = 1
a = 0, b = 0, f = 0
a = 1, b = 1, f = 0
a = 1, b = 0, f = 1
a = 1, b = 0, f = 1
a = 0, b = 0, f = 0
a = 1, b = 0, f = 1
a = 0, b = 1, f = 1
a = 1, b = 1, f = 0
a = 0, b = 1, f = 1
a = 0, b = 1, f = 1
a = 1, b = 1, f = 0
a = 1, b = 1, f = 0
a = 1, b = 1, f = 0
(base) william@william-T5-Series:~/下载/GitHub/ysyx-workbench/npc$ gtkwave wave.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[63] end time.
WM Destroy
```

**3编写Makefile**

修改Makefile如下

```makefile
all:
	@echo "Write this Makefile by your self."

sim:
	$(call git_commit, "sim RTL"); # DO NOT REMOVE THIS LINE!!!
	verilator -Wall vsrc/our.v csrc/sim_main.cpp --cc --trace --exe --build;obj_dir/Vour;gtkwave wave.vcd
    
include ../Makefile
```

**4.接入NVBoard**

按文档执行，makefile能找到路径但无法导入头文件，绑定指令去掉括号能执行但出错
```bash
ysyx-workbench/npc/vsrc$ python $NVBOARD_HOME/scripts/auto_pin_bind.py signal.txt output.cpp
Error: Invalid pin pin
```
signal.txt
```bash
top=our

# Line comment inside nxdc
signal pin
signal (pin1, pin2, pin3)
```

**5.示例: 流水灯**

.v文件与文档相同，.cpp文件调整了几次顺序，编译通过

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "Vour.h"
#include "verilated.h"

#include "verilated_vcd_c.h" //可选，如果要导出vcd则需要加上

VerilatedContext* contextp = new VerilatedContext;

Vour* top = new Vour{contextp}; 

void single_cycle() {
  top->clk = 0; top->eval();
  top->clk = 1; top->eval();
}

void reset(int n) {
  top->rst = 1;
  while (n -- > 0) single_cycle();
  top->rst = 0;
}



int main(int argc, char** argv) {
    contextp->commandArgs(argc, argv); 
    reset(10);  // 复位10个周期
    VerilatedVcdC* tfp = new VerilatedVcdC; //初始化VCD对象指针
    contextp->traceEverOn(true); //打开追踪功能
    top->trace(tfp, 0); //
    tfp->open("wave.vcd"); //设置输出的文件wave.vcd
    
    int i=0;
    while (!contextp->gotFinish()&& i<50) {
        single_cycle(); 

        tfp->dump(contextp->time()); //dump wave
        contextp->timeInc(1); //推动仿真时间
        i++;
        }
    delete top;
    tfp->close();
    delete contextp;
    return 0;
}
```

注意：由于系统故障，本笔记中的项目完成后的第二天进行了系统回滚，可能损失部分开发跟踪数据，只保证恢复最后一个示例的内容。


