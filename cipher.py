class CaesarCipher:
    crypt =''
    descrypt = ''
    def __init__(self):
        pass

    def crypting(self, msg:str)->str:
        for char in text:
            if not char.isalpha():
                continue
            char = char.upper()
            code = ord(char) + 1
            if code > ord('Z'):
                code = ord('A')
            self.crypt += chr(code)

    def decrypting(self, msg:str)->str:            
        for char in cipher:
            if not char.isalpha():
                continue
            char = char.upper()
            code = ord(char) - 1
            if code < ord('A'):
                code = ord('Z')
            self.descrypt += chr(code)
    
    
