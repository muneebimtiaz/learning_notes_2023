// overloaded constructors  // member functions declare outside the class
#include <iostream>
using namespace std;
class person{
	private:
		int age;
		double height;
	public:
	// a constructor is a member function that is executed automatically whenever an object is created.no return type is used for constructors.
	// if multiple members must be initialized they are separated by commas,the result is the initializer list also called member-inititalization list.
		// constructor (no args)
		person() : age(0),height(0){
			cout<<"i am a constructor"<<endl;
		}
		// constructor (two args)
		person(int a,double h) : age(a),height(h){
			cout<<"i am a constructor"<<endl;
		}
		// In C++, destructors are special member functions of a class that are used to release resources, clean up memory, and perform any necessary cleanup operations when an object is destroyed or goes out of scope.
		// Destructor 
		~person(){
			cout<<"I am a destructor"<<endl;
		}
		
	// member functions declare outside the class using scope resolution operator
		// funtion declaration
		void input(int,double);
		void show();
};
int main(){

	// initializing using constructors
	person p1;
	person p2(31,6.1);

	
	// update value of p1 using member function
	int a;
	double b;
	cout<<"enter values:"<<endl;
	cin>>a>>b;
	p1.input(a,b);	//function call
     
	// display
	p1.show(),p2.show();
	cout<<endl;
	
	return 0;
}

//function definition 
void person::input(int _age,double _height){
	age=_age;
	height=_height;	
}
void person::show(){
	cout<<"age of person:"<<age<<endl;
	cout<<"height of person:"<<height<<endl;
	cout<<endl;
}


