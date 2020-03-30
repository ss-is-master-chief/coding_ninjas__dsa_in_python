# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    # Please add your code here
    if(len(string) in [0,1]):
        return string
    if(string[0]==string[1]):
        return removeConsecutiveDuplicates(string[1:])
    else:
        return string[0] + removeConsecutiveDuplicates(string[1:])

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
