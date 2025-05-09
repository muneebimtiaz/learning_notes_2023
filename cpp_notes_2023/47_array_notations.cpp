// Notations in an array refer to the various ways you can access and manipulate elements within an array in C++.
#include <iostream>
// the name of the array is its address.not need to use '&' operator
// you cant increment the address but you can increment the pointer
using namespace std;
int main(){
	//array accessed with subscript notation
	int sn1[5]={44,33,6,4,86};
	for(int i=0;i<5;i++){
		cout<<sn1[i]<< " ";
    }
    cout<<endl;

	//array accessed with pointer notation
	int pn1d[5]={44,33,6,4,86};
	for(int i=0;i<5;i++){
		cout<<*(pn1d+i)<< " ";
	}
    cout<<endl;


	// example 2
	int arr[4] = {10, 11, 12, 13};
    cout<<(arr+3)<<endl;
    cout<<*(arr+3)<<endl;
    
    int arr2[3][4] = { {10, 11, 12, 13}, {20, 21, 22, 23}, {30, 31, 32, 33} };
    cout<<arr2[1][3]<<endl;
	cout<<*(*(arr2+1)+3)<<endl;

	return 0;
}

