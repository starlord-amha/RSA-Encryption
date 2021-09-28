def Encrypt(n,e,message):
    known={}
    cipher=[]
    for char in message:
        if char not in known:
            msg=pow(char,e,n)
            known[char]=msg
            cipher.append(msg)
        else:
            cipher.append(known[char])
    return cipher
def Decrypt(n,d,cipher):
    known={}
    message=[]
    for char in cipher:
        if char not in known:
            msg=pow(char,d,n)
            message.append(msg)
            known[char]=msg
        else:
            message.append(known[char])
    return message
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
def publicKey(n):
    e=random.randint(2,n)
    while gcd(e,n) != 1:
        e-=2
    return e
def privateKey(phi,e,s0=1,s1=0,t0=0,t1=1):
    if phi % e == 0:
        return t1
    else:
        q=phi//e
        s=s0 - q*s1
        t=t0 - q*t1
        return privateKey(e,phi%e,s1,s,t1,t)
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
def generatePrime():
    a=random.getrandbits(100)
    if a%2 == 0:
        a+=1
    b=random.randint(2,a-2)
    while pow(b,a-1,a) != 1 :
        a+=2
        b=random.randint(2,a-2)
    return a
