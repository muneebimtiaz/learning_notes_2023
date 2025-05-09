#include<iostream>
using namespace std;
int main(){
	int age;
	char currency;
	string name;
	
//	integer input
	cout<<"enter your age please!: "<<endl;
	cin>>age;
	cout<<"so you are "<<age<<" years old"<<endl;

//	string input
	cout<<"Now enter your name: "<<endl;
	getline(cin,name,'$');
	cout<<"Nice to meet you "<<name<<endl;

//	character input
	cout<<"Enter a currency symbol:"<<endl;
	cin>>currency;
	cout<<"you have 19"<<currency<<" only";
	return 0;
}
