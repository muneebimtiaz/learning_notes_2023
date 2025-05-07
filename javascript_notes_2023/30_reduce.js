
    // reduces an array to a single value
    let prices=[10,15,20,55,60];
    
    let total=prices.reduce(checkout);
    console.log(total);

    function checkout(total,value){
        return total+value;
    }
