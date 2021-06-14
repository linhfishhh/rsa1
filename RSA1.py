import math
import random

#chọn p & q là 2 số nguyên tố ngẫu nhiên
#p*q=n
#(p-1)(q-1)=Q(n);
#e=2^16+1=65537
#chọn d 
def main():
    p,q,n,e,d = gen_keys()
    s = "p = " + str(p) + "\n"
    t = "q = " + str(q) + "\n"
    x = "n = " + str(n) + "\n"
    y = "e = " + str(e) + "\n"
    z = "d = " + str(d) + "\n"
    pub = "Public key( " + str(n) + " , " + str(e) + " )\n"
    pri = "Private key( " + str(n) + " , " + str(d) + " )\n"
    print(pub)
    print(pri)
    file = open("gen_key.txt", "w")
    file.write(pub)
    file.write(pri)
    file.write(s)
    file.write(t)
    file.write(x)
    file.write(y)
    file.write(z)
    file.close()

def get_prime():
	#chọn ngẫu nhiên 2 số trong khoảng từ 1000-10000
    prime = []
    for num in range(1000, 10000 + 1):
        # check xem phai la so nguyen to hay khong
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime.append(num)
    y = len(prime)
    x = random.randint(1, y-1)
    return prime[x]

def gen_keys():
    p = get_prime()
    q = get_prime()
    n = p * q
    m = (p - 1) * (q - 1)
    e = 65537
    d = get_d(e, m)
    while d < 0:
        d += m
    return [p, q, n, e, d]
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def get_d(e, m):
    x = lasty = 0
    lastx = y = 1
    while m != 0:
        q = e // m
        e, m = m, e % m
        x, lastx = lastx - q*x, x
        y, lasty = lasty - q*y, y
    return lastx

if __name__ == "__main__":
    main()