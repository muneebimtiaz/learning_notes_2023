#include<iostream>
using namespace std;
class base{
	private:
		int num; //only access in their block of code.to access private data from outside the class using an obj we need to create a public method.
	protected:
		string name; //similar to private but ist can be access from those classes as well whoes are inherited from base class.
	//to access protected data from outside the class using an obj of that class or inherited classes from them we need to create a public method.
	public:
		char symbol; 

		void print(){
			cout<<num<<endl;
			cout<<name<<endl;
			cout<<symbol<<endl;
		}
		base() : num(5),name("chen"),symbol('#'){
			cout<<"i am a constructor"<<endl;
		}

};

class derived:public base{
	public:
		void printData(){
			base::print();
		}
};
int main(){
	base b1; 
	derived d1;
	b1.print();
	d1.printData();
	return 0;
}

//access specifiers during inheritance

/*
Public Inheritance:
When you inherit a class publicly, the public members of the base class remain public in the derived class, and the protected members of the base class become protected members in the derived class. Private members of the base class remain inaccessible in the derived class.
eg.class Derived : public Base{};

Protected Inheritance:
When you inherit a class as protected, the public and protected members of the base class become protected members in the derived class. Private members of the base class remain inaccessible in the derived class.
eg.class Derived : protected Base{};

Private Inheritance:
When you inherit a class as private, all members of the base class become private members in the derived class, regardless of their access specifiers in the base class. This means that you can't directly access any members of the base class from outside the derived class.
eg.class Derived : private Base{};
*/