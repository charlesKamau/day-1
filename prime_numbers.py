#This function outputs the prime numbers between 0 and  N
def primeFun():
    list=[]
    num=int(input("Input the value of N\n"))
    for i in range(0,num):
        if i%2==0:
            list.append(i)
            i+=1
        else:
          i+=1
    print(list)
print(primeFun())

