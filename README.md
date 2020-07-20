# Recursive-Descent-Parser
This interactive script of python is based on the following version of the grammar: 

0     <statement> → table | show <exp>{<exp>} | <id> = <exp> 
1     <exp> → <term>{+<term> | -<term>} 
2     <term> → <factor>{*<factor> | /factor>} 
3     <factor> → (<exp>) | pi | - | <func>(<exp>) | <atomic> | <extra>(<exp>) 
4     <func> → sin | cos | tan | sqrt  
5     <extra> → fact | log | floor | ceil | trunc

A table is a dictionary which will store the varaibles and its value, whenever that variable is called in the output, it will give the value associated with it. The best use of this feature is you can use that value as many times as possible without having to write the value again and again.

An expression is something which is a mathematical expression, such as "10 + 15 * sin(180)", however an expression should contain a prefix word called "show", so that the output of the expression is visible once it is done.

There are some in-built python functionality used from the math library like calculating sin, cos, tan, log, etc. 
