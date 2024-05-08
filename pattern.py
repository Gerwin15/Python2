def showPattern(rCount, cCount):
    for r in range (rCount):
        print ('O\t', end="")
        for  c in range (cCount):
            print ('X\t', end="")
        print()

row = 5
col = 10
showPattern(row, col)

    