#파이썬 예외 처리 try / except 

# try:
#     val = "10.5"
#     n = int(val)
# except ValueError as e:
#     print("오류발생 오류발생!!{}".format(e))


try:
   idx = []
   idx[0] = 100
except Exception as e:
    print("오류발생 오류발생!!{}".format(e))
finally:
    print("파이널리 호출 오케이")
    