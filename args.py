# # *args
# # **kwargs
# def test_args(f_args, *argv):
#     print("첫번째 인자는: ",f_args)
#     for arg in argv:
#         print("argv 의 다른인자:", arg)
#
# test_args('야솦', 'python', '달걀', '테스트')
#
#
#
# def greet_me(**kwargs):
#     if kwargs is not None:
#         for key, value in kwargs.items():
#             print('키: {} 벨류: {}'.format(key, value))
#
#
#
# greet_me(name = 'dynamicduo')
#
# def test_args_kwargs(arg1, arg2, arg3):
#     print("인자1:",arg1)
#     print("인자2:",arg2)
#     print("인자3:",arg3)
#
# args = ("two", 3, 5)
# test_args_kwargs(*args)
#
# kwargs = {"인자3:" 3, "인자2":"two", "인자1": 5}
#
#
# test_args_kwargs(**kwargs)
#
# import someclass
#
# def get_info(self, *args):
#     retutn "test data"
#
# someclass.get_info = get_info()
#



import os

import numpy
# lotto = numpy.random.choice(range(1,46), 6, replace = False)
# lotto.sort()
os.system('clear')

fullcount = []
for i in range(1):
    lotto = numpy.random.choice(range(1, 46), 6, replace=False)
    lotto.sort()
    print(lotto)




















# loto = [1, 2, 3, 4, 5, 6]
# print(loto.count(1))



