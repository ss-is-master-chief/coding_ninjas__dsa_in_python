
import queue
def reverseQueue(q1):
#### Implement Your Code Here
    Stack = []  
    while (not q1.empty()):  
        Stack.append(q1.queue[0])  
        q1.get() 
    while (len(Stack) != 0):  
        q1.put(Stack[-1])  
        Stack.pop() 
    

from sys import setrecursionlimit
setrecursionlimit(11000)
li = [int(ele) for ele in (input().split()[1:])]
q1 = queue.Queue()
for ele in li:
    q1.put(ele)
reverseQueue(q1)
while(q1.empty() is False):
    print(q1.get(),end= ' ')