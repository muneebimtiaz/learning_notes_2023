#include<iostream>
using namespace std;
int main(){
/*As the user enters more elements (10 in this case), the array dynamically doubles its size when it needs more space. So, after the 4th element, the size becomes 6, and after the 7th element, the size becomes 12.*/
int *dynamicArray;
int no_of_elements;
cout<<"enter no of elements user want to input:";
cin>>no_of_elements;
dynamicArray=new int[3]; //originally allocated array

for(int i=0;i<no_of_elements;i++){
	cout<<"element:";
	cin>>dynamicArray[i];
}
for(int i=0;i<no_of_elements;i++){
	cout<<dynamicArray[i]<<",";
}

delete[] dynamicArray; // This deletes the originally allocated array
cout<<"dynamicArray array deleted succesfully"<<endl;
//
//for(int i=0;i<no_of_elements;i++){
//	cout<<dynamicArray[i]<<endl;
//}
    return 0;
}