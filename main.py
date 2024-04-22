from cipher import CaesarCipher


cifra = CaesarCipher()
#cifra.crypting('IGOR')
#cifra.descrypting('JHPS')
frase = input("digite sua mensagem:")
cifra.crypting(frase)
cifra.descrypting(cifra.crypt)
print(cifra.crypt)
#print(cifra.descrypt)