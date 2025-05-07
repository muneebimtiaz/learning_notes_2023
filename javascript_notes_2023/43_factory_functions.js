
function createProduct(na,pr,sr){
    return {
        name:na,   
        price:pr,
        serialno:sr,
        rating:{         
            stars:4.3,
            count:79
        },
        message:function print(){
            console.log('message display in console')
        }
    }
}

const product1 = createProduct('bread', '$43', 234);
const product2 = createProduct('soda', '$32', 242);

console.log(product1.name);
console.log(product1.price); 
console.log(product1.rating); 
product1.message(); 
