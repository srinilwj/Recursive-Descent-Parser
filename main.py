'''
The interactive session above is based on the following expanded version of the grammar:

0     <statement> → table | show <exp>{,<exp>} | <id> = <exp>
1     <exp> → <term>{+<term> | -<term>}
2     <term> → <factor>{*<factor> | /<factor>}
3     <factor> → (<exp>) | pi | - | <func>(<exp>) | <atomic> | <extra>(<exp>)
4     <func> → sin | cos | tan | sqrt 
5     <extra> → fact | log | floor | ceil | trunc

I have added 'extra()' function, which consists of methods like factorial, log (to the base 2), floor value, ceiling value and truncate (rounds towards zero regardless of whether the number is positive or negative)
The symbol table also accepts negative values and can be used in calculations 
'''


import math


class ParseError(Exception): pass

#============================================================================
# FRONT END PARSER
#============================================================================

i = 0 # keeps track of what character we are currently reading.
var_table = {}
display = {}

#============================================================================
# Parse a Statement: <statement> → table | show <exp>{,<exp>} | <id> = <exp>
#============================================================================

def statement():
    global i
    a = 0
    if w[i] == 'table':
        
        print('\nSymbol Table\n====================')
        for v in var_table:
          print(v, '\t', var_table[v])
    elif w[i] == 'show':
        i += 1
        value = exp()
        
        if value in var_table:
            display[a] = var_table[value]
            a += 1
        else:
            display[a] = value
            a += 1
        while w[i] == ',':
            i += 1
            value = exp() 
            if value in var_table:
              display[a] = var_table[value]
              a += 1
            else:
              display[a] = value
              a += 1 
        print('\nValue: ', end = '')
        for j in range(a):
          print(display[j],'  ', end = '')
    
    
    else:
        id = w[i]
        if w[i+1] == '=':
            i += 2
            if w[i] == '\'':
              value = exp()
              var_table[id] = value
            else:
              if w[i] in var_table:
                w[i] = var_table[w[i]]
              elif w[i] in {'sin', 'cos', 'tan', 'sqrt', '(', 'pi', 'fact', 'log', 'floor', 'ceil', 'trunc'}:
                w[i] = w[i]
              else:
                try:
                  if w[i] == '-':                    
                    float(w[i] and w[i+1])
                  else:
                    float(w[i])
                except:
                  print('missing \' \'', w[i])
                  raise ParseError
              value = exp()
              var_table[id] = value
        else:
          print('\'=\' not found')
          raise ParseError
    
#============================================================================
#Parse an expression: <exp> → <term>{+<term> | -<term>}
#============================================================================
def exp():
    global i, err

    value = term()
    while True:
        if w[i] == '+':
            i += 1
            value = binary_op('+', value, term())
        elif w[i] == '-':
            i += 1
            value = binary_op('-', value, term())
        else:
            break

    return value
#============================================================================
# Parse a Term: <term> → <factor>{+<factor> | -<factor>}
#============================================================================
def term():
    global i, err

    value = factor()
    while True:
        if w[i] == '*':
            i += 1
            value = binary_op('*', value, factor())
        elif w[i] == '/':
            i += 1
            value = binary_op('/', value, factor())
        else:
            break

    return value

#============================================================================
# Parse a Factor: <factor> → (<exp>) | pi | - | <func>(<exp>) | <atomic>
#============================================================================       
def factor():
    global i, err
    value = None
    if w[i] == '(':
        i += 1          # read the next character
        value = exp()
        if w[i] == ')':
            i += 1
            return value
        else:
            print('missing )')
            raise ParseError
    elif w[i] == 'pi':
        i += 1
        return math.pi
    elif w[i] == '-':
        i += 1
        return -factor()
    elif w[i] == 'sin':
        #i +=1
        value = func()
    elif w[i] == 'cos':
        #i +=1
        value = func()
    elif w[i] == 'tan':
        #i +=1
        value = func()
    elif w[i] == 'sqrt':
        #i +=1
        value = func()
    elif w[i] == 'fact':
        value = extra()
    elif w[i] == 'log':
        value = extra()
    elif w[i] == 'floor':
        value = extra()
    elif w[i] == 'ceil':
        value = extra()
    elif w[i] == 'trunc':
        value = extra()
    else:
        
        value = atomic(w[i])
        i += 1          # read the next character

    return value

#============================================================================
# Parse a function: <func> → sin | cos | tan | sqrt
#============================================================================

