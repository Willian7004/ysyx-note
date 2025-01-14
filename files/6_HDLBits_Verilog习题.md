这是“数字电路基础实验”部分中的Verilog部分的内容。原本考虑学习多语言可能有开发习惯冲突，但群友还是建议同时掌握Verilog和Chisel。

以前在runoob上看过一点Verilog，但由于缺少说明，无法理解代码含义，后来就没有看了。本次课程中的hdlbits上虽然没有直接给出例程，但具有较为详细的说明，通常不需要另外查询资料就能完成。以下网站上的顺序记录各习题情况，也作为对知识点的记录。各部分均使用译文中的名称。

另外吐槽一下，hdlbits连接很慢，开代理的改善比较小。后面查询发现服务器ip属地在加拿大，改用位于美国的代理服务器就快很多。

### Verilog语言

### 基础

**1.简单电线**
```verilog
module top_module( input in, output out );
assign out=in; //输出端在等号左边
endmodule
```

**2.四根线**
```verilog
module top_module( 
    input a,b,c,
    output w,x,y,z );
assign w=a;
assign x=b;   
assign y=b;  
assign z=c;      
endmodule
```

**3.非门**
```verilog
module top_module( input in, output out );
assign out=!in; // ~为位非，!为逻辑非
endmodule
```

**4.与非门**
```verilog
module top_module( 
    input a, 
    input b, 
    output out );
assign out=a&&b; // &为按位与，&&为逻辑与
endmodule
```

**5.或非门**
```verilog
module top_module( 
    input a, 
    input b, 
    output out );
    assign out=!(a|b); //|为按位或，||为逻辑或
endmodule
```

**6.异或非门**
```verilog
module top_module( 
    input a, 
    input b, 
    output out );
assign out=!a^b; //^为按位异或，没有逻辑异或
endmodule
```

**7.声明导线**
```verilog
module top_module(
    input a,
    input b,
    input c,
    input d,
    output out,
    output out_n   ); 
    wire and1; //用wire声明导线
    assign and1=a&&b;  
    wire and2;
    assign and2=c&&d; 
    assign out=and1|and2;
    assign out_n=!(and1|and2);    
endmodule
```

**8.7458芯片**
```verilog
module top_module ( 
    input p1a, p1b, p1c, p1d, p1e, p1f,
    output p1y,
    input p2a, p2b, p2c, p2d,
    output p2y );
wire and1;
assign and1=p2a&&p2b;  
wire and2;
assign and2=p2c&&p2d; 
assign p2y=and1|and2;
wire and11;
wire and12; //多输入逻辑门创建时使用导线
assign and11=p1a&&p1b;
assign and12=p1c&&and11;   
wire and21;
wire and22;
assign and21=p1e&&p1d;
assign and22=p1f&&and21;  
assign p1y=and12||and22;    
endmodule
```

### 向量

**1.向量**
```verilog
module top_module ( 
    input wire [2:0] vec, //括号内为位数范围，从高到低，最低位为0
    output wire [2:0] outv,
    output wire o2,
    output wire o1,
    output wire o0  ); 
assign outv=vec;
assign o0=vec;
assign o1=vec[1]; //选择特定的位
assign o2=vec[2];
endmodule
```

**2.向量详细**
```verilog
module top_module( 
    input wire [15:0] in,
    output wire [7:0] out_hi,
    output wire [7:0] out_lo );
    assign out_hi=in[15:8]; //选择位数范围
    assign out_lo=in[7:0];
endmodule
```

**3.向量部分选择**
```verilog
module top_module( 
    input [31:0] in,
    output [31:0] out );
    wire [7:0]b1;
    assign b1[7:0]=in[31:24]; //分配连续的多个位
    wire [7:0]b2;
    assign b2[7:0]=in[23:16];
    wire [7:0]b3;
    assign b3[7:0]=in[15:8];
    wire [7:0]b4;
    assign b4[7:0]=in[7:0]; //调整顺序实现位反转
    assign out[7:0]=b1;
    assign out[15:8]=b2;
    assign out[23:16]=b3;
    assign out[31:24]=b4;
endmodule
```

**4.位运算符**
```verilog
module top_module( 
    input [2:0] a,
    input [2:0] b,
    output [2:0] out_or_bitwise,
    output out_or_logical,
    output [5:0] out_not
);
    assign out_or_bitwise=a|b;  //按位或
    assign out_or_logical=a||b; //逻辑或
    assign out_not[5:3]=~b; //按位非
    assign out_not[2:0]=~a;
endmodule
```

**5.四输入门**
```verilog
module top_module( 
    input [3:0] in,
    output out_and,
    output out_or,
    output out_xor
);
    assign out_and=in[3]&in[2]&in[1]&in[0]; 
    assign out_or=in[3]|in[2]|in[1]|in[0];
    assign out_xor=in[3]^in[2]^in[1]^in[0];
endmodule
```

**6.向量连接运算符**
```verilog
module top_module (
    input [4:0] a, b, c, d, e, f,
    output [7:0] w, x, y, z );
    assign z[1]=1; //赋布尔值
    assign z[0]=1;
    assign{w, x, y, z[7:2]}={a, b, c, d, e, f}; //连接多位并赋值
endmodule
```

