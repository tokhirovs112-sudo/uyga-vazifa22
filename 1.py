class Talaba:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Kurs:
    def __init__(self, kurs_name, kurs_teacher):
        self.kurs_name = kurs_name
        self.kurs_teacher = kurs_teacher
        self.talabalar_soni = 0
        self.talabalar = []


    def add(self, new_student):
        self.talabalar.append(new_student)
        self.talabalar_soni += 1


    def delete(self, new_student):
        self.talabalar.remove(new_student)
        self.talabalar_soni -= 1


    def info_kurs(self):
        print("Kurs:", self.kurs_name)
        print("Teacher:", self.kurs_teacher)
        print("Talabalar:", self.talabalar_soni)

        for talaba in self.talabalar:
            print(talaba.name, talaba.age)



kurs1 = Kurs("Python", "Ali")
kurs2 = Kurs("Java", "Vali")


for i in range(10):
    kurs1.add(Talaba("Ali"+str(i), 15+i))
    kurs2.add(Talaba("Vali"+str(i), 16+i))


kurs1.delete(kurs1.talabalar[0])
kurs2.delete(kurs2.talabalar[0])


kurs1.info_kurs()
print()
kurs2.info_kurs()
