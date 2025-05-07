
        // class Person{
        //     constructor(fname,lname){
        //         this.fname=fname;
        //         this.lname=lname;
        //     }
        // get fullName(){
        //     return (`${this.fname} ${this.lname}`);
        // }}

        // let p1=new Person("muneeb","imtiaz");
        // p1.fname="mike";
        // console.log(p1.fullName)

        class Employee{
            constructor(name,salary){
                this._name=name;
                this._salary=salary;
            }
        get salary(){
            
            if(this._salary>3500 && this._salary<20000){
                console.log("Salary incremented by 5%")
            }
            else if(this._salary<3500 && this._salary>0){
                console.log("Salary incremented by 10%")
            }
            else{
                console.log("enter a logical this._salary")
            }
            return `Name:${this._name} oldSalary:${this._salary}`
        }
        set salary(value){
            console.log("You Are Not Allowed To Change Offical Accounts")
        }
    }
        let emp1=new Employee("Mike",4300);
        let emp2=new Employee("John",3200);
        
        // emp1.salary=6620;
        console.log(emp1.salary)
        console.log(emp2.salary)
        emp1.salary=34234
