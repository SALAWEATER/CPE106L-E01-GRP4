fileName = input("Enter the file name: ")


def run_all_functions(fileName):
    global f 
    f = open(fileName, 'r')
    median()
    f.close()
    
    f = open(fileName, 'r')
    mode()
    f.close()
    
    f = open(fileName, 'r')
    mean()
    f.close()

def median():   
    # Input the text, convert it to numbers, and
    # add the numbers to a list
    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))

    if len(numbers) == 0:
        print("The median is 0")
        return 0
    
    #Sort the list and print the number at its midpoint
    numbers.sort()
    midpoint = len(numbers) // 2
    print("The median is", end=" ")
    if len(numbers) % 2 == 1:
        print(numbers[midpoint])
    else:
        print((numbers[midpoint] + numbers[midpoint - 1]) / 2)

def mode():
    # Input the text, convert its to words to uppercase, and
    # add the words to a list
    words = []
    for line in f:
        wordsInLine = line.split()
        for word in wordsInLine:
            words.append(word.upper())

    if len(words) == 0:
        print("The mode is 0")
        return 0
    
    # Obtain the set of unique words and their
    # frequencies, saving these associations in
    # a dictionary
    theDictionary = {}
    for word in words:
        number = theDictionary.get(word, None)
        if number == None:
            # word entered for the first time
            theDictionary[word] = 1
        else:
            # word already seen, increment its number
            theDictionary[word] = number + 1

    # Find the mode by obtaining the maximum value
    # in the dictionary and determining its key
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            print("The mode is", key)
            break

def mean():
    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))
    f.close()

    if len(numbers) == 0:
        print("The mean is 0")
    else:
        avg = sum(numbers) / len(numbers)
        print("The mean is", avg)

run_all_functions(fileName)