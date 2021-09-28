from RSA import keys
file=open('trailMessage.txt','r')
messageFromFile = file.read()
file.close()
key=keys()

MessageAscii=keys.getASCII(messageFromFile)

EncryptedMessageAscii=key.Encrypt(MessageAscii)
DecryptedMessage=key.Decrypt(EncryptedMessageAscii)
file=open('decryptedMessage.txt','w')
file.write(DecryptedMessage)
file.close()
