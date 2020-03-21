
def checkBalanced(expr):
    valid_expr = ['{', '}', '[', ']', '(', ')']
    bracket_exp = [sym for sym in expr if sym in valid_expr]
    if(len(bracket_exp)==0):
        return True
    ls = [bracket_exp[0]]
    if(len(ls)==0):
        return False
    for i in range(1, len(bracket_exp)):
        if(bracket_exp[i]=="{" or bracket_exp[i]=="(" or bracket_exp[i]=="["):
            ls.append(bracket_exp[i])
        else:
            try:
                if(bracket_exp[i]=="]" and ls[-1]=="["):
                    ls.pop()
                elif(bracket_exp[i]=="}" and ls[-1]=="{"):
                    ls.pop()
                elif(bracket_exp[i]==")" and ls[-1]=="("):
                    ls.pop()
            except:
                return False
    if(len(ls)==0):
        return True
    else:
        return False
            
    
### Implement your code here

exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')