def func():
    global i, err
    
    if w[i] == 'sin':
        i += 1
        if w[i] == '(':
            i += 1
            if w[i] in var_table:
                w[i] = var_table[w[i]]
                sin_val = (math.sin(w[i]))
                i += 1
                if w[i] == ')':
                  i += 1
                  return sin_val                
                else:
                  print('missing )')
                  raise ParseError
            else:
              value = exp()
              if w[i] == ')':
                i += 1              
                sin_val1 = (math.sin(value))             
                return sin_val1                            
              else:
                print('missing )')
                raise ParseError
     
    elif w[i] == 'cos':
        i += 1
        if w[i] == '(':
            i += 1
            if w[i] in var_table:
                w[i] = var_table[w[i]]
                cos_val = (math.cos(w[i]))
                i += 1
                if w[i] == ')':
                  i += 1
                  return cos_val
                else:
                  print('missing )')
                  raise ParseError
            else:
              value = exp()
              if w[i] == ')':
                i += 1
                cos_val1 = (math.cos(value))                
                return cos_val1
              else:
                print('missing )')
                raise ParseError      
    
    elif w[i] == 'tan':
        i += 1
        if w[i] == '(':
            i += 1
            if w[i] in var_table:
                w[i] = var_table[w[i]]
                tan_val = (math.tan(w[i]))
                i += 1
                if w[i] == ')':
                  i += 1
                  return tan_val
                else:
                  print('missing )')
                  raise ParseError
            else:
              value = exp()
              if w[i] == ')':
                i += 1
                tan_val1 = (math.tan(value))               
                return tan_val1
              else:
                print('missing )')
                raise ParseError  
       
    elif w[i] == 'sqrt':
        i += 1
        if w[i] == '(':
            i += 1
            if w[i] in var_table:
                w[i] = var_table[w[i]]
                sqrt_val = (math.sqrt(w[i]))
                i += 1
                if w[i] == ')':
                  i += 1
                  return sqrt_val
                else:
                  print('missing )')
                  raise ParseError
            else:
              value = exp()
              if w[i] == ')':
                i += 1
                sqrt_val1 = (math.sqrt(value))                
                return sqrt_val1
              else:
                print('missing )')
                raise ParseError          
    else:
        return value

#============================================================================
# Parse an extra: <extra> → factorial | log | floor | ceil
#============================================================================

def extra():
    global i, err

    if w[i] == 'fact':
        i += 1
        if w[i] == '(':
            i += 1
            if w[i] in var_table:
                w[i] = var_table[w[i]]
                fact_val = float(math.factorial(w[i]))
                i += 1
                if w[i] == ')':
                  i += 1
                  return fact_val
                else:
                  print('missing )')
                  raise ParseError
            else:
              value = exp()
              if w[i] == ')':
                i += 1
                fact_val1 = float(math.factorial(value))                
                return fact_val1
              else:
                print('missing )')
                raise ParseError

    elif w[i] == 'log':
        i += 1
        if w[i] == '(':
            i += 1
            if w[i] in var_table:
                w[i] = var_table[w[i]]
                log_val = float(math.log2(w[i])) # calculates log to the base 2 
                i += 1
                if w[i] == ')':
                  i += 1
                  return log_val
                else:
                  print('missing )')
                  raise ParseError
            else:
              value = exp()
              if w[i] == ')':
                i += 1
                log_val1 = float(math.log2(value))                
                return log_val1
              else:
                print('missing )')
                raise ParseError

    elif w[i] == 'floor':
        i += 1
        if w[i] == '(':
            i += 1
            if w[i] in var_table:
                w[i] = var_table[w[i]]
                floor_val = float(math.floor(w[i]))
                i += 1
                if w[i] == ')':
                  i += 1
                  return floor_val
                else:
                  print('missing )')
                  raise ParseError
            else:
              value = exp()
              if w[i] == ')':
                i += 1
                floor_val1 = float(math.floor(value))                
                return floor_val1
              else:
                print('missing )')
                raise ParseError

    elif w[i] == 'ceil':
        i += 1
        if w[i] == '(':
            i += 1
            if w[i] in var_table:
                w[i] = var_table[w[i]]
                ceil_val = float(math.ceil(w[i]))
                i += 1
                if w[i] == ')':
                  i += 1
                  return ceil_val
                else:
                  print('missing )')
                  raise ParseError
            else:
              value = exp()
              if w[i] == ')':
                i += 1
                ceil_val1 = float(math.ceil(value))                
                return ceil_val1
              else:
                print('missing )')
                raise ParseError
      
    elif w[i] == 'trunc':
        i += 1
        if w[i] == '(':
            i += 1
            if w[i] in var_table:
                w[i] = var_table[w[i]]
                trunc_val = float(math.trunc(w[i]))
                i += 1
                if w[i] == ')':
                  i += 1
                  return trunc_val
                else:
                  print('missing )')
                  raise ParseError
            else:
              value = exp()
              if w[i] == ')':
                i += 1
                trunc_val1 = float(math.trunc(value))                
                return trunc_val1
              else:
                print('missing )')
                raise ParseError

    else:
        return value

#============================================================================
# BACK END PARSER (ACTION RULES)
#============================================================================

def binary_op(op, lhs, rhs):
  if lhs in var_table:
      lhs = var_table[lhs]
  if rhs in var_table:
      rhs = var_table[rhs]

  try:
    if op == '+':
        return lhs + rhs
    elif op == '-':
        return lhs - rhs
    elif op == '*':
        return lhs * rhs
    elif op == '/':
        return lhs / rhs
    else:
        return None 
  except:
      print('value cant be calculated', lhs, rhs)
      raise ParseError
  return

def atomic(x):
  try:
    return float(x)
  except:
    return x



w = input('\n=> ')
while w != '':
  i = 0
#============================================================================
# Split string into token list.
#============================================================================
  for c in '()+-*/,=':
    w = w.replace(c, ' '+c+' ')
  w = w.split()
  w.append('$') # EOF marker

  #print('\nToken Stream:\n')
  #for t in w: print(t, end = '  ')
  #print('\n\nEnd Token Stream\n')


  try:
    
    statement()
    print('\nDone')
  except:
    print('parse error')
  print()
  #if w[i] != '$': print('Syntax error: all input not parsed')
  #for c in w[:i]: print(c, end = '')
  #print(' | ', end = '')
  #for c in w[i:]: print(c, end = '')
  #print()
#print(w[:i], '|', w[i:])

  w = input('\n=> ')
