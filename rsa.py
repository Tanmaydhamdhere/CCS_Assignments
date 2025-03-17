import random;
import math;

p = int(input("Enter  p: "))
q = int(input("Enter  q: "))
for num in (p, q):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                exit() 
            else:
                continue   
    else:
        print(f"{num} is not a prime number.")
        
        exit()

print(f"Both numbers are prime.")

n = p * q
print("n : ",n)
phi_n = (p - 1) * (q - 1)
print("phin_n :",phi_n)


def select_e(phi_n):
    
    while True:
        e = random.randint(2, phi_n)  
        if math.gcd(e, phi_n) == 1:  
            return e

e = select_e(phi_n)



print("e is :",e)

m=int(input("Enter m :"))


d=pow(e,-1,phi_n)
print("d is :",d)

print(f"Public Key (e,n): {e,n}")
print(f"Private Key (d,n): {d,n}")
C=pow(m,e,n)
print("C is :",C)

M=pow(C,d,n)
print("M is :",M)
 