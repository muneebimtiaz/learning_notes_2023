//getters_setters
#include<iostream>
using namespace std;
// class declaration/prototype or declare a object
class car{
    private:
    // data members
	string name;
	int modelNumber;
	double cost;

    public:
	// member functions/methods
// member functions of a class can be accessed only by and object of that class,
// Member functions are functions inside a class that can access its private members (variables and functions).
    void set(string _name,int _modelNumber,double _cost){
        name=_name;
	    modelNumber=_modelNumber;
	    cost=_cost;
    }
	void get(){  //Getters are used to retrieve the values of private data members.
		cout<<"enter car name:"<<endl;
        cin>>name;
		cout<<"enter model number:"<<endl;
        cin>>modelNumber;
		cout<<"enter cost:"<<endl;
        cin>>cost;
	}
    void show(){  //Setters are used to modify the values of private data members.
        cout<<"car name:"<<name<<endl;
		cout<<"model number:"<<modelNumber<<endl;
		cout<<"cost:"<<cost<<endl;
    }
// there is no rule that data must be private and functons public;in some circumstances you may find you will need to use private functions and public data.
};
int main(){
    // objects definition
// an object is an instance of a class.objects are sometimes called instance variables.
    car objCar1,objCar2;

	// set values to data members using member function
    objCar1.set("honda",1636,25500.00);

    // get values from user using member function
    objCar2.get();
    cout<<endl;

    // display 
//  objCar1.show(); can be thought of as sending a message to the objCar1 object, asking it to display or show its data.
	objCar1.show();
	objCar2.show();
	return 0;
}

