function binnarySearch(arr, target) { 
    // First element
    let begin = 0

    // Last Element
    let end = arr.length - 1

    // Loops until get the target or until the middle is empty
    while (begin <= end) {

        // Middle element
        let middle = Math.floor((begin + end) / 2)

        // Check
        if (arr[middle] < target) {
            begin = middle + 1
        } else if (arr[middle] > target) {
            end = middle - 1
        } else {
            // the target is the middle value
            return middle
        }      
    }
    // Target not found
    return -1;
}

const arrayCadence = [0,1,3,5,9,10,15,16,17,18,19,22,26,28,29,30]
console.log(binnarySearch(arrayCadence, 99))
