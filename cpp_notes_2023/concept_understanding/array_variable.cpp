#include <iostream>
#include <string>
using namespace std;

int main(){
  	int max;
  	cout<<"enter no of elements:";
  	cin>>max;
  	int arr[max]={11,13,19};
	   
	for(int i=0;i<max;i++){
  		cout<<arr[i]<<endl;
	   }

    int max;
  	cout<<"enter no of elements:";
  	cin>>max;
   
   string anime[max]={"aot", "fmab", "jjba", "mha"};
   for(int i=0;i<max;i++){
  		cout<<anime[i]<<endl;
  	}

    return 0;
}
