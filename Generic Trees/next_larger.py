import queue

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def nextLargest(tree, n):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if(tree==None):
        return
    
    q = queue.Queue()
    q.put(tree)
    lower = float(n)
    upper_value = float("inf")
    
    while(q.empty()==False):
        node = q.get()
        for child in node.children:
            q.put(child)
            if lower<child.data<upper_value:
                upper_value = child.data
                upper = child
    return upper

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
n = int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(nextLargest(tree, n).data)
