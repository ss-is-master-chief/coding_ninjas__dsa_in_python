## Read input as specified in the question.
## Print output as specified in the question.

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def heightOfTree(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if(tree==None):
        return 0
    height = 1
    height_sub = [heightOfTree(child) for child in tree.children]
    if(height_sub!=[]):
        height = 1 + max(height_sub)
    return height
        
    

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
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(heightOfTree(tree))
