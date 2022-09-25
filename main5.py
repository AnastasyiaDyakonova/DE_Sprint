def dec(a):
    a = a[::-1]
    n = 0
    for i in range(len(a)):
        n += int(a[i])*2**i
    return n 

num1, num2 = input("Введите 1 число: "), input("Введите 2 число: ")    
decim = dec(num1)*dec(num2)
res = ""
while decim !=0:
    res += str(decim%2)
    decim = decim//2
print("Произведение равно:", res[::-1])