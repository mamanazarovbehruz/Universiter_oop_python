class Bino():
    """ Binolar haqida malumot """
    def __init__(self, nomi, maydoni, manzili, qavati, xona_soni):
        self.name = nomi
        self.area = maydoni
        self.address = manzili
        self.floor = qavati
        self.rooms = xona_soni


class Maktab_binosi(Bino):
    def __init__(self, nomi, maydoni, manzili, qavati, xona_soni):
        super().__init__(nomi, maydoni, manzili, qavati, xona_soni)
        self.students = 0
    def student(self, oquvchi_soni):
        self.students = oquvchi_soni    
    
class Bank(Bino):
    def __init__(self, nomi, maydoni, manzili, qavati, xona_soni):
        super().__init__(nomi, maydoni, manzili, qavati, xona_soni)
        self.mutaxasisligi = ''
    
    def purpose(self, maqsadi):
        self.mutaxasisligi = maqsadi

maktab = Maktab_binosi('7-maktab', '200 m2', 'Istiqlol ko\'chasi 4-uy', '3 qavat', 45)
maktab.student(1200)
print(maktab.name)
print(maktab.area)
print(maktab.address)
print(maktab.floor)
print(maktab.rooms)
print(maktab.students)

bank = Bank('Agro bank', '100 m2', 'bunyodgor ko\'chasi 2 - uy', '2 qavat', 20)
bank.purpose('Asosan valyuta ayirboshlash uchun')