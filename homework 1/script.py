import math
#craete the list
list = []
for i in range(1, 300):
    list.append(i)

# print(list)

print("length of the list:{}".format(len(list)) )

# printing square values
print("the square values in the list:")
for i in list:
    if (math.sqrt(i).is_integer()):
        print(i)


print("57 is in the list") if 57 in list else print("57 is not in the list")