
    // reference to a particular object but it depends on the immediate context where it used
    let product={
        name:"cake",
        message:function(){
            console.log(`name of product is ${this.name}`)
        }
    };
    product.message();
    
    function sayMyName(){
            console.log(`name of product is ${this.name}`)
        }

    let product1={
        name:"icecream",   
        message:sayMyName
    };
    let product2={
        name:"bread",   
        message:sayMyName
    };
    
    product1.message();
    product2.message();
    let name="coke";
    sayMyName();

