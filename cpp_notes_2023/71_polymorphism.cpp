//* Polymorphism means "many shapes" and refers to the ability of different objects to respond to the same method or function call in a way that is appropriate for their individual types. */

/* Polymorphism is one of the four fundamental principles of OOP, along with encapsulation, inheritance, and abstraction.*/

/* Polymorphism is often achieved through inheritance and virtual functions.
A base class declares a virtual function, and derived classes override it with their specific implementations.
At runtime, the appropriate implementation of the virtual function is called based on the actual object's type.*/

/*
Topics Related to Polymorphism:

Virtual Functions: The concept of declaring and using virtual functions for polymorphism.
Abstract Classes and Pure Virtual Functions: Classes with pure virtual functions that cannot be instantiated and must be overridden by derived classes.
Dynamic Binding: The mechanism by which the appropriate function is determined at runtime.
Static Binding: When function calls are resolved at compile time, not suitable for achieving polymorphism.
Interface Classes: Classes that define a set of methods without providing implementations, often used in interfaces.
Function Overloading: Overloading functions with different parameter lists in the same class.
Operator Overloading: Overloading operators for custom types to enable polymorphic behavior for operators like +, -, etc.
Compile-Time Polymorphism: Polymorphism achieved at compile time, often through function overloading.
Run-Time Polymorphism: Polymorphism achieved at runtime, typically through inheritance and virtual functions.
Late Binding: Another term for dynamic binding, where the function call is resolved at runtime
*/


// bindings in C++ refer to the behavior of function calls and how the appropriate function implementation is determined. Early binding is associated with non-virtual functions, while late binding is associated with virtual functions and polymorphism, where the decision on which function to call is made at runtime based on the actual type of the object.

