#include<iostream>
using namespace std;
int main(){

        int *dynamic;
        int count=3;
        dynamic=new int[count];
        dynamic[0]=10;
        dynamic[1]=20;
        dynamic[2]=30;
        dynamic[3]=40;
        dynamic[4]=50;

    for(int i=0;i<8;i++){
        cout<<dynamic[i]<<endl;
    }

    delete[] dynamic;
    cout<<"dynamic array deleted succesfully"<<endl;

    for(int i=0;i<6;i++){
        cout<<dynamic[i]<<endl;
    }

    return 0;
}