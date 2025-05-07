
        function createProduct(na,pr,sr){
            this.name=na
            this.price=pr
            this.serialno=sr 
            this.rating={
                stars:4.3,
                count:79
            }
            this.message=()=> console.log('message display in console')
        }
// by convention constructor in javascript begin with a capital letter
const product1 = new createProduct('bread', '$43', 234);
const product2 = new createProduct('soda', '$32', 242);

console.log(product1.name);
console.log(product1.price); 
console.log(product1.rating); 
product1.message(); 
