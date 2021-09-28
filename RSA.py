import random
class keys:
    def __init__(self):
        self.p=keys.generatePrime()
        self.q=keys.generatePrime()
        self.n=self.p*self.q
        self.phi=(self.p-1)*(self.q-1)
        self.e=self.publicKey(self.phi)
        self.d=self.privateKey(self.phi,self.e)
    def Encrypt(self,message):
        known={}
        cipher=[]
        for char in message:
            if char not in known:
                msg=pow(char,self.e,self.n)
                known[char]=msg
                cipher.append(msg)
            else:
                cipher.append(known[char])
        return cipher
    def Decrypt(self,cipher):
        known={}
        message=[]
        for char in cipher:
            if char not in known:
                msg=pow(char,self.d,self.n)
                message.append(msg)
                known[char]=msg
            else:
                message.append(known[char])
        return message
    @staticmethod
    def gcd(a,b):
        if b == 0:
            return a
        else:
            return keys.gcd(b,a%b)
    def publicKey(self):
        e=random.randint(2,self.phi)
        while keys.gcd(e,self.phi) != 1:
            e=random.randint(2,self.phi)
        return e
    def privateKey(self,phi,e,s0=1,s1=0,t0=0,t1=1):
        if phi % e == 0:
            return t1
        else:
            q=phi//e
            s=s0 - q*s1
            t=t0 - q*t1
            return self.privateKey(e,phi%e,s1,s,t1,t)
    @staticmethod
    def getASCII(File):
        knownValues={}
        asciiFile=[]
        for x in File:
            if x not in knownValues:
                knownValues[x]=ord(x)
                asciiFile.append(knownValues[x])
            else:
                asciiFile.append(knownValues[x])
        return asciiFile
    @staticmethod
    def getTxtFromAscii(asciiFile):
        message=""
        for x in asciiFile:
            message+=chr(x)
        return message
    @staticmethod
    def generatePrime():
        prime=random.getrandbits(500)
        if prime%2 == 0:
            prime+=1
        b=random.randint(2,prime-2)
        while pow(b,prime-1,prime) != 1 :
            prime+=2
            b=random.randint(2,prime-2)
        return prime

