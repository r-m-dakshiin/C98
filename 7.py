
def countWordsFromFile():
    fileName = input("Enter the file name:-")
    w =0
    numberOfWords = 0

    file = open("D:/Dakshiin/Python/class98/multi.txt", "r")
    t = file.read()
    p = t.split()
    for i in p:
        w = w+1
    print(w)
    for line in file:
        words = line.split()
        numberOfwords = numberOfWords + len(words)
    print("Number of words:")
    print(numberOfWords)


countWordsFromFile()


