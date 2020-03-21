def checkRedundant(Str):
#### Implement Your Code Here
    st = []  

    for ch in Str:  
  
        if (ch == ')'):  
            top = st[-1]  
            st.pop()  
  
            flag = True
  
            while (top != '('):  
  
                if (top == '+' or top == '-' or
                    top == '*' or top == '/'):  
                    flag = False
  
                top = st[-1]  
                st.pop() 
  
            if (flag == True): 
                return True
  
        else: 
            st.append(ch)   
                          
    return False
    

string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')