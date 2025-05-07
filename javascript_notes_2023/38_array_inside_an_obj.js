
    // objects inside an array
    let movies=[
    {name:"Dark Knight",duration:"180min",rating:8.9},
    {name:"truth or dare",duration:"90min",rating:8},
    {name:"Saw",duration:"80min",rating:7.6}
    ];

    console.log(movies[0]); //to get info of elements of array
    console.log(movies[0].name); //to get info of property of objects

    
    // array inside an object
    let anna={name:"Anna",age:11,luckyNumbers:[2, 4, 8, 16]};
    let dave={name:"Dave",age:5,luckyNumbers:[3, 9, 40]};
    let kate={name:"Kate",age:9,luckyNumbers:[1, 2, 3]}
    let friends=[anna, dave, kate];

    console.log(friends[1]);
    console.log(friends[2].name);
    console.log(friends[0].luckyNumbers[1]);
