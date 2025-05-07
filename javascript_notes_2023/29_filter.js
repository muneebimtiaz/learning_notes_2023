
    // creates the new array with all elements that pass the test provided by a function
    let diffAges=[10,15,20,25,30,35];
    
    let passAges=diffAges.filter(check);
    passAges.forEach(print);

    function check(value){
        if(value>=18){
            return value;
        }
    }
    function print(value){
        console.log(value);
    }
