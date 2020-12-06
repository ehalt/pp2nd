string = ''
numbers = []
for word in string.split():
    if word.isdigit():
        numbers.append(int(word))
print(numbers)