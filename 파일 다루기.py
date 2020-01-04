



f = open('/Users/aucready/Documents/coding/VC/visualcode/hellofile.txt', 'r')
lines = f.readlines()

f.close()

f = open('/Users/aucready/Documents/coding/VC/visualcode/hellofile_rt01.txt', 'w')
for line in lines:
    f.write(line.replace('\t','    '))
f.close()




'''
file = open('/Users/aucready/Documents/coding/VC/visualcode/hellofile.txt', 'r')
txt = file.read()
print(txt)
file.close()
...


with open('/Users/aucready/Documents/coding/VC/visualcode/hellofile.txt', 'r') as file_re:
    txt = file_re.read()
    print(txt)

with open('/Users/aucready/Documents/coding/VC/visualcode/hellofile.txt', 'w') as f:
    for i in range(100):
        f.write('{}: hello python\n'.format(i))
        
with open('/Users/aucready/Documents/coding/VC/visualcode/hellofile.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))

print('{} {} {} {}'.format(1,2,3,4))
'''

# file = '    hello will     '
# f = file.upper()
# print(f)

# print(f.rstrip())
# print(f.lstrip())

# print(f.find('L'))

# print(f.rfind('L'))

# print('H' in f)


# print(f.split('L'))


# a = int(input('a:'))

# b = int(input('b:'))

# print('{}+{} = {}'.format(a, b, a+b))












