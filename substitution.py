class Cypher:

    def __init__(self, message, key):
        self.message = message
        self.key = key
        self.d = {k:v for k,v in zip([char for char in "abcdefghijklmnopqrstuvwxyz"],range(26))}
