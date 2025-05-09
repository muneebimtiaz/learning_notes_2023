#include <iostream>
#include <fstream>
using namespace std;
int main() {
	char para[70];
	cout<<"input data:"<<endl;
	cin.getline(para,70);
	//write
	ofstream obj("myfile.txt",ios::app);// appent in a file using ios::app
	obj<<para;
	obj.close();
	cout<<"data write successfully"<<endl;
	
	char para1[70];
	cout<<"output data:"<<endl;
	//read
	ifstream obj1("myfile.txt");
	obj1.getline(para1,70);
	obj1.close();
	cout<<para1<<endl;
	cout<<"data read successfully"<<endl;
    return 0;
}

