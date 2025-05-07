
    class Employee{
        name;
        present(){
            console.log("this employee is avaible");
        }
        notPresent(){
            console.log("this employee is not avaible");
        }
    }

    let emp1=new Employee();
    emp1.present()
    let emp2=new Employee();
    emp2.notPresent()
