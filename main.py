from cipher import CaesarCipher


cifra = CaesarCipher()
cifra.crypting('IGOR')
cifra.descrypting('JHPS')
print(cifra.crypt)
print(cifra.descrypt)