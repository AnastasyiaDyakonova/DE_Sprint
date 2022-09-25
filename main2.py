#phrase = ''.join(input('Введите слово или фразу для проверки:').split()
phrase = input('Введите слово или фразу для проверки:').replace(" ", "")
if phrase == phrase[::-1]:
    print("true")
else:
    print("false")

