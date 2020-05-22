string = "The quick brown fox jumps over the lazy dog."
print('The first letters are:',string[0])

for x in range (0, len(string)):
    if string[x] == " ":
        letter = string[x + 1]
        print(letter)
