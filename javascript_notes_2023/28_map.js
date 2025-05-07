
    // executes a provided callback function once for each array value/element and creates a new array
    let diffNumbers=[10,15,20,25,30] 

    let diffSquares=diffNumbers.map(sqtName);
    diffNumbers.forEach(print);
    diffSquares.forEach(print);

    function sqtName(value,index,array){
        return Math.pow(value,2);
    }
    function print(value){
        console.log(value);
    }
