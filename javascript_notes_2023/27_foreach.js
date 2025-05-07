
    // The forEach() method is a higher-order array method in JavaScript that allows you to iterate over the elements of an array and execute a provided function once for each element.
    
// order matters(value,index,array)
    let myNames=["muneeb","ali","jason"]
    myNames.forEach(sayHello);

    function sayHello(value){
        console.log("Hello"+value)
    }

    myNames=["muneeb","ali","jason"]
    myNames.forEach(sayHello);

    function sayHello(value,index,array){
        console.log("Hello"+index)
    }

//example 1
    let diffNames=["muneeb","surish","jason"] 

    diffNames.forEach(capName)
    diffNames.forEach(print)

    function capName(element,index,array){
        array[index]=element.toUpperCase();
    }
    function print(element){
        console.log(element);
    }

//example 2
    let diffNumbers=[2,3,4,5,6] 

    diffNumbers.forEach(sqtName)
    diffNumbers.forEach(print)

    function sqtName(value,index,array){
        array[index]=Math.pow(value,2);
    }
    function print(value){
        console.log(value);
    }

    // The forEach() method does not return a new array; it simply iterates through the existing array and applies the provided function to each element.
