import re 

  

operators_key = ['=', '+', '-', '/', '*', '<', '>'] 

  

identifier_key = ['a-z', 'A-Z', '0-9'] 

  

punctuator_key = ['(', ')', '{', '}'] 

  

  

a=input("Enter the expression: ") 

print("\n") 

  

count=0 

tokens =re.split('\s' , a) 

  

print("The Tokens Of The Expression: " , tokens) 

  

for token in tokens: 

        if re.search('{list}'.format(list=operators_key),token): 

            print("OPERATOR: ", token) 

             

        if re.search('{list}'.format(list=identifier_key),token) : 

            print ( "IDENTIFIER: " , token) 

             

        if re.search('{list}'.format(list=punctuator_key),token) : 

            print ( "PUNCTUATOR: " , token) 

  

print("\n EXECUTED SUCCESSFULLY !!") 
