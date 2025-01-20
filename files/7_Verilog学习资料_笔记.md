这是“数字电路基础实验”部分中的“verilog学习资料”的笔记。之前在HDLBits了解过不少语法，这里主要记录这部分资料提到的设计思路和之前未了解到的语法。

### 1.三段式状态机

（资料上的代码逻辑不够清晰，另外查询有关代码进行记录）

从状态 A，如果 w 为 1，则转移到状态 B，否则保持在状态 A。

从状态 B，如果 w 为 1，则转移到状态 C，否则返回到状态 A。

从状态 C，如果 w 为 1，则保持在状态 C，否则返回到状态 A。
```verilog
module simple(
    input clk,          // 时钟信号
    input rst_n,        // 异步复位信号，低电平有效
    input w,            // 输入信号，用于状态转移
    output reg[1:0] z   // 输出信号，表示当前状态
);

// 定义状态编码
localparam A = 2'b00;   // 状态A，编码为00
localparam B = 2'b01;   // 状态B，编码为01
localparam C = 2'b10;   // 状态C，编码为10

reg [1:0] current_state; // 当前状态寄存器
reg [1:0] next_state;    // 下一个状态寄存器

// 状态转移逻辑
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        // 复位时，将当前状态设置为A
        current_state <= A;
    end
    else begin
        // 否则，将当前状态更新为下一个状态
        current_state <= next_state;
    end
end

// 组合逻辑，根据当前状态和输入w计算下一个状态
always @(*) begin
    case (current_state)
        A: begin
            // 当前状态为A时
            if (w) begin
                // 如果w为1，转移到状态B
                next_state = B;
            end
            else begin
                // 否则，保持在状态A
                next_state = A;
            end
        end 
        B: begin
            // 当前状态为B时
            if (w) begin
                // 如果w为1，转移到状态C
                next_state = C;
            end
            else begin
                // 否则，返回到状态A
                next_state = A;
            end
        end
        C: begin
            // 当前状态为C时
            if (w) begin
                // 如果w为1，保持在状态C
                next_state = C;
            end
            else begin
                // 否则，返回到状态A
                next_state = A;
            end
        end
        default: begin
            // 默认情况下，返回到状态A
            next_state = A;
        end
    endcase
end

// 输出逻辑，根据下一个状态设置输出z
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        // 复位时，输出z为0
        z <= 2'd0;
    end
    else begin
        case (next_state)
            A: z <= 2'd0; // 下一个状态为A时，输出0
            B: z <= 2'd1; // 下一个状态为B时，输出1
            C: z <= 2'd2; // 下一个状态为C时，输出2
            default: z <= 2'd0; // 默认情况下，输出0
        endcase
    end
end

endmodule
```

### 2.原理图描述法优缺点

优点：直观、元件丰富

缺点：不利于复用，芯片换代后要更改原理图

描述电路首选HDL语言，只在要求图形描述设计顶层时使用原理图。

### 3.波形设计工具

简单信号容易用波形描述，复杂的测试激励难以用波形描述。

应当优先使用代码进行测试。

### 3.Verilog的缺点

错误检测能力弱（需要EDA工具支持）

参数化能力弱

代码复用程度低

需要手动连线和声明中间信号

### 4.HDL与c语言的区别

wire变量描述模块连接关系

能有效描述并行硬件系统

定义了绝对和相对时间，有物理延时

### 5.运行顺序

Verilog的module中，所有描述语句（包括连续赋值语句、行为语句块alwaysinitial以及模块实例化等）都是并行发生的，而begin...end中的语句应该是顺序执行的。

### 6.wire和reg

wire型：表示电路模块中的连线，仿真波形中不可见

reg型：占用仿真环境的物理内存，会显示在仿真波形中，在时序电路中必为寄存器

凡是在always initial语句中赋值的变量，一定是reg型

凡是在assign语句中赋值的变量，一定是wire型

### 7.always语句块

后接敏感列表，用@表示

always@（a or b or c）表示只要a,b,c中有一个产生变换，则执行该always块

一般包含begin...end语句组

always@（*）表示白动将该always块中所有引用的信号都白动添加到敏感列表中（组合逻辑）

always@（posedge clk or negedge rst_n)代表只在clk上升沿或rst_n下降沿上执行该always块（时序逻辑）

### 8.选择语句优先级

if-else有优先级

case无优先级

### 9.触发器和锁存器

寄存器（Register）在时钟上升或下降沿存入数据

锁存器（Latch）在高电平或低电平存入数据，易传播毛刺，只用于异步电路和低功耗电路

if语句缺少else或case语句缺少default易引入锁存器，会以warning报告

D触发器(DFF)
```verilog
always@ (posedge clk or negedge rst_n）
begin
    if（rst_n==1'b0）
        Q<=1b'0;
    else
        Q<=D;
end
```

### 10.组合逻辑与时序逻辑

组合逻辑用“=”赋值。时序逻辑用“<=”赋值，需要复位，每增加一个触发器使输出推迟1个时钟周期。

### 11.存储器

语法：reg[数据位宽]名称[地址位宽]，例如数据8bit、地址64bit的RAM8x64为reg[7:0]RAM8x64[0:63]

使用存储单元应当赋值给寄存器再对寄存器进行操作

FPGA由于内置块RAM和分布式RAM等资源，建议使用配套的ip生成器进行调用。

### 12.流水线

通过增加寄存器实现时序电路中多个步骤并行，可以提高效率。

### 13.优化方法

确认电路要以性能优先还是面积优先

使用硬件思维，代码代表硬件模块

预先进行规划

### 14.波形文件

vcd是标准波形文件，所有仿真器都支持，包含信号变化信息，可用于估算功耗，但体积大。

其它格式一般适用于特定仿真器，体积较小。

生成方法（位于testbench）
```verilog
initial
begin
    $dumfile("*.vcd"); //*为文件名
    $dumpvars(0,**); //抽取特定模块或信号，**为测试文件名
end
```
