## Read input as specified in the question.
## Print output as specified in the question.
def pairStar(string):
  if(len(string)==0 or len(string)==1):
    return string
  if(string[0]==string[1]):
    return string[0] + "*" + pairStar(string[1:])
  else:
    return string[0] + pairStar(string[1:])


string = input()
string = pairStar(string)
print(string)