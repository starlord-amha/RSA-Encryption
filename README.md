# RSA-Encryption
The implementation of RSA Encryption Algorithm using Python

The library contains the necessary functions to implement RSA Encryption.
generatePrime: this function uses fermat's little theorem to generate 1024 bit prime numbers.
getASCII: A function that returns a list of ascii values of characters in a string passed as arguments.
publicKey: A function that generates the public key(e) used for encryption in the Encrypt function.
privateKey: A function that uses Euclid's Extended Algorithm to generate the private key(d).
Encrypt: A function that uses the public key generated to encrypt a file and return the cipher as a list ascii value.
Decrypt: A function that uses the private key generated to Decrypt a file and return the message as a list of ascii value.
gcd: A function used in other functions of the library to calculate the gcd of two numbers.
