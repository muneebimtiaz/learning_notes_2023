
    //  rest parameters -> represents an indefinite number of parameters,condense multiple elements into an array (packs arguments into an array)

// passing array as an argument
    function sum(...nameOfArray){
        let total=0;
        for(let i of nameOfArray){
            total=total+i;
        }
        return total;
    }
    console.log(sum(1,2,3,4,5,6,7));
