def get_pesa(A,R,T):

    calcloan=A*(R/100)*(T/12)
    return calcloan+A
A=2000
R=23
T=12

print(get_pesa(A,R,T))