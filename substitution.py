class Cypher:

    def __init__(self, message, key):
        """Initializes the Cypher, storing the original message and key"""
        self.message = message.replace(' ','').lower()
        self.key = key
        self.LetNum = {k:v for k,v in zip([char for char in "abcdefghijklmnopqrstuvwxyz"],range(26))}
        self.NumLet = {k:v for k,v in zip(range(26),[char for char in "abcdefghijklmnopqrstuvwxyz"])}
        self.encryption = None
        self.decryption = None

    def toNum(self,s):
        return [self.LetNum[char] for char in s]

    def toString(self,l):
        s = [self.NumLet[i] for i in l]
        final = ''.join(s)
        return final.upper()
class Encrypt(Cypher):

    def encrypt(self):
        self.encryption = self.toString([(i + self.key) % 26 for i in self.toNum(self.message)])
    def __repr__(self):
        return ' '.join([self.encryption[i:i+5] for i in range(0, len(self.encryption), 5)])


class Decrypt(Cypher):

    def decrypt(self):
        self.decryption = self.toString([(i - self.key) % 26 for i in self.toNum(self.message)])

    def __repr__(self):
        return self.decryption
