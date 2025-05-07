
    // Automatic Type Conversion (Type Coercion):
    console.log(8*null)
    // → 0
    console.log("5"-1)
    // → 4
    console.log("5"+1)
    // → 51
    console.log("five"*2)
    // → NaN
    console.log(false==0)
    // → true

    let x=12
    let y=13.9
    console.log(x,typeof x)
    console.log(y,typeof y)
    let z=x+y
    console.log("sum:",z,typeof z)


    // User-Initiated Type Conversion (Explicit Type Conversion):
    let a,b,c,d;
    a=parseInt("3.14");  //Explicit type conversion from string to number
    b=Number("3.14");  //Explicit type conversion from string to number
    c=String(3.14);  //Explicit type conversion from number to string
    d=Boolean("pizza");  //Explicit type conversion from string to boolean
    console.log(typeof a);
    console.log(typeof b);
    console.log(typeof c);

    // Using arithmetic operators like + or * for type conversion is not a best practice and can lead to unexpected behavior.
