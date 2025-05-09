// user defined functions
// Function to calculate the Fibonacci sequence iteratively
#include<iostream>
using namespace std;
// function declaration/prototype
void disp(int);

int main(){
	int terms;
	cout<<"enter no of terms:"<<endl;
	cin>>terms;
	
	if(terms>0){
		// call to function
		disp(terms);
	}else{
		cout<<"please enter a positive number.";
	}
	return 0;
}

void disp(int n){
	int a=0,b=1;
	// function definition
	for(int i=0;i<n;i++)	//function declarator
	{
		cout<<a<<" ";    //0
		int temp=a;		//temp=0,a=0
		a=b;		//a=1,b=1,temp=0
		b=temp+b;		//1=0+1
	}

}