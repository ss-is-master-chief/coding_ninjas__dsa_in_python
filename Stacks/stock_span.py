def stockSpan(rates,n):

    stockspan = []
    stack = [] # Creating an empty stack

    stockspan.append(1)
    stack.append(0)
    for i in range(1, n):

      while rates[i] > rates[stack[-1]]:
        stack.pop()

        if len(stack) is 0:
          break
      
      if len(stack) > 0:
          stockspan.append(i - stack[-1])
      else:
          stockspan.append(i + 1) 

      stack.append(i)
    
    return stockspan


n = int(input())
price = [int(ele) for ele in input().split()]
# n = price[0]
# price = price[1:]
spans = stockSpan(price,n)
for ele in spans:
    print(ele,end= ' ')