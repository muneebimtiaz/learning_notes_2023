
        class Employee{
            constructor(name,age,doj){
                this.name=name;
                this.age=age;
                this.dateOfJoining=doj;
            }
            experience(){
                console.log(`Employee working with our company since ${this.dateOfJoining}.`);
            }
            showDetails(){
                console.log(`name:${this.name} age:${this.age} since:${this.dateOfJoining}`);
            }
        }
        class Manager extends Employee{
            constructor(name,age,doj,post,salary){
                super(name,age,doj);
                this.post=post;
                this.salary=salary;
            }
            showDetails(){
                //polymorphism
                super.showDetails();
                console.log(`post:${this.post} YearlySalary:${this.salary}`)
            }
        }

      let m1=new Manager("Jason",66,1993,"CEO","1.1M")
      m1.showDetails()
