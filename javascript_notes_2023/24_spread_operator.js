
        let price=["$25","$55","$12","$45","$9"]
        console.log(...price)

        num=[11,35,79,56,34,67]
        console.log(Math.max(num))  //NaN
        console.log(Math.max(...num))

// add elements of an existing array into a new array
        // let class1=["eren","levi","mikasa"];
        // let class2=["connie","erwin","armin"];
        // class1.push(...class2)
        // console.log(...class1)

        let class1=["eren","levi","mikasa"];
        let class2=["connie","erwin","armin",...class1];
        console.log(class2)

// pass elements of the array as arguments of function
        let arg=[1,2,3,4,5]
        function sum(a,b,c){
            return a+b+c;
        }
        console.log(sum(...arg))

// cpy arrays   
        class1=["eren","levi","mikasa"];
        class2=[...class1];
        console.log(class2)
        
// concatinating arrays
        class1=[...class1,"hello to my",...class2]
        console.log(class1)
