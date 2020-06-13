from decimal import Decimal 
import random

class RSA:
    def __init__(self, anchor,accuracy, text):
        self.anchor = anchor
        self.accuracy = accuracy
        self.text = text
    def gcd(self,a,b): 
        if b==0: 
            return a 
        else: 
            return self.gcd(b,a%b) 
    
    def test(self,n):
        k = 0
        m = n - 1 
        q = 1
        while(m%2 == 0):
            k += 1
            m = int(m/2)
        
        q = m
        flag = True
        i = 0
        random_numbers = random.sample(range(n),self.accuracy)
        while flag:
            a = random_numbers[i]
            if (a**q)%n == 1:
                flag = True
            elif k == 0 and (a**q)%n != n-1:
                flag = False
            else:
                t = 0
                for j in range(k):
                    if (a**(2**j*q) % n) != n-1:
                        t += 1
                if(t==k):
                    flag = False
            i += 1
            if(i>=len(random_numbers)): 
                break
        return flag
            

        
    def find_prime(self,anchor):
        i = 0
        p = []
        while True:
            if  self.test(anchor):
                p.append(anchor)
                anchor += 1
                i += 1
                if(i==2):
                    return p
            else:
                anchor += 1
    def create_key(self):
        self.p, self.q = self.find_prime(self.anchor)
        self.n = self.p*self.q 
        t = (self.p-1)*(self.q-1) 
        self.e, self.d = 0, 0
        
        for i in range(2,t): 
            if self.gcd(i,t)== 1: 
                self.e = i
            
                break
        for i in range(1,self.e+1): 
            x = 1 + i*t 
            if x % self.e == 0: 
                self.d = int(x/self.e) 
                break
    def encrypt(self,pk,plaintext):
        key, n = pk
        cipher = [(ord(char) ** key) % n for char in plaintext]
        return cipher

    def decrypt(self,pk,ciphertext):
        key, n = pk
        plain = [chr((dec ** key) % n) for dec in ciphertext]
        return ''.join(plain)