#include<iostream>
#include<stdlib.h>
using namespace std;
int main(){
	int *iptr , n , i;
	cout<<"Enter no of elements you want : ";
	cin>>n;

	iptr=(int*)malloc(6*sizeof(int));
	
	for(i=0;i<n;i++){
		cout<<"Enter element no "<<i<<":";
		cin>>iptr[i];
	}
	cout<<"created: ";
	for(int i=0;i<n;i++){
		cout<<*(iptr+i)<<",";
	}
	
}