
    let movies={
        "Finding Nemo":{
            releaseDate:2003,
            duration:100,
            actors:["Albert Brooks", "Ellen DeGeneres", "Alexander Gould"],
            format:"DVD"
        },
        "Star Wars: Episode VI - Return of the Jedi":{
            releaseDate:1983,
            duration:134,
            actors:["Mark Hamill", "Harrison Ford", "Carrie Fisher"],
            format:"DVD"
        },
        "Harry Potter and the Goblet of Fire":{
            releaseDate:2005,
            duration:157,
            actors:["Daniel Radcliffe", "Emma Watson", "Rupert Grint"],
            format:"Blu-ray"
        }
        };
/*
You might have noticed that I used quotes for the movie 
titles (the keys in the outer object) but not for the keys in the 
inner objects. That’s because the movie titles need to have 
spaces
*/

        let findingNemo=movies["Finding Nemo"];
        findingNemo.duration;   //100
        findingNemo.format;

        let cars={
            releaseDate:2006,
            duration:117,
            actors:["Owen Wilson", "Bonnie Hunt", "Paul Newman"],
            format:"Blu-ray"
        };
        movies["Cars"] = cars;
// list the names of all  movies
        Object.keys(movies);
        
