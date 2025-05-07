
// array#1
let anime=["aot","fmab","jjba","mha"];
console.log(anime);

// access an array's elements
console.log(anime[1]);
console.log(anime[-2]);  //negative index not work in js
// setting or changing element in a array
anime[3]="jk";
console.log(anime)

/*
The act of running a method in 
computer-speak is known as calling the 
method. When you call the push method, 
two things happen. First, the element 
in parentheses is added to the array. 
Second, the new length of the array is 
returned. That’s why you see those numbers printed out every time you call push 
*/

// array methods()
anime.push("naruto");   //add element at the end of an array
anime.pop();    //remove element from the end of an array
anime.unshift("onepiece");  //add element at the beginning of the array
anime.shift();  //remove element from the beginning of the array
anime.length;  //length of the array
anime.indexOf("jjba");  //finding the index of an element in an array
// If the element whose position you ask for is not in the array,JavaScript returns -1.
// This is JavaScript’s way of saying “That doesn’t exist here,” while still returning a number
firstArray.concat(otherArray)  //adding arrays
firstArray.concat(otherArray,moreArray)  //joining multiple arrays
anime.join(" ")  //turning an array into a string --> .join(separator)
console.log(anime) 


// array#2
let fruit=["apple","mango","orange","banana","strawberry"]
// way 1
for(let i=0;i<fruit.length;i+=1){
        console.log(fruit[i]);
}
// way 2
for(let i of fruit){
        console.log(i);
}  

// we can select a random element from an array
let randomWords=["Explosion","Bear","City","Spacestation"];
let randomIndex=Math.floor(Math.random()*4);
// let randomIndex=Math.floor(Math.random()*randomWords.length);
randomWords[randomIndex]