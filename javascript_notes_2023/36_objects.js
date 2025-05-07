
/*
Objects in JavaScript are very similar to arrays, but 
objects use strings instead of numbers to access the 
different elements. The strings are called keys or 
properties, and the elements they point to are called 
values. Together these pieces of information are called 
key-value pairs.
*/
    const product={
        name:"bread",   //(property-value pair) property/key(always a string):value(can be any type)
        price:"$9"
    }
/*
JavaScript knows that the keys will always be strings, which 
is why you can leave out the quotes.spaces aren’t allowed in an unquoted key.
*/
    console.log(product);
    console.log(product["name"]);  // asscessing values in obj with bracket notation
    console.log(product.price);  // asscessing values in obj with dot notation
    product.name="honey";  //change property value
    product.newProperty="rice";  //add new property
    delete product.newProperty;  //delete property

    const product2={
        name:"icecream",   
        price:"$15",
        ["serial-no"]:337, //bracket notation lets us use properties that don"t work with dot notation
        rating:{           //nested object
            stars:4.3,
            count:79
        },
        func:function message(){  //functions inside objects called methods
            console.log("message display in console")
        }
    }
    console.log(product2.price)
    console.log(product2["serial-no"])
    console.log(product2.rating.stars)  //calling property of obj inside obj
    product2.func() // object.funciton()
    console.log(typeof console)
    console.log(typeof console.log)

    // buildinobj
    // JSON,localStorage

    // JSON(javascript object notation) build-in objects help us work with JSON is syntax similar to javascript syntax,similiar to javascript object but has less features,JSON syntax understood almost every programming language(more universel),thats why we use JSON to send data between two different computers using two different programming languages,and also use JSON to store data.
    
    // converting js--->JSON
    console.log(JSON.stringify(product2))  // JSON doesnot support function
    console.log(typeof JSON.stringify(product2))

    // converting JSON--->js
    console.log(JSON.parse(JSON.stringify(product2)))
    console.log(typeof JSON.parse(JSON.stringify(product2)))

    // localStorage
    localStorage.setItem("message","hello")
    console.log(localStorage.getItem("message")) //local storage only supports strings

    // auto-boxing(javascript automatically wraps the string in an object like a box)
    console.log("hello".length)
    console.log("hello".toUpperCase())
    console.log(2.0.toString())
    console.log(true.toString()) //doesnot work with null or undefined

