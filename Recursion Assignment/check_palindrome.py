## Read input as specified in the question.
## Print output as specified in the question.
def checkPalindrome(string):
  if(len(string)==0 or len(string)==1):
    print("true")
    return
  if(string[0]==string[-1]):
    checkPalindrome(string[1:-1])
  else:
    print("false")
    return

string = input()
checkPalindrome(string)