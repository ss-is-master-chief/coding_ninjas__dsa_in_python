import queue
class StackUsingQueues:
    
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.curr_size = 0
        
        
    def push(self,data):
        self.curr_size += 1 
        self.q2.put(data)  
  
        while (not self.q1.empty()): 
            self.q2.put(self.q1.queue[0])  
            self.q1.get() 
  
        self.q = self.q1  
        self.q1 = self.q2  
        self.q2 = self.q 
        
       
    def pop(self):
        if (self.q1.empty()):  
            return 
        data = self.q1.queue[0]
        self.q1.get()  
        self.curr_size -= 1
        return data
    
    def top(self):
        if (self.q1.empty()): 
            return 
        return self.q1.queue[0] 
        
    def getSize(self):
        return self.curr_size 
        
    
s = StackUsingQueues()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i+1])
        i+=1
    elif choice == 2:
        ans = s.pop()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        j = 0
        Stack = []
        while(j<s.getSize()):
            Stack.append(s.q1.queue[0])
            s.q1.get()
            j += 1
        while j >0:
            print(Stack[-1], end=' ')
            Stack = Stack[:-1]
            j -= 1
            
    i+=1






