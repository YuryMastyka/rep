number = []
for i in range(5):
    number.append(int(input("number?:")))

def maxim(arg):
    max = 0
    for i in arg:
        if i > max:
            max = i
    return max

def minim (arg):
    min = 1
    for i in arg:
        if i < min:
            min = i
    return min

def remainder(arg):
    even = []
    odd = []
    for i in number:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd



print (number)
print (max(number))
print (min(number))
print (maxim(number))
print (minim(number))
print (remainder(number))
