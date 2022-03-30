file = open("D:/Dakshiin/Python/class98/file.txt", "r")
text_in_file=file.read()
words = 1
for i in text_in_file:
    if(i==' '):
        words = words + 1

print(words)
