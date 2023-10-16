def updateInventory(arr1,arr2):
    def indexArr(item):
        for actualItem in range(0,len(arr1)):
            if arr1[actualItem][1] == item:
                return actualItem
        return -1

    for new in arr2:
        index =  indexArr(new[1])
        if index>=0:
            arr1[index][0]= arr1[index][0] + new[0]
        else:
            arr1.append(new)
    return sorted(arr1,key=lambda x: x[1])

# Example inventory lists
curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]

newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
]

print(updateInventory(curInv, newInv))