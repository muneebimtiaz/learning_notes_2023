
    // defining/declaring a function
    function square(x){
        //  When control comes across such a statement, it immediately jumps out of the current function and gives there turned value to the code that called the function
        return x*x;
    };
    // calling a function
    console.log(square(6))

    // function expression
                                //parameters
    const callMyName=function(fname,lname){
        console.log(`hi, ${fname} ${lname}`)
    };
                    //arguments
    callMyName("Muneeb","Imtiaz");
