## Read input as specified in the question.
## Print output as specified in the question.
def stringToInteger(string):
  if(len(string)==1):
    return int(string[0])
  return int(string[0])*(10**(len(string)-1)) + stringToInteger(string[1:])

n = input()
val = stringToInteger(n)
print(val)