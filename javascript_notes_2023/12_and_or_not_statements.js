
    // and operator(&&)
    let age=25;
    let hasDriverLicense=true;

    if(age>=18 && hasDriverLicense){
    console.log("You can drive!");
    }else{
    console.log("You cannot drive.");
    }


    // or operator(||)
    let isStudent=true;
    let isEmployee=false;

    if(isStudent || isEmployee){
    console.log("You have access to the building.");
    }else{
    console.log("You are not allowed to enter.");
    }


    // not operator(!)
    let loggedIn=false;

    if(!loggedIn){
    console.log("Please log in to continue.");
    }else{
    console.log("Welcome!");
    }

/*
NOT (!) - Highest Precedence
AND (&&) - Second Precedence
OR (||) - Lowest Precedence
*/
