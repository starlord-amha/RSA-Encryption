# RSA-Encryption
The implementation of RSA Encryption Algorithm using Python





The RSA library contains the necessary methods to implement RSA Encryption inside the keys class.

generatePrime: A static method uses fermat's little theorem to generate 1024 bit prime numbers.

getASCII: A static method that returns a list of ascii values of characters in a string passed as arguments.

publicKey: A method that generates the public key(e) used for encryption in the Encrypt method.

privateKey: A method that uses Euclid's Extended Algorithm to generate the private key(d).

Encrypt: A method that uses the public key of the object to encrypt a file and return the cipher as a list ascii value.

Decrypt: A method that uses the private key of the object to Decrypt a file and returns the message.

gcd: A static method used in other methods of the class to calculate the gcd of two numbers.

The main.py file contains a program that implement the RSA library to read and encrypt a message from trailMessage.txt file 
and decrypt the message and write the decrypted message to the file decryptedMessage.txt
