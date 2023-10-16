function updateInventory(arr1, arr2) {
    const indexArray  = (item)=>{
        for (let i = 0; i < arr1.length; i++) {
            const element = arr1[i];
            if(item=== element[1])
             return i
        }
        return -1;
    }
    const sortFun = (a,b)=>{
        if (a[1] > b[1]) {
            return 1;
        }
        if (a[1] < b[1]) {
            return -1;
        }
        return 0;
    }
    for (let i = 0; i < arr2.length; i++) {
        const search = arr2[i][1]
       const index = indexArray(search)
       if(index>=0){
        arr1[index][0]=arr1[index][0] + arr2[i][0]
       }else{
        arr1.push(arr2[i])
       }
    }

    return arr1.sort(sortFun);
}

// Example inventory lists
const curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
];

const newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];

console.log(updateInventory(curInv, newInv));