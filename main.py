import RSA
file=open('trailMessage.txt','r')
messageFromFile = file.read()
file.close()

MessageAscii=rsa.getASCII(messageFromFile)
p=rsa.generatePrime()
q=rsa.generatePrime()
n=p*q
phi=(p-1)*(q-1)
e=rsa.publicKey(phi)
d=rsa.privateKey(phi,e)
EncryptedMessageAscii=rsa.Encrypt(n,e,MessageAscii)
DecryptedMessageAscii=rsa.Decrypt(n,d,EncryptedMessageAscii)
message=rsa.getTxtFromAscii(DecryptedMessageAscii)
file=open('decryptedMessage.txt','w')
file.write(message)
file.close()
