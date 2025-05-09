#include<iostream>
using namespace std;
int main(){
// break->break out of loop entirely
// continue->skip an iteration of a loop
// pass--->does nothing,act as a placeholder
/*The loop body, which consists of braces delimiting several statements, 
is called a block ofcode. One important aspect of a block is that a variable 
defined inside the block is not visible outside it*/

    for(int i=0;i<20;i++){
        if(i==6){
            // break;
            continue;
        }
    cout<<i<<endl;
    }
    return 0;
}