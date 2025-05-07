
                        //   index   index                  index                    index      
                        //    [0]     [1]                    [2]                      [3]
    let dinosaursAndNumbers = [3, "dinosaurs", ["triceratops","stegosaurus", 3627.5], 10];
    dinosaursAndNumbers[2];  //["triceratops", "stegosaurus", 3627.5
    dinosaursAndNumbers[2][0];  //"triceratops"


    // example 1
    let anime=["aot","naruto","onepiece"];
    let movies=["#alive","batman vs superman","inception"];
    let series=["Twd","got","vikings"];
// way 1
    let tv=[anime,movies,series];
    for(let i=0;i<tv.length;i+=1){
        for(let j=0;j<tv[i].length;j+=1){
            console.log(tv[i][j])
        }
    } 
// way 2
    for(let i of tv){
        for(let j of i){
            console.log(j);
        }
    }


    // example 2
    let numbers=[1,2,3,4,5,6];
    let alphabets=["a","b","c","d","e","f"];
    let characters=["!","@","#","$","%","^","&"];
// way 1
    let combineAll=[numbers,alphabets,characters];

    for(let i=0;i<combineAll.length;i+=1){
        for(let j=0;j<combineAll[i].length;j+=1){
            console.log(combineAll[i][j])
        }
    } 
// way 2        
    for(let i of combineAll){
        for(let j of i){
            console.log(j);
        }
    }
