// The one-dimensional arrays are known as vectors and two-dimensional arrays are known as matrice:
/*Static Array:
A static array is a fixed-size array where the number of elements is determined at compile-time.
The size of a static array is constant throughout its lifetime and cannot be changed once it's defined.
Elements in a static array are stored in contiguous memory locations.
Static arrays are declared using a fixed size within square brackets.*/

#include <iostream>
using namespace std;
int main(){
    // declare and initialize and array of strings
    // The size of an array is fixed at the time of declaration and cannot be changed during runtime. It represents the total number of elements the array can store.
    string anime[4]={"aot", "fmab", "jjba", "mha"};

    // Accessing and printing elements from the array
    cout<<anime[0]<<endl; // "aot"
    cout<<anime[1]<<endl; // "fmab"
    cout<<anime[2]<<endl; // "jjba"
    cout<<anime[3]<<endl; // "mha"  
    // Accessing elements within bounds (array bounds)
    cout<<"Element at index 0: "<< anime[0]<<endl; // Valid
    cout<<"Element at index 3: "<< anime[3]<<endl; // Valid
    // Accessing elements out of bounds (undefined behavior)
    cout<<"Element at index -1: "<< anime[-1]<<endl; // Invalid
    cout<<"Element at index 4: "<<anime[4]<<endl;   // Invalid

    // Changing an element in the array
    anime[3]="jk";
    cout<<anime[3]<<endl; // "jk"

    // Print the entire array using a loop
    for(int i=0;i<4;i++){
        cout<<anime[i]<<" ";
    }
    cout<<endl;
    return 0;
}
// Q:In C++, if an array has a size n, we can store upto n number of elements in the array. However, what will happen if we store less than n number of elements.
// A:In such cases, the compiler assigns random values to the remaining places. Oftentimes, this random value is simply 0.