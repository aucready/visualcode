#파이썬에서 파일 읽고 쓰기

# file =  open("sample.txt",mode = "w", encoding="utf-8")

# file.write("안녕 파이썬")

# file.close()


# rfile = open("sample.txt", mode = "r")

# a = rfile.read(10)
# print(rfile.tell())
# print(a)
# rfile.seek(0)

# a = rfile.read(10)
# rfile.close()
# print(a)

with open("sample.txt", mode = "r", encoding="utf-8") as s, \
    open("sample2.txt", mode = "w", encoding="utf-8") as t:
    t.write(s.read().replace("파이썬", "python"))





    


