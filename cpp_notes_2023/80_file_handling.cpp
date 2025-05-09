#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
	char arr[100];
	cout<<"enter any form of data:"<<endl;
	cin.getline(arr,100);
	//write
	ofstream obj("file.txt");
	obj<<arr;
	obj.close();
	cout<<"data has entered successfully:";
	
	cout<<"to read data from txt file created before:"<<endl;
	char arr1[100];
	//read 
	ifstream obj1("file.txt");
	obj1.getline(arr1,100);
	obj1.close();
	cout<<arr1;
	cout<<"data has read successfully:"<<endl;
	return 0;

}

