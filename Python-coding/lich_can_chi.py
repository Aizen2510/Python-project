nam = int(input())
can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh","Mậu", "Kỷ"]
chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
def lich_can_chi(nam):
    return can[nam%10]+''+chi[nam%12]

lich_can_chi(nam)