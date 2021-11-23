import random
import string

fileName = './students_names.txt'
# read the file
file = open(fileName)
students = file.read()

# write a list of random names
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

names = ''
for i in range(5):
    names = names + get_random_string(random.randint(2, 10)) + '\n'

file = open(fileName, 'w')
file.write(names)

# read the first n lines 
n = input("enter the number of lines to read:")
n = int(n)
file = open(fileName)
lines = file.readlines()
for i in range(n):
    print(lines[i], end='')


#read the last n lines
n = input("enter the number of lines to read from the end:")
n = int(n)
file = open(fileName)
lines = file.readlines()
i = 0
j = -1
while i < n:
    print(lines[j], end='')
    j -= 1
    i += 1


# check if x is in the names
x = input('enter the name:')
for line in lines:
    line = line.strip()

if x in lines:
    print("{} is in the list".format(x))
else:
    print("{} is not in the list".format(x))

# generate files from a.txt to z.txt
# make sure the folder 'alphabet_files' is created in the current working directory
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for c in alpha:
    file = open('./alphabet_files/' + c + '.txt', 'w')
    file.write(c)