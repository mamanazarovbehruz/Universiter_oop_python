from cmath import log
import json
from queue import PriorityQueue
    
class Unversitet():
    def __init__(self, name, address, domen, faculties):
        self.nomi = name
        self.manzil = address
        self.sayt = domen
        self.fakultet = faculties
    
    
class Tatu(Unversitet):
    def __init__(self, name, address, domen, faculties):
        super().__init__(name, address, domen, faculties)
    
    def get_info(self):
        return f'{self.nomi} 1955 - yil tashkil topgan \nManzil : {self.manzil} \nUnversitet asosan IT sohasiga yo\'naltirilgan \nSayti : {self.sayt}'

    def get_fakultet(self):
        ins = 0
        for x in self.fakultet:
            ins += 1
            print(f'{ins}.{x}') 

class Shaxs():
    def __init__(self, name, surname, login, password, faculty, science):
        self.ism = name
        self.familya = surname
        self.login = login
        self.parol = password
        self.fakultet = faculty
        self.fan = science

class Ustoz(Shaxs):
    def __init__(self, name, surname, login, password, faculty, science):
        super().__init__(name, surname, login, password, faculty, science)
    
    def get_info(self):
        return f'1.Ismingiz : {self.ism} \n2.Familyangiz : {self.familya} \n3.Loginiz : {self.login} \n4.Paroliz : {self.parol} \n5.Fakultetiz : {self.fakultet} \n6.Mutaxasisligiz : {self.fan}'

class Talaba(Shaxs):
    def __init__(self, name, surname, login, password, faculty, science, rating):
        super().__init__(name, surname, login, password, faculty, science)
        self.baho = rating
    
    def get_info(self):
        return f'Ismingiz : {self.ism} \nFamilyangiz : {self.familya} \nLoginiz : {self.login} \nParoliz : {self.parol} \nFakultetiz : {self.fakultet}'

    def get_fan(self):
        for x in self.fan:
            print(f'----- {x} fani ------')
            ins = 1
            natija = False
            for y in self.baho:
                if x == y['Fan']:
                    natija = True
                    print(f'{ins} - Baho')
                    ins += 1
                    print(f'Ustoz : {y["Ustoz"]}')
                    print(f'Ball : {y["Ball"]}')
            if not natija:
                print('Siz bu fandan baholanmadiz')



def tatu_dict():
    with open('unversitet.json', 'r') as file:
        tatu = json.load(file)
        return tatu


def talaba_dict():
    with open('talaba.json', 'r') as file:
        talaba = json.load(file)
    return talaba


def talaba_dump(student):
    with open('talaba.json', 'w') as file:
        json.dump(student, file, indent = 4)


def ustoz_dict():
    with open('ustoz.json', 'r') as file:
        ustoz = json.load(file)
    return ustoz

def owener_dict():
    with open('owener.json', 'r') as file:
        owener = json.load(file)
    return owener