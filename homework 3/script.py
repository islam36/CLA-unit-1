#5
def reverseString(string):
    result = ''
    for i in string:
        result = i + result
    return result



#1
def isPalindrome(string):
    return (reverseString(string) == string)


#2
def isPrime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x // 2):
            if (x % i == 0):
                return False
        return True



#3
def isInRange(x, start, end):
    return (start <= x <= end)


#4
def factoriel(x):
    if x == 0:
        return 1
    else:
        return x*factoriel(x-1)


#6
def sumOfList(list):
    result = 0
    for x in list:
        result += x
    return result


#7
def maxOf3(a, b, c):
    x = a
    if x < b:
        x = b
    if x < c:
        x = c
    return x