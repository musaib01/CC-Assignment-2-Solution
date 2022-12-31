import ast 

  

expression = '2 + 4 * 9' 

  

code = ast.parse(expression, mode = 'eval') 

  

print(eval(compile(code, '', mode = 'eval'))) 

  

print(ast.dump(code)) 