**7.向量反转**
```verilog
module top_module( 
    input [7:0] in,
    output [7:0] out
);
    assign{out[7],out[6],out[5],out[4],out[3],out[2],out[1],out[0]}={in[0],in[1],in[2],in[3],in[4],in[5],in[6],in[7]}; //使用连接运算符改变顺序
endmodule
```

**8.复制操作符**
```verilog
module top_module (
    input [7:0] in,
    output [31:0] out );
    assign out={{24{in[7]}},in}; //重复24次in[7]并连接到前面
endmodule
```

**9.更多复制**
```verilog
module top_module (
    input a, b, c, d, e,
    output [24:0] out );//
    assign out[24:20]=~{a,a,a,a,a}^{a,b,c,d,e}; //每个信号与5个信号的一对一比较
    assign out[19:15]=~{b,b,b,b,b}^{a,b,c,d,e};
    assign out[14:10]=~{c,c,c,c,c}^{a,b,c,d,e};
    assign out[9:5]=~{d,d,d,d,d}^{a,b,c,d,e};
    assign out[4:0]=~{e,e,e,e,e}^{a,b,c,d,e};
endmodule
```

### 模块：层次结构

**1.模块**
```verilog
module top_module ( input a, input b, output out );
    mod_a instance1 ( a, b, out ); //创建名为instance1的mod_a并把top_module的端口依次连接到mod_a的三个端口
   endmodule
```

**2.按位置连接端口**
```verilog
module top_module ( 
    input a, 
    input b, 
    input c,
    input d,
    output out1,
    output out2
);
    mod_a instance1(out1,out2,a,b,c,d);
endmodule
```

**3.通过名称连接端口**
```verilog
module top_module ( 
    input a, 
    input b, 
    input c,
    input d,
    output out1,
    output out2
);
    mod_a instance2 ( .in1(a), .in2(b), .in3(c), .in4(d), .out1(out1) , .out2(out2)); //.后面为mod_a的端口名称，括号内为top_module的端口名称
endmodule
```

**4.三个模块**
```verilog
module top_module ( input clk, input d, output q );
    wire q1;
    my_dff instance1( clk, d,q1 ); //通过线连接不同自定义模块的输入和输出
    wire q2;
    my_dff instance2( clk,q1,q2);
    my_dff instance3( clk,q2,q);
endmodule
```

**5.模块和向量**
```verilog
module top_module ( 
    input clk, 
    input [7:0] d, 
    input [1:0] sel, 
    output reg [7:0] q 
);
    wire [7:0] q1;
    wire [7:0] q2;
    wire [7:0] q3;

    my_dff8 instance1(clk, d, q1);
    my_dff8 instance2(clk, q1, q2);
    my_dff8 instance3(clk, q2, q3);

    always @* //case要放到always内
        begin 
        case(sel) //在sel为相应的值的时候执行操作
            2'b00: q = d;
            2'b01: q = q1;
            2'b10: q = q2;
            2'b11: q = q3;             
        endcase
    end   
endmodule
```

**6.加法器1**
```verilog
module top_module(
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);
    wire cout; //连接进位引脚
    add16 instance1( a[15:0] , b[15:0], 0, sum[15:0],cout );
    add16 instance2( a[31:16] , b[31:16],cout, sum[31:16],0 );
endmodule
```

**7.加法器2**
```verilog
module add1 (input a, input b, input cin, output sum, output cout); //全加器
    assign sum = a ^ b ^ cin; //输出是输入的异或
    assign cout = a & b | a & cin | b & cin; //进位是输入的同或
endmodule

module top_module (
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);
    wire cout0;
    add16 instance1(a[15:0], b[15:0], 0, sum[15:0], cout0);
    add16 instance2(a[31:16], b[31:16], cout0, sum[31:16], 0);
endmodule
```

**8.带选择加法器**
```verilog
module top_module( 
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);
    wire cout0;
	add16 instance1(a[15:0], b[15:0], 0, sum[15:0], cout0);
    wire [15:0] sum_hi0;
    wire [15:0] sum_hi1;
    add16 instance2(a[31:16], b[31:16], 0, sum_hi0, 0);
    add16 instance3(a[31:16], b[31:16], 1, sum_hi1, 0);
    always @* //case要放到always内
        begin 
        case(cout0) //根据cout0的值选择合适的加法结果
            'b0: sum[31:16]=sum_hi0;
            'b1: sum[31:16]=sum_hi1;           
        endcase
    end  
endmodule
```

**9.加法器-减法器**
```verilog
module top_module(
    input [31:0] a,
    input [31:0] b,
    input sub,
    output [31:0] sum
);
    wire [31:0] b1;
    always @* //case要放到always内
        begin 
    	case(sub) //根据cout0的值选择是否反转
            'b0: b1=b;
            'b1: b1=~b+1; //反转并加1实现减法
        endcase
    end 
    wire cout; 
    add16 instance1( a[15:0] , b1[15:0], 0, sum[15:0],cout );
    add16 instance2( a[31:16] , b1[31:16],cout, sum[31:16],0 );
endmodule
```

