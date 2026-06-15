
class Taqvim:
    def hijriy(self, yil):
        hijriy_yil = int((yil - 622) * 33 / 32)
        return hijriy_yil
    def grigoriyan(self, yil):
        grigoriy_yil = int(yil * 32 / 33 + 622)
        return grigoriy_yil
    def kabisami(self, yil):
        if yil % 400 == 0:
            return True
        elif yil % 100 == 0:
            return False
        elif yil % 4 == 0:
            return True
        else:
            return False
t = Taqvim()
print(t.hijriy(2026))
print(t.grigoriyan(1447))
print(t.kabisami(2024))