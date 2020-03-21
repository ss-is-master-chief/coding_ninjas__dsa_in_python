## Read input as specified in the question.
## Print output as specified in the question.
#Write your code here

def countMinReversals(expr):  
  
    length = len(expr) 

    if length % 2: 
        return -1
  
    # To store number of reversals required. 
    ans = 0

    open = 0

    close = 0
  
    for i in range(0, length):  

        if expr[i] == "{": 
            open += 1

        else: 
            if not open: 
                close += 1
            else: 
                open -= 1
          
    ans = (close // 2) + (open // 2) 

    close %= 2
    open %= 2
      
    if close > 0: 
        ans += 2
  
    return ans 
  
# Driver Code  
if __name__ == '__main__':  
  
    expr = input()
    print(countMinReversals(expr))  