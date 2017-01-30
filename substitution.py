class Cypher:

    def __init__(self, message, key):
        self.message = message.replace(' ','').lower()
        self.key = key
        self.LetNum = {k:v for k,v in zip([char for char in "abcdefghijklmnopqrstuvwxyz"],range(26))}
        self.NumLet = {k:v for k,v in zip(range(26),[char for char in "abcdefghijklmnopqrstuvwxyz"])}
        self.encryption = None

    def toNum(self,s):
        return [self.LetNum[char] for char in s]

    def toString(self,l):
        s = [self.NumLet[i] for i in l]
        final = ''.join(s)
        return final.upper()
class Encrypt(Cypher):

    def __init__(self):
        self.encryption = self.toString([(i + self.key) % 26 for i in self.toNum(self.message)])
        
    def __repr__(self):

class Decrypt(Cypher):

    def __init__(self):
        self.decryption = self.toString([(i - self.key) % 26 for i in self.toNum(self.message)])
