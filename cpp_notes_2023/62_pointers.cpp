/*A pointer is a variable that store memory address. Like all other variables it also has a name, has to be declared and oGcupies sQme
space in memory. It is called pointer because it points to a particular location in memory by storingthe address of that location*/
#include <iostream>
using namespace std;
int main(){
	int a=8;
	float b=4.5;

// declaration of pointer variables
	int *ptr1;
	ptr1=&a;  //Each byte has an index number, which is called the address of that byte.
	// The address operator cannot be used with a, constant or an expression.
	// Valid, used with a '&a' variable,'&arr[1]'array element.

// declaration and assigning the pointer variable
	int *ptr1=&a;
	float *ptr2=&b;
	// When we declare a pointer variable it contains garbage value i.e, it may be pointing anywhere in the memory
	// it is also possible to assign the value of pointer variable to the other, 

	cout<<"Value of ptr1=adress of a:"<<ptr1<<endl; 
	cout<<"Value of ptr2=adress of b:"<<ptr2<<endl;
	cout<<"Address of ptr1:"<<&ptr1<<endl;
	cout<<"Address of ptr2:"<<&ptr1<<endl;
	cout<<"Value of a:"<<a<<","<<*ptr1<<","<<*(&ptr1)<<endl;  //By placing the indirection operator before a pointer variable, we can access the variable whose address iS stored in the pointer. 
	cout<<"Value of b:"<<b<<","<<*ptr2<<","<<*(&ptr2)<<endl;

	return 0; 
}

/*
what is meant by the term *(&ptr1), where ptr is a variable. Since &ptr is an address,
so dereferencing it with *. operator will give the variable at that address and the variable at that address is a;\
*/
