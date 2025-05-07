    /*
    class->objects
    classes are used to create one or more objects/structure for objects being created.
    instance properties ->is being define inside the constructor.
    instance methods ->is used to apply logic to those instance properties.
    */
    class Employee{
        constructor(_name,_age,_salary,_doj){
            // this->refers to current object that is created by that class.
            // parameters->which are now passed in throught constructors function and then these will be assigned to the instance properties of the paricular rectangle objects.
            this.name=_name;
            this.age=_age;
            this.salary=_salary;
            this.doj=_doj;
        }
        show(){
            // methods->are defined in actual class definition and they are generic to their actual claa and they are assigned the instance properties that are defined by the constuctor to give different results based on obj being used.
            console.log(`name:${this.name} age:${this.age} salary:${this.salary} dateofjoining:${this.doj}`)
        }
    }

    let employee1=new Employee("John",30,"$5500",2014);
    let employee2=new Employee("Mike",33,"$6000",2013);
    employee1.show();
    employee2.show();


console.log("Next Program")


    class Student{
        constructor(_name,_english,_science,_maths){
            this.name=_name;
            this.english=_english;
            this.science=_science;
            this.maths=_maths;
        }
        show(){
            console.log(`Student Name:${this.name} English Marks:${this.english} Science Marks:${this.science} Maths Marks:${this.maths}`)
        }
        get totalMarks(){
            this.total=this.english+this.science+this.maths;
            return this.total;
        }
        get showMarks(){
            console.log(`Total Marks:${this.total}`);
        }
        get grades(){
            this.per=Math.round((this.total/300)*100);
            console.log(`Percentage:${this.per}`);
            if(this.per>=90){
            console.log("Grade A")
            }else if(this.per>=80){
                console.log("Grade B")
            }else if(this.per>=70){
                console.log("Grade C")
            }else if(this.per>=60){
                console.log("Grade D")
            }else{
                console.log("Grade F")
            }
        }
    }
    let s1=new Student("muneeb",67,89,91);
    let s2=new Student("ali",37,59,81);
    s1.show()
    s1.totalMarks
    s1.showMarks
    s1.grades
    s2.show()
    s2.totalMarks
    s2.showMarks
    s2.grades
