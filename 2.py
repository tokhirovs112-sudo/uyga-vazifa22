class Convertor:
    def ru_to_en(self, text):
        ru = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        en = "ABVGDEYOZHZIYKLMNOPRSTUFHTSCHSHCH_Y_YEYA"
        result = ""
        for harf in text:
            if harf in ru:
                result += en[ru.index(harf)]
            elif harf.lower() in ru.lower():
                result += en.lower()[ru.lower().index(harf.lower())]
            else:
                result += harf
        return result
    def en_to_ru(self, text):
        en = "ABVGDEYOZHZIYKLMNOPRSTUFHTSCHSHCH_Y_YEYA"
        ru = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        result = ""
        for harf in text:
            if harf in en:
                result += ru[en.index(harf)]
            elif harf.lower() in en.lower():
                result += ru.lower()[en.lower().index(harf.lower())]
            else:
                result += harf
        return result
c = Convertor()

print(c.en_to_ru("Salom dunyo"))