
    // primitive/value types(copy by values)->numbers,strings,booleans,undefined,null difintion:store simple data types

        let num=10;
        let value=null; //object
        console.log(typeof num)
        console.log(typeof value)
        // the best way to determine if a value is null is to compare it against null directly
        console.log(value==null)


        let x=10;
        let y=x;
        x=30;
        console.log(`x=${x}`,`y=${y}`)

    // reference types(copy by reference)->objects,arrays,functions    definition:store as objects which are really just references to location in memory
        let xx={
            value:10
        };
        let yy=xx;
        xx.value=30;
        console.log(`xx=${xx.value}`,`yy=${yy.value}`)

        
    // major diff b/w primitive and reference is primitive store directly in variable while reference type holds a pointer(reference) to the location in memory where the object exsists
