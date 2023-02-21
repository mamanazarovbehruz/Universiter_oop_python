# # 1-misol
# class Notebook():
#     def __init__(self, name, color, memory):
#         self.nomi = name
#         self.rangi = color
#         self.xotira = memory

# class HP(Notebook):
#     def __init__(self, name, color, memory):
#         super().__init__(name, color, memory)
    
#     def get_info(self):
        
#         return f'Nomi : {self.nomi} \nRangi : {self.rangi} \nXotirasi : {self.xotira}'

# hp = HP('Lenuva', 'Qora', '8 Gb / 512 SSD')
# print(hp.get_info())

# # 2-misol
# class Xona():
#     def __init__(self, eni, boyi, balandligi):
#         self.eni = eni
#         self.boyi = boyi
#         self.balanligi = balandligi

# xona = Xona(12, 8, 3)
# print(f'Eni : {xona.eni}')
# print(f'Boyi : {xona.boyi}')
# print(f'Balandligi : {xona.balanligi}')

# # 3-misol
# import builtins

# def open(abc):
#     f = builtins.open(abc, 'r')
#     return Abc(f)

# class Abc:

#     def __init__(self, f):
#         self._f = f

#     def read(self):
#         return self._f

# x = Abc(-155)
# print(x.read())

# # 4-misol
# class Student():
#     def __init__(self, Student_id, Student_name):
#         self.id = Student_id
#         self.name = Student_name

# class Student1(Student):
#     def __init__(self, Student_id, Student_name, Student_class):
#         super().__init__(Student_id, Student_name)
#         self.klass = Student_class
    
#     def get_info(self):
#         return f'ID : {self.id} \nName : {self.name} \nKlass : {self.klass}'

# student = Student1(1111, 'Behruz', 'Student')
# print(student.get_info())

# # 5-misol
# rim = {
#     '1':'I',
#     '5':'V',
#     '10':'X',
#     '50':'L',
#     '100':'C',
#     '500':'D',
#     '1000':'M'
# }


# class Rim():
#     def __init__(self, son):
#         self.son = son
    
#     def rim(self):
#         rimm = ''
#         nomer = self.son
#         ins = len(str(nomer))
#         i = 1
#         while i <= ins:
#             a = nomer % (10**i)
#             b = a // (10**(i-1))
#             if b == 1:
#                 rimm = rim[f'{10**(i-1)}'] + rimm
#             elif b == 2:
#                 rimm = rim[f'{10**(i-1)}'] + rim[f'{10**(i-1)}'] + rimm
#             elif b == 3:
#                 rimm = rim[f'{10**(i-1)}'] + rim[f'{10**(i-1)}'] + rim[f'{10**(i-1)}'] + rimm
#             elif b == 4:
#                 rimm = rim[f'{10**(i-1)}'] + rim[f'{a + 10**(i-1)}'] + rimm
#             elif b == 5:
#                 rimm = rim[f'{a}'] + rimm
#             elif b == 6:
#                 rimm = rim[f'{(b -1 ) * (10**(i-1))}'] + rim[f'{10**(i-1)}'] + rimm
#             elif b == 7:
#                 rimm = rim[f'{(b -2 ) * (10**(i-1))}'] + rim[f'{10**(i-1)}'] + rim[f'{10**(i-1)}'] + rimm
#             elif b == 8:
#                 rimm = rim[f'{(b -3 ) * (10**(i-1))}'] + rim[f'{10**(i-1)}'] + rim[f'{10**(i-1)}'] + rim[f'{10**(i-1)}'] + rimm
#             elif b == 9:
#                 rimm = rim[f'{10**(i-1)}'] + rim[f'{10**(i)}'] + rimm
#             else:
#                 pass
#             nomer -= a
#             i += 1
#         return rimm

# def run():
#     sikl = 'ha'
#     while sikl == 'ha':
#         nomer = int(input('Raqam kiriting : '))
#         if 1 <= nomer < 4000:
#             son = Rim(nomer)
#             print(son.rim())
#             sikl = input('Yana raqam kiritasizmi ha/yoq : ')
#         else:
#             print('1 dan 4000 gacha bo\'lgan son kiriting!!!')

# if __name__ == '__main__':
#     run()

# # 7-misol

# class Qavslar():
#     def __init__(self, *qavslar):
#         self.qavslar = qavslar
    
#     def tekshiruv(self):
#         for qavs in self.qavslar:
#             ins = len(qavs)
#             i = 0
#             while i < ins:
#                 if qavs[i] == '(' and qavs[i + 1] == ')':
#                     natija = True
#                 elif qavs[i] == '[' and qavs[i + 1] == ']':
#                     natija = True
#                 elif qavs[i] == '{' and qavs[i + 1] == '}':
#                     natija = True
#                 else:
#                     natija = False
#                 i += 2
#             if natija:
#                 print(f'{qavs} qavslar to\'g\'ri')
#             else:
#                 print(f'{qavs} qavslar nato\'g\'ri')

# qavs = Qavslar('()', '()[]{}', '[)', '({[)]')
# qavs.tekshiruv()

# 8-misol

class Toplam():
    def __init__(self, *sonlar):
        self.sonlar = sonlar
    
    def toplamlar(self):
        toplamlar = [[],]
        sonlar:list = list(self.sonlar)
        ins = len(sonlar)
        i = 0
        while i < ins:
            toplam = []
            j = 0
            toplamlar = toplamlar.append(toplam)
            i += 1
        return toplamlar

def run():
    sonlar = Toplam(4, 5, 6)
    print(sonlar.toplamlar())

if __name__ == '__main__':
    run()