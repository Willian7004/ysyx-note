这是“数字电路基础实验”部分中的Verilog部分的内容。原本考虑学习多语言可能有开发习惯冲突，但群友还是建议同时掌握Verilog和Chisel。

以前在runoob上看过一点Verilog，但由于缺少说明，无法理解代码含义，后来就没有看了。本次课程中的hdlbits上虽然没有直接给出例程，但具有较为详细的说明，通常不需要另外查询资料就能完成。以下网站上的顺序记录各习题情况，也作为对知识点的记录。各部分均使用译文中的名称。

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


