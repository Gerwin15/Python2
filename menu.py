def getLargest(arrNum):
    largest = arrNum[0]
    for n in arrNum:
        if n > largest:
            largest = n 

    return largest

def showPattern(rCount, cCount):
    for r in range (rCount):
        print ('O\t', end="")
        for  c in range (cCount):
            print ('X\t', end="")
        print()

while True:
    def showOptions():
        print('1. Largest Number')
        print('2. Pattern')
        print('3. Exit Program')

    showOptions()
    choice = int(input('Enter desired  program:'))
    if choice == 1:
        nums = [5,31,7,9,2]
        largest = getLargest(nums)
        print('Largest', largest)
    elif choice == 2:
        r = 5
        c = 5
        showPattern(r,c)
    elif choice == 3:
        print('Thanks for using MyApp 1.0. Bye...')
        break
    else:
        print('ERROR! Invalid input, 1 to 3 only')

