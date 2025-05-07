
    class Player{
        // static keyword can only be applied to a method or property thats belongs to a class and not any on e object 
        static totalPlayers=0;
        constructor(name,shirt){
            this.name=name;
            this.shirt=shirt;
            Player.totalPlayers+=1;
        // instead of each obj has its own property by using static keyword only class has a property for every object 
        }
        show(){
            console.log(`name:${this.name} shirt:${this.shirt} totalPlayers:${Player.totalPlayers}`)
        }
    }
    let p1=new Player("Ronaldo",7);
    let p2=new Player("Messi",10);
    let p3=new Player("Beckham",10);
    let p4=new Player("Onana",1);
    let p5=new Player("Garnacho",47);
    p1.show();
    p2.show();
    p3.show();
    p4.show();
    p5.show();
