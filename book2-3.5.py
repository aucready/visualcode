# def f(a, b):
#     return a+b
#
#
#
# print (f(5,2))
#
#
# def f(a):
#     return a + 1
#
# print('결과값은 {}'.format(f(9)))
def f(a):
    def g(b):
        return a * b
    return g
doubler = f(2)
triplee =  f(3)
quruple =  f(4)
print(doubler(3))
print(triplee(5))
print(quruple(50))





