
# 5 + 5 * 10

operator = ['+', '-', '*', '/', '=']
user_input = '5333 + 3334 * 310'
string_list = []    
lop = 0

for i, s in enumerate(user_input):
    if s in operator:
        if user_input[lop:i].strip() != "":
            string_list.append(user_input[lop:i])
            string_list.append(s)
            lop = i+1
print(string_list)


