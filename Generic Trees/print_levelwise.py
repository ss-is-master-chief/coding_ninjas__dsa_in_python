import queue

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def printLevelWiseTree(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    q = queue.Queue()
    
    if tree == None:
        return
    q.put(tree)
    
    while (not(q.empty())):
        current_node = q.get()
        print(str(current_node)+":", end = "")
        i = 0
        for child in current_node.children:
            q.put(child)
            if(i<len(current_node.children)-1):
                print(child.data, end = ",")
            else:
                print(child.data, end = "")
            i += 1
        print()

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
printLevelWiseTree(tree)
