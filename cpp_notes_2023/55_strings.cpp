#include<iostream>
#include<string>
using namespace std;
int main(){
    //string header file
	string sentence="have a good day";
	cout<<sentence.size()<<endl;
	cout<<sentence[7]<<endl;
	cout<<sentence.find("good",0)<<endl;
	cout<<sentence.substr(7,4)<<endl;

    //cstrings
	char str[7]={'m','u','n','\0','e','b','\0'};
	cout<<str<<endl;
	
	//stringconstants
	char str1[]="muneebimtiaz hhh";
	cout<<str1;
	
}
