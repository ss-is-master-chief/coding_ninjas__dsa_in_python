def pairSum(arr, x):
    # Please add your code here
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == x:
                if arr[i] < arr[j]:
                    print(arr[i],end =' ')
                    print(arr[j])
                    
                else:
                    print(arr[j],end =' ')
                    print(arr[i])

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
pairSum(arr, sum)
