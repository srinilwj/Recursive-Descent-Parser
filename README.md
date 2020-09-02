# Recursive-Descent-Parser
This python script consist of a lot of functions which are recursively called as per the rules described at the start of the program.
This is basically a parser which reads the input from the user and follows some pre-defined rules to produce some output.

For eg:
The user input is what follows on a line after the => prompt:

=> x = 2
Done
=> y = 3
Done
=> show x, y, 1 + sqrt(2*x*y  -  4)
value: 2.0      3.0      3.8284271247461903
Done
=> z = sqrt(2*x*y  +  4)
Done
=> table

Symbol Table
====================
x           2.0
y           3.0
z           4.0

Done
=> show x + y*sin(pi*sqrt(z)/4)
value: 5.0
Done

=> x = (2 - 3

missing   )
Parse Error
=>
