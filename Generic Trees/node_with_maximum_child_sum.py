import queue

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def maxSumNode(tree):
    # Return the node and its sum
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if(tree==None):
        return None
    q = queue.Queue()
    q.put(tree)
    max_sum = tree.data
    return_node = tree
    while(q.empty()!=True):
        node = q.get()
        init_sum = node.data
        for child in node.children:
            q.put(child)
            init_sum += child.data
        if(init_sum > max_sum):
            max_sum = init_sum
            return_node = node
    return return_node, max_sum
            
            
            

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
temp, tempSum = maxSumNode(tree)
print(temp.data)
