#
#
#
# class person:
#     def greeting(self):
#         print('안녕하세요.')
#
# class student(person):
#     def study(self):
#         print('공부하기')
#
# james = student()
#
# james.greeting()
# james.study()
#
#
# print(issubclass(student, person))

#--------------------------------------
#
#
# class person:
#     def greeting(self):
#         print('Hi hello?')
#
# class person_list:
#
#     def __init__(self):
#         self.person_list = []
#
#     def append_person(self):
#         self.person_list.append(person)
#
#-----------------------------------
#
# class person():
#     def __init__(self):
#         print('peron __init__')
#         self.hello = 'hello?'
#
# class student(person):
#
#     def __init__(self):
#         print('student__init__')
#         super().__init__()
#         self.school = 'best school'
#
# class yung_student(person):
#     def __init__(self):
#
#
#         self.school = 'best school is here!'
#
#     pass
#
#
#
# james = student()
# print(james.school)
# print(james.hello)
#
# mark = yung_student()
# print(mark.hello)
# print(mark.school)





#-----------------------------


#
#
# class person:
#     def greeting(self):
#         print('안녕하세요')
#
# class student(person):
#     def greeting(self):
#         super().greeting()
#         print('홍대입니다.')
#
# james = student()
#
# james.greeting()

#---------------------------------
#
# class person:
#     def greetin(self):
#         print('안녕하세요?')
# class university:
#     def mannage_credit(self):
#         print('학점관리')
#
# class undergraduation(person, university):
#     def study(self):
# #        super().__init__()
#
#         print('공부하기')
#
# james = undergraduation()
#
# james.greetin()
# james.mannage_credit()
# james.study()

#다이아몬드 상속(죽음의 다이아몬드)
#
#
# class a:
#     def greeting(self):
#         print('a')
#
#
# class b(a):
#     def greeting(self):
#         print('b')
#
#
# class c(a):
#     def greeting(self):
#         print('c')
#
#
#
# class d(b,c):
#     pass
#
#
# x = d()
# x.greeting()
#
# print(d.mro())
#
# print(int.mro())


#
# class advencelist(list):
#     def replace(self, old, new):
#         while old in self:
#             self[self.index(old)] =  new
#
# x = advencelist([1,2,3,4,5,100,3,1,4,1,33,1])
#
# x.replace(1, 500)
# print(x)

# --------------------------
# import math
# class point2d:
#     def __init__(self, x ,y):
#
#         self.x = x
#         self.y = y
#
#
# p1 = point2d(30,20)
# p2 = point2d(60,50)
#
# a = p2.x - p1.x
# b = p2.y - p1.y
#
#
# c = math.sqrt(a**2+ b**2)
#
# print(c)

#---------------------------------

#
# class rectagle:
#     def __init__(self,x , y, x2, y2):
#         self.x = x
#         self.y = y
#         self.x2 = x2
#         self.y2 = y2
#
#
# rec =  rectagle(20,20,40,30)
#
# width = abs(rec.x2 - rec.x)
# height = abs(rec.y2 - rec.y)
# area = width * height
# print(area)

#--------------------------

#
# try :
#     x = int(input('어떤숫자로 나눌지 입력 하세요'))
#     y = 10 /x
#
# except ZeroDivisionError:
#     print("숫자를 0이로 나눌수 없습니다.")
# else:
#     print(y)
#
# class except_raise(Exception):
#
#     def __init__(self):
#         super().__init__('3의 배수가 아닙니다. ')
#
# def three_multi():
#     try :
#         x = int(input('3의 배수를 입력하세요:'))
#         if x % 3 != 0:
#             raise except_raise
#         print(x)
#     except Exception as e:
#         print('예외가 발생 했습니다. ', e)
#
# three_multi()
#-------------------------------------------


def file_read():

    with open('word.txt') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            yield line.strip('\n')

for i in file_read():
    print(i)




