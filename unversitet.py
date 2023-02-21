from operator import imod
from unversitet_klass import *
import pprint
# unversitet = [
#     {
#         'name':'Toshkent axborot texnalogiyalari unversiteti',
#         'address':'Amir Temur ko\'chasi 108 - uy',
#         'domen':'http//tuit.uz'
#     },
#     {
#         'name':'Toshkent moliya unversiteti',
#         'address':'Amir Temur ko\'chasi 90 - uy',
#         'domen':'http//tdmu.uz'
#     }
# ]


def run():
    print('Toshkent axborot texnalogiyalari unversitetiga xush kelibsiz!!!')
    sikl = '2'
    while sikl == '2':
        print('1.Unversitet haqida malumot')
        print('2.Unversitet tizimiga kirish')
        print('3.Unversitet qabul bo\'limi')
        ins = input('Nomer kiriting : ')
        if ins.isdigit():
            ins = int(ins)
            if ins == 1:
                sikl = '1'
                while sikl == '1':
                    print('1.Unversitet haqida')
                    print('2.Fakultetlari')
                    ins = input('Nomer kiriting : ')
                    if ins.isdigit():
                        tatu = tatu_dict()[0]
                        tuit = Tatu(tatu['name'], tatu['address'], tatu['domen'], tatu['faculties'])
                        ins = int(ins)
                        if ins == 1:
                            print(tuit.get_info())
                        elif ins == 2:
                            tuit.get_fakultet()
                        else:
                            print('1 yoki 2 raqamini kiriting.')
                        sikl = input('1.Orqaga || 2.Bosh menu (1/2) : ')
                    else:
                        print('Raqam kiriting.')
            elif ins == 2:
                sikl = '1'
                while sikl == '1':
                    print('1.O\'qtuvchi')
                    print('2.O\'quvchi')
                    # print('3.Owener')
                    ins = input('Nomer kiriting : ')
                    if ins.isdigit():
                        ins = int(ins)
                        if ins == 1:
                            ustozs = ustoz_dict()
                            login = input('Loginizni kiriting :')
                            password = int(input('Parolizni kiriting :'))
                            baza = False
                            for ustoz in ustozs:
                                if login == ustoz['login'] and password == ustoz['password']:
                                    baza = True
                                    sikl = '1'
                                    while sikl == '1':
                                        print('1.Malumotlariz : ')
                                        print('2.O\'quvchilariz : ')
                                        ins = int(input('Nomer kiritng : '))
                                        if ins == 1:
                                            ustoz1 = Ustoz(ustoz['name'], ustoz['surname'], ustoz['login'], ustoz['password'], ustoz['faculty'], ustoz['science'])
                                            print(ustoz1.get_info())
                                        elif ins == 2:
                                            students = talaba_dict()
                                            fullnames = []
                                            baho = {
                                                'Ustoz':f'{ustoz["surname"]} {ustoz["name"]}',
                                                'Fan':f'{ustoz["science"]}'
                                            }
                                            numer = 1
                                            for student in students:
                                                for science in student['science']:
                                                    if ustoz['science'] == science:
                                                        print(f'{numer}.{student["surname"]} {student["name"]}')
                                                        fullnames.append(student)
                                                        numer += 1
                                            ins = int(input('Nomer kiriting : '))
                                            fullname = fullnames[ins - 1]
                                            print(f'{fullname["surname"]} {fullname["name"]}')
                                            print(f'{ustoz["science"]} fanidan 0 balldan 100 ballgacha baholang')
                                            ball = input('ball : ')
                                            baho['Ball'] = ball
                                            fullname['rating'].append(baho)
                                            numer = 0
                                            for student in students:
                                                if student['login'] == fullname['login'] and student['password'] == fullname['password']:
                                                    students.pop(numer)
                                                    students.insert(numer,fullname)
                                                numer += 1
                                            talaba_dump(students)
                                        else:
                                            print('Bunday amal yoq.')
                                        sikl = input('1.Orqaga || 2.Bosh menu (1/2) : ')
                            if baza == False:
                                print('Siz bazadan topilmadiz.')
                        elif ins == 2:
                            login = input('Loginizni kiriting :')
                            password = int(input('Parolizni kiriting :'))
                            students = talaba_dict()
                            for student in students:
                                if login == student['login'] and password == student['password']:
                                    talaba = Talaba(student['name'], student['surname'], student['login'], student['password'], student['faculty'], student['science'], student['rating'])
                                    print('')
                                    print(talaba.get_info())
                                    talaba.get_fan()
                            sikl = input('1.Orqaga || 2.Bosh menu (1/2) : ')
                        # elif ins == 3:
                        #     owener = owener_dict()
                        #     login = input('Loginizni kiriting :')
                        #     password = input('Parolizni kiriting :')
                        #     natija = False
                        #     for owner in owener:
                        #         if login == owner['login'] and password == owner['password']:
                        #             natija = True
                        #             print('1.Unversitet')
                        #             print('2.O\'qtuvchilar')
                        #             print('3.o\'quvchilar')
                        #             nomer = input('Nomer kiriting : ')
                        #             if nomer == '1':
                        #                 pass
                        #             elif nomer == '2':
                        #                 pass
                        #             elif nomer == '3':
                        #                 pass
                        #             else:
                        #                 print('Bunday amal yoq.')
                        #     if not natija:
                        #         print('Login yoki Paroliz xato!!!')
                        #     sikl = input('1.Orqaga || 2.Bosh menu (1/2) : ')
                        else:
                            print('Bunday amal yoq')
                    else:
                        print('Raqam kiriting.')
            elif ins == 3:
                fakultet = ['KOMPYUTER INJINIRINGI', 'DASTURIY INJINIRINGI', 'KIBERXAVFSIZLIK', 'TELEKOMMUNIKATSIYA TEXNOLOGIYALARI', 'TELEVIZION TEXNOLOGIYALAR']
                fan = ['Kriptagrafiya','Tarmoq havfsizligi','Mashinali O\'qitish','Operatsion Tizimlar','Dasturiy Taminot','Web Dasturlash','Metralogiya','Kompyuter Tarmoqlari','Boshqaruv Tamoyillari','Texnalogik Jarayon']
                fan1 = []
                ism = input('Ismingiz : ')
                familya = input('Familyangiz : ')
                login = input('Loginiz : ')
                parol = input('Paroliz : ')
                print('Fakultetni tanlang')
                ins = 1
                for x in fakultet:
                    print(f'{ins}.{x}')
                    ins += 1
                nomer = int(input('Nomer kiriting : '))
                fakultet1 = fakultet[nomer-1]
                sikl = 'ha'
                while sikl == 'ha':
                    print('Fanlarni tanlang')
                    ins = 1
                    for x in fan:
                        print(f'{ins}.{fan[ins-1]}')
                        ins += 1
                    nomer = int(input('Nomer kiriting : '))
                    fan1.append(fan[nomer-1])
                    sikl = input('Yana fan tanlaysizmi ha/yoq :')
                talaba = {
                    'name': ism,
                    'surname': familya,
                    'login': login,
                    'password': parol,
                    'faculty': fakultet1,
                    'science': fan1,
                    'rating': []
                }
                student = talaba_dict()
                student.append(talaba)
                talaba_dump(student)
                sikl = input('1.Orqaga || 2.Bosh menu (1/2) : ')
            else:
                print('Faqat 1/2/3 raqamlardan birini kiriting...')
        else:
            print('Raqam kiritng...')

if __name__ == '__main__':
    run()