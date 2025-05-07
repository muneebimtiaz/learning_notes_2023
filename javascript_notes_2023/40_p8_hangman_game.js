
        // creating a random word
        let randomWords=["python","fish","monkey","apple","dog","plant","school","newyork","computer","elephant"]
        function randomNum(arr){
            return Math.floor(Math.random()*arr.length)
        }
        let mainWord=randomWords[randomNum(randomWords)];

        // creating a answer array
        let ansArray=[];
        for(let i=0;i<mainWord.length;i++){
            ansArray[i]="_";
        }
        let remainingLetters=mainWord.length;
        
        // game loop
        while(remainingLetters>0){
            alert(ansArray.join(" "));
            userInput=prompt("Guess a letter,or click cancel to stop playing");
            if(userInput===null){
                break;
            }else if(userInput.length!==1){
                alert("Please enter only one letter at a time")
            }else{
                for(let j=0;j<mainWord.length;j++){
                    if(mainWord[j]===userInput){
                        ansArray[j]=userInput;
                        remainingLetters--
                    }p
                }
            }
        } 
        alert(`Guess Word:${mainWord}`)
