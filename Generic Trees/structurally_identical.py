import queue 
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def isIdentical(tree1, tree2):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree1 == None and tree2 == None:
        return True
    
    if tree1 == None or tree2 == None:
        return False
    
    q1 = queue.Queue()
    q2 = queue.Queue()
    
    q1.put(tree1)
    q2.put(tree2)
     
    l1 = []
    l2 = []
    
    while(not(q1.empty())):
        curr = q1.get()
        l1.append(curr)
        for child in curr.children:
            l1.append(child)
            q1.put(child)            
    
    while(not(q2.empty())):
        curr = q2.get()
        l2.append(curr)
        for child in curr.children:
            l2.append(child)
            q2.put(child)
    
    if len(l1) == len(l2):
        for i in range(len(l1)):
            if l1[i].data != l2[i].data:
                return False
        return True
    else:
        return False
            

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr1 = list(int(x) for x in input().strip().split(' '))
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in input().strip().split(' '))
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')
