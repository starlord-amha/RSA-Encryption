from RSA import keys
file=open('trailMessage.txt','r')
messageFromFile = file.read()
file.close()
key=keys()

MessageAscii=keys.getASCII(messageFromFile)

EncryptedMessageAscii=key.Encrypt(MessageAscii)
DecryptedMessageAscii=key.Decrypt(EncryptedMessageAscii)
message=keys.getTxtFromAscii(DecryptedMessageAscii)
file=open('decryptedMessage.txt','w')
file.write(message)
file.close()
