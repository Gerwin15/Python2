def getLargest(arrNum):
    largest = arrNum[0]
    for n in arrNum:
        if n > largest:
            largest = n 

    return largest

nums = [5,31,7,9,2]
l = getLargest(nums)
print('Largest is:  ', l)