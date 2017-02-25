list=[1]
result=[]
last=1
count=1
a=1
while(a>=0):
    print("수열의 몇번째 행을 원하십니까?(음수를 입력하면 종료)")
    a=int(input())
    for j in range(0,a):
        size=len(list)
        for i in range(0,size):
            last=list[i]
            if (i==(size-1))or(list[i+1]!=last):
                result.append(list[i])
                result.append(count)
                count=1
            else:
                count=count+1
        else:
            last=1
        list=result
        result=[]
    print(list)
    list=[1]
else:
    print('\n')
