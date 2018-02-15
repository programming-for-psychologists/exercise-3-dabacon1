def repetition(letters, numberBeforeSwitch, numRepetitions):
    for x in range(numRepetitions):
        for y in range(numberBeforeSwitch):
            print letters[0]
        for y in range(numberBeforeSwitch):
            print letters[1]
repetition(['A','B'],2,5)