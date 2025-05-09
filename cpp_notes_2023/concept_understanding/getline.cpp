//why we use getline in string case instead of cin
#include<iostream>
#include<string>
using namespace std;
int main(){
    string line;
    cout<<"enter the line:";
    cin>>line;
    cout<<"the line you enter:"<<line<<endl;;

    string line2;
    cout<<"enter the line again:";
    getline(cin,line2);
    cout<<"\nthe line you enter:"<<line2;
    return 0;
}

/*cin with the >> operator reads until it encounters whitespace (like space, tab, or newline) and stops, so it doesn't handle spaces within a single input.
getline(), on the other hand, reads the entire line, including spaces.*/