def prime_num(n):
    list_prime=[]
    for num in range(0, n+ 1):#

        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                list_prime.append(num)
    print(list_prime)
user_input=int(input("Input the value of the upper bound\n"))
print(prime_num(user_input))