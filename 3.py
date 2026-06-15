class String:
    def __init__(self, text):
        self.text = text
    def to_lower(self):
        result = ""
        for harf in self.text:
            if harf >= "A" and harf <= "Z":
                result += chr(ord(harf)+32)
            else:
                result += harf
        return result
    def to_upper(self):
        result = ""
        for harf in self.text:
            if harf >= "a" and harf <= "z":
                result += chr(ord(harf)-32)
            else:
                result += harf
        return result
    def is_lower(self):
        for harf in self.text:
            if harf >= "A" and harf <= "Z":
                return False
        return True
    def is_upper(self):
        for harf in self.text:
            if harf >= "a" and harf <= "z":
                return False
        return True
s = String("Hello")
print(s.to_lower())
print(s.to_upper())
print(s.is_lower())
print(s.is_upper())
