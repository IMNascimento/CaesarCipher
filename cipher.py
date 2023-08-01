class CaesarCipher:
    crypt =''
    descrypt = ''
    def __init__(self):
        pass

    def crypting(self, msg:str)->None:
        for char in msg:
            if not char.isalpha():
                continue
            char = char.upper()
            code = ord(char) + 1
            if code > ord('Z'):
                code = ord('A')
            self.crypt += chr(code)

    def descrypting(self, msg:str)->None:            
        for char in msg:
            if not char.isalpha():
                continue
            char = char.upper()
            code = ord(char) - 1
            if code < ord('A'):
                code = ord('Z')
            self.descrypt += chr(code)
            
    
    