### 程序

**1.alwsys块（组合）**
```verilog
module top_module(
    input a, 
    input b,
    output wire out_assign,
    output reg out_alwaysblock
);
    assign out_assign=a&b;
    always @* //case要放到always内
	    begin 
        case(a) 
            'b0: out_alwaysblock=0;
            'b1: out_alwaysblock=b; //与门a为1时输出等于b
        endcase
	end 

endmodule
```

**2.alwsys块（时钟）**
```verilog
module top_module(
    input clk,
    input a,
    input b,
    output wire out_assign,
    output reg out_always_comb,
    output reg out_always_ff   );
    assign out_assign=a^b; //赋值语句
    always @* //组合always
        begin 
            case(a) 
                'b0: out_always_comb=b;
                'b1: out_always_comb=!b; 
            endcase
    end 
    always @(posedge clk) //时钟always
        begin 
        case(a) 
            'b0: out_always_ff<=b; //时钟always使用非阻塞赋值
            'b1: out_always_ff<=!b; 
        endcase
    end 
endmodule
```

**3.if语句**
```verilog
module top_module(
    input a,
    input b,
    input sel_b1,
    input sel_b2,
    output wire out_assign,
    output reg out_always   ); 
	wire sel; 
    assign sel=sel_b1&sel_b2;
    assign out_assign=((sel&b)|(sel|a))&(!(sel&(!b)));
    always @(*) begin
        if (sel) begin //sel=1时选b，sel=0时选a
            out_always = b;
        end
        else begin
            out_always = a;
        end
    end   
endmodule
```
**4.if语句锁**
```verilog
module top_module (
    input      cpu_overheated,
    output reg shut_off_computer,
    input      arrived,
    input      gas_tank_empty,
    output reg keep_driving  ); 

    always @(*) begin
        if (cpu_overheated) begin
           shut_off_computer = 1;
        end
        else begin //用else设置默认情况
            shut_off_computer = 0;
        end
    end
    always @(*) begin
        if (~arrived) begin
           keep_driving = ~gas_tank_empty;
        end
        else if(arrived) begin
            keep_driving =0;
        end
        else begin
            keep_driving =0;
    	end
    end
endmodule
```

**5.case语句**
```verilog
module top_module ( 
    input [2:0] sel, 
    input [3:0] data0,
    input [3:0] data1,
    input [3:0] data2,
    input [3:0] data3,
    input [3:0] data4,
    input [3:0] data5,
    output reg [3:0] out   );
    always@(*) begin  
        case(sel) //根据sel的值给out赋值
            3'b000: out = data0;
			3'b001: out = data1;
            3'b010: out = data2;
			3'b011: out = data3;
            3'b100: out = data4;
			3'b101: out = data5;
            3'b110: out = 0;
			3'b111: out = 0;
        endcase
    end
endmodule
```

**6.优先编码器**
```verilog
module top_module (
    input [3:0] in,
    output reg [1:0] pos  );
    always@(*) begin  
        case(in) //输出值为输入值中最低的为1的位
            4'h0: pos = 2'b00;
            4'h1: pos = 2'b00;
            4'h2: pos = 2'b01;
            4'h3: pos = 2'b00;
            4'h4: pos = 2'b10;
            4'h5: pos = 2'b00;
            4'h6: pos = 2'b01;
            4'h7: pos = 2'b00;
            4'h8: pos = 2'b11;
            4'h9: pos = 2'b00;
            4'ha: pos = 2'b01;
            4'hb: pos = 2'b00;
            4'hc: pos = 2'b10;
            4'hd: pos = 2'b00;
            4'he: pos = 2'b01;
            4'hf: pos = 2'b00;
        endcase
	end
endmodule
```

**7.优先编码器带casez**
```verilog
module top_module (
    input [7:0] in,
    output reg [2:0] pos );
    always@(*) begin  
        casez(in[7:0]) //casez中用z设置不确定的值，用default设定其它情况
            8'bzzzzzzz1: pos = 3'b000;
            8'bzzzzzz10: pos = 3'b001;
            8'bzzzzz100: pos = 3'b010;
            8'bzzzz1000: pos = 3'b011;
            8'bzzz10000: pos = 3'b100;
            8'bzz100000: pos = 3'b101;
            8'bz1000000: pos = 3'b110;
            8'b10000000: pos = 3'b111;
            default: pos = 3'b000;
        endcase
    end
endmodule
```

**8.避免锁定**
```verilog
module top_module (
    input [15:0] scancode,
    output reg left,
    output reg down,
    output reg right,
    output reg up  ); 
    always @(*) begin
    up = 1'b0; down = 1'b0; left = 1'b0; right = 1'b0; //确保初始输出为0
        case (scancode)
            16'he06b:	left=1;  //左箭头
            16'he072:	down=1;   //下箭头
            16'he074:	right=1;   //右箭头
            16'he075:	up=1;  //上箭头
        endcase
	end
endmodule
```
### 更多特性

**1.条件三元运算符**
```verilog
