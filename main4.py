word = input("Введите последовательность скобок: ").strip()
res = []
if len(word)%2 == 0:
    for i in word:
        if res == []:
            res.append(i)
        else:
            if (res[-1] == '{' and i == '}') or (res[-1] == '(' and i == ')') or (res[-1] == '[' and i == ']'):
                res.pop()
            else:
                res.append(i)
    if res == []:
        print(True)
    else:
        print(False)

else:
    print(False)